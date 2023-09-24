import argparse
from django.core.management.base import BaseCommand
from django_swagger_utils.server.generators.build_app import build


class Command(BaseCommand):
    help = 'My custom Django management command'

    def add_arguments(self, parser):
        # Define the 'command' argument with choices for sub-commands
        parser.add_argument("command", choices=["build"], help="The command to run")

        # Add other command-specific options as needed
        parser.add_argument("--app", help="Command-specific option")

    def handle(self, *args, **kwargs):
        # 'command' is automatically available as self.command
        if self.command == "build":
            build(self.options)
        else:
            print("Invalid command. Use 'build' as the command.")


if __name__ == "__main__":
    Command().execute()
