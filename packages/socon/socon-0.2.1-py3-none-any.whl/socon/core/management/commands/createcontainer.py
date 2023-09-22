from argparse import ArgumentParser
from typing import Union

from socon.core.management.base import Config
from socon.core.management.templates import TemplateCommand


class CreateContainerCommand(TemplateCommand):
    help: str = (
        "Creates a Socon container directory structure for the given container "
        "name in the current directory or optionally in the given directory."
    )
    missing_args_message: str = "You must provide a container name."
    template_prefix: str = "container"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("name", help="Name of the container.")
        parser.add_argument("--target", help="Optional path to the container")

    def handle(self, config: Config) -> Union[str, None]:
        container_name = config.getoption("name")
        target = config.getoption("target")
        super().handle(config, container_name, target)
