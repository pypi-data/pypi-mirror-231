from django.core.management.base import BaseCommand
from django_swagger_utils.server.generators.build_app import build
from django_swagger_utils.server.generators.create_app import create_app


class Command(BaseCommand):
    help = 'My custom Django management command'

    def add_arguments(self, parser):
        # Define the 'command' argument with choices for sub-commands
        parser.add_argument("command", choices=["build", "create_app"], help="The command to run")

        # Add other command-specific options as needed
        parser.add_argument("--app", help="Command-specific option")
        args = parser.parse_args()

    def handle(self, *args, **kwargs):
        # 'command' is automatically available as self.command
        if self.command == "build":
            build(self.options)
        elif self.command == "create_app":
            create_app(self.options)
        else:
            print("Invalid command. Use 'build' or 'create_app' as the command.")
