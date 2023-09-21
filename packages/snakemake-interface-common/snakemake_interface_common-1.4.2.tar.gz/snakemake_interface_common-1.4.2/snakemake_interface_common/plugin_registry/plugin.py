__author__ = "Johannes Köster"
__copyright__ = "Copyright 2022, Johannes Köster, Vanessa Sochat"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from abc import ABC, abstractmethod
from dataclasses import fields
from dataclasses import MISSING, Field, dataclass
from typing import Any, Type
import copy
from snakemake_interface_common.exceptions import WorkflowError

from snakemake_interface_common.exceptions import InvalidPluginException
from snakemake_interface_common._common import (
    dataclass_field_to_argument_args,
)

# Valid Argument types (to distinguish from empty dataclasses)
ArgTypes = (str, int, float, bool, list)


@dataclass
class SettingsBase:
    """Base class for plugin settings."""

    def get_items_by_category(self, category: str):
        """Yield all items (name, value) of the given group (as defined by the)
        optional category field in the metadata.
        """
        for field in fields(self.__class__):
            if field.metadata.get("subgroup") == category:
                yield field.name, getattr(self, field.name)


class PluginBase(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def cli_prefix(self) -> str:
        ...

    @property
    @abstractmethod
    def settings_cls(self) -> Type[SettingsBase]:
        ...

    def has_settings_cls(self):
        """Determine if a plugin defines custom executor settings"""
        return self.settings_cls is not None

    def register_cli_args(self, argparser):
        """Add arguments derived from self.executor_settings to given
        argparser."""

        # Cut out early if we don't have custom parameters to add
        if not self.has_settings_cls():
            return

        # Convenience handle
        params = self.settings_cls

        # Assemble a new dataclass with the same fields, but with prefix
        # fields are stored at dc.__dataclass_fields__
        dc = copy.deepcopy(params)
        for field in fields(params):
            if "help" not in field.metadata:
                raise InvalidPluginException(
                    "Fields of ExecutorSettings must have a help string."
                )
            if field.default is MISSING and field.default_factory is MISSING:
                raise InvalidPluginException(
                    "Fields of ExecutorSettings must have a default value."
                )

            # Executor plugin dataclass members get prefixed with their
            # name when passed into snakemake args.
            prefixed_name = self._get_prefixed_name(field)

            # Since we use the helper function below, we
            # need a new dataclass that has these prefixes
            del dc.__dataclass_fields__[field.name]
            field.name = prefixed_name
            dc.__dataclass_fields__[field.name] = field

        settings = argparser.add_argument_group(f"{self.name} executor settings")

        for field in fields(dc):
            args, kwargs = dataclass_field_to_argument_args(field)

            if field.metadata.get("env_var"):
                kwargs["env_var"] = f"SNAKEMAKE_{prefixed_name.upper()}"
            settings.add_argument(*args, **kwargs)

    def get_settings(self, args) -> SettingsBase:
        """Return an instance of self.executor_settings with values from args.

        This helper function will select executor plugin namespaces arguments
        for a dataclass. It allows us to pass them from the custom executor ->
        custom argument parser -> back into dataclass -> snakemake.
        """
        if not self.has_settings_cls():
            return SettingsBase()

        # We will parse the args from snakemake back into the dataclass
        dc = self.settings_cls

        # Iterate through the args, and parse those in the namespace
        kwargs = {}

        # These fields will have the executor prefix
        for field in fields(dc):
            # This is the actual field name without the prefix
            name = field.name.replace(f"{self.name}_", "", 1)
            value = getattr(args, field.name, None)

            if field.metadata.get("required") and value is None:
                cli_arg = self._get_cli_arg(field)
                raise WorkflowError(
                    f"Missing required argument {cli_arg} for executor {self.name}."
                )

            # This will only add instantiated values, and
            # skip over dataclasses._MISSING_TYPE and similar
            if isinstance(value, ArgTypes):
                kwargs[name] = value

        # At this point we want to convert back to the original dataclass
        return dc(**kwargs)

    def _get_cli_arg(self, field: Field[Any]) -> str:
        return self._get_prefixed_name(field).replace("_", "-")

    def _get_prefixed_name(self, field: Field[Any]) -> str:
        return f"{self.cli_prefix}_{field.name}"
