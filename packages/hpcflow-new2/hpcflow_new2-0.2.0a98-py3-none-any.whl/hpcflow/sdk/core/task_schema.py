from contextlib import contextmanager
import copy
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Union

from rich import print as rich_print
from rich.table import Table

from hpcflow.sdk import app
from hpcflow.sdk.core.parameters import Parameter
from .json_like import ChildObjectSpec, JSONLike
from .parameters import NullDefault, ParameterPropagationMode, SchemaInput
from .utils import check_valid_py_identifier


@dataclass
class TaskObjective(JSONLike):
    _child_objects = (
        ChildObjectSpec(
            name="name",
            is_single_attribute=True,
        ),
    )

    name: str

    def __post_init__(self):
        self.name = check_valid_py_identifier(self.name)


class TaskSchema(JSONLike):
    """Class to represent the inputs, outputs and implementation mechanism of a given
    task.

    Parameters
    ----------
    objective
        This is a string representing the objective of the task schema.
    actions
        A list of Action objects whose commands are to be executed by the task.
    method
        An optional string to label the task schema by its method.
    implementation
        An optional string to label the task schema by its implementation.
    inputs
        A list of SchemaInput objects that define the inputs to the task.
    outputs
        A list of SchemaOutput objects that define the outputs of the task.

    """

    _validation_schema = "task_schema_spec_schema.yaml"
    _hash_value = None
    _validate_actions = True

    _child_objects = (
        ChildObjectSpec(name="objective", class_name="TaskObjective"),
        ChildObjectSpec(
            name="inputs",
            class_name="SchemaInput",
            is_multiple=True,
            parent_ref="_task_schema",
        ),
        ChildObjectSpec(name="outputs", class_name="SchemaOutput", is_multiple=True),
        ChildObjectSpec(
            name="actions",
            class_name="Action",
            is_multiple=True,
            parent_ref="_task_schema",
        ),
    )

    def __init__(
        self,
        objective: Union[app.TaskObjective, str],
        actions: List[app.Action] = None,
        method: Optional[str] = None,
        implementation: Optional[str] = None,
        inputs: Optional[List[Union[app.Parameter, app.SchemaInput]]] = None,
        outputs: Optional[List[Union[app.Parameter, app.SchemaOutput]]] = None,
        version: Optional[str] = None,
        _hash_value: Optional[str] = None,
    ):
        self.objective = objective
        self.actions = actions or []
        self.method = method
        self.implementation = implementation
        self.inputs = inputs or []
        self.outputs = outputs or []
        self._hash_value = _hash_value

        self._set_parent_refs()

        self._validate()
        self.actions = self._expand_actions()
        self.version = version
        self._task_template = None  # assigned by parent Task

        # if version is not None:  # TODO: this seems fragile
        #     self.assign_versions(
        #         version=version,
        #         app_data_obj_list=self.app.task_schemas
        #         if app.is_data_files_loaded
        #         else [],
        #     )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.objective.name!r})"

    @property
    def info(self):
        """Show attributes of the task schema."""
        tab = Table(show_header=False)
        tab.add_column()
        tab.add_column()
        tab.add_row("Objective", self.objective.name)
        tab.add_row("Actions", str(self.actions))

        tab_ins = Table(show_header=False, box=None)
        tab_ins.add_column()
        for inp in self.inputs:
            def_str = ""
            if not inp.multiple:
                if inp.default_value is not NullDefault.NULL:
                    def_str = f" [i]default[/i]={inp.default_value}"
            tab_ins.add_row(inp.parameter.typ + def_str)

        tab_outs = Table(show_header=False, box=None)
        tab_outs.add_column()
        for out in self.outputs:
            tab_outs.add_row(out.parameter.typ)

        tab.add_row("Inputs", tab_ins)
        tab.add_row("Outputs", tab_outs)
        rich_print(tab)

    def __eq__(self, other):
        if type(other) is not self.__class__:
            return False
        if (
            self.objective == other.objective
            and self.actions == other.actions
            and self.method == other.method
            and self.implementation == other.implementation
            and self.inputs == other.inputs
            and self.outputs == other.outputs
            and self.version == other.version
            and self._hash_value == other._hash_value
        ):
            return True
        return False

    def __deepcopy__(self, memo):
        kwargs = self.to_dict()
        obj = self.__class__(**copy.deepcopy(kwargs, memo))
        obj._task_template = self._task_template
        return obj

    @classmethod
    @contextmanager
    def ignore_invalid_actions(cls):
        try:
            cls._validate_actions = False
            yield
        finally:
            cls._validate_actions = True

    def _validate(self):
        if isinstance(self.objective, str):
            self.objective = self.app.TaskObjective(self.objective)

        if self.method:
            self.method = check_valid_py_identifier(self.method)
        if self.implementation:
            self.implementation = check_valid_py_identifier(self.implementation)

        # coerce Parameters to SchemaInputs
        for idx, i in enumerate(self.inputs):
            if isinstance(
                i, Parameter
            ):  # TODO: doc. that we should use the sdk class for type checking!
                self.inputs[idx] = self.app.SchemaInput(i)

        # coerce Parameters to SchemaOutputs
        for idx, i in enumerate(self.outputs):
            if isinstance(i, Parameter):
                self.outputs[idx] = self.app.SchemaOutput(i)
            elif isinstance(i, SchemaInput):
                self.outputs[idx] = self.app.SchemaOutput(i.parameter)

        # check action input/outputs
        if self._validate_actions:
            has_script = any(
                i.script and not i.input_file_generators and not i.output_file_parsers
                for i in self.actions
            )

            all_outs = []
            extra_ins = set(self.input_types)

            act_ins_lst = [act.get_input_types() for act in self.actions]
            act_outs_lst = [act.get_output_types() for act in self.actions]

            schema_ins = set(self.input_types)
            schema_outs = set(self.output_types)

            all_act_ins = set(j for i in act_ins_lst for j in i)
            all_act_outs = set(j for i in act_outs_lst for j in i)

            non_schema_act_ins = all_act_ins - schema_ins
            non_schema_act_outs = set(all_act_outs - schema_outs)

            extra_act_outs = non_schema_act_outs
            seen_act_outs = []
            for act_idx in range(len(self.actions)):
                for act_in in [
                    i for i in act_ins_lst[act_idx] if i in non_schema_act_ins
                ]:
                    if act_in not in seen_act_outs:
                        raise ValueError(
                            f"Action {act_idx} input {act_in!r} of schema {self.name!r} "
                            f"is not a schema input, but nor is it an action output from "
                            f"a preceding action."
                        )
                seen_act_outs += [
                    i for i in act_outs_lst[act_idx] if i not in seen_act_outs
                ]
                extra_act_outs = extra_act_outs - set(act_ins_lst[act_idx])
                act_inputs = set(act_ins_lst[act_idx])
                act_outputs = set(act_outs_lst[act_idx])
                extra_ins = extra_ins - act_inputs
                all_outs.extend(list(act_outputs))

            if extra_act_outs:
                raise ValueError(
                    f"The following action outputs of schema {self.name!r} are not schema"
                    f" outputs, but nor are they consumed by subsequent actions as "
                    f"action inputs: {tuple(extra_act_outs)!r}."
                )

            if extra_ins and not has_script:
                # TODO: bit of a hack, need to consider script ins/outs later
                # i.e. are all schema inputs "consumed" by an action?

                # consider OFP inputs:
                for act_i in self.actions:
                    for OFP_j in act_i.output_file_parsers:
                        extra_ins = extra_ins - set(OFP_j.inputs or [])

                if self.actions and extra_ins:
                    # allow for no actions (e.g. defining inputs for downstream tasks)
                    raise ValueError(
                        f"Schema {self.name!r} inputs {tuple(extra_ins)!r} are not used "
                        f"by any actions."
                    )

            missing_outs = set(self.output_types) - set(all_outs)
            if missing_outs and not has_script:
                # TODO: bit of a hack, need to consider script ins/outs later
                raise ValueError(
                    f"Schema {self.name!r} outputs {tuple(missing_outs)!r} are not "
                    f"generated by any actions."
                )

    def _expand_actions(self):
        """Create new actions for input file generators and output parsers in existing
        actions."""
        return [j for i in self.actions for j in i.expand()]

    def make_persistent(self, workflow: app.Workflow, source: Dict) -> List[int]:
        new_refs = []
        for input_i in self.inputs:
            for lab_info in input_i.labelled_info():
                if "default_value" in lab_info:
                    _, dat_ref, is_new = lab_info["default_value"].make_persistent(
                        workflow, source
                    )
                    new_refs.extend(dat_ref) if is_new else None
        return new_refs

    @property
    def name(self):
        out = (
            f"{self.objective.name}"
            f"{f'_{self.method}' if self.method else ''}"
            f"{f'_{self.implementation}' if self.implementation else ''}"
        )
        return out

    @property
    def input_types(self):
        return tuple(j for i in self.inputs for j in i.all_labelled_types)

    @property
    def output_types(self):
        return tuple(i.typ for i in self.outputs)

    @property
    def provides_parameters(self) -> Tuple[Tuple[str, str]]:
        out = []
        for schema_inp in self.inputs:
            for labelled_info in schema_inp.labelled_info():
                prop_mode = labelled_info["propagation_mode"]
                if prop_mode is not ParameterPropagationMode.NEVER:
                    out.append(
                        (schema_inp.input_or_output, labelled_info["labelled_type"])
                    )
        for schema_out in self.outputs:
            if schema_out.propagation_mode is not ParameterPropagationMode.NEVER:
                out.append((schema_out.input_or_output, schema_out.typ))
        return tuple(out)

    @property
    def task_template(self):
        return self._task_template

    @classmethod
    def get_by_key(cls, key):
        """Get a config-loaded task schema from a key."""
        return cls.app.task_schemas.get(key)

    def get_parameter_dependence(self, parameter: app.SchemaParameter):
        """Find if/where a given parameter is used by the schema's actions."""
        out = {"input_file_writers": [], "commands": []}
        for act_idx, action in enumerate(self.actions):
            deps = action.get_parameter_dependence(parameter)
            for key in out:
                out[key].extend((act_idx, i) for i in deps[key])
        return out

    def get_key(self):
        return (str(self.objective), self.method, self.implementation)
