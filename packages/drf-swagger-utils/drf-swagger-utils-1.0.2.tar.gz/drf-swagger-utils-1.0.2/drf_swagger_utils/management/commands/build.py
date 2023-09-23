import argparse
import os
from django.apps import apps
from .generators import APIViewGenerator, ViewSetGenerator, \
    FunctionViewGenerator, ModelViewSetGenerator

import django
from django.conf import settings


def generate_views(app_name, content):
    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=[app_name],
        # Add other settings as needed
    )
    django.setup()
    installed_apps = settings.INSTALLED_APPS
    print("installed_apps:",installed_apps)
    app_config = apps.get_app_config(app_name)
    force = True  # Set this based on your requirements

    # Create instances of the generator classes
    function_view_generator = FunctionViewGenerator(app_config, force)

    # Generate the code by calling the appropriate methods
    function_view_result = function_view_generator.generate_views(app_name)

    # You can print or handle the results as needed
    print(function_view_result)


def generate_view_urls():
    pass


def generate_serializers():
    pass


def build(args):
    # Implement the logic for your custom command here
    print(("Building the app", args['app']))
    spec_path = "{}/api_specs/api_spec.json".format(args['app'])

    if spec_path:
        if os.path.exists(spec_path):
            try:
                with open(spec_path, "r") as file:
                    file_contents = file.read()
                    generate_views(args['app'], file_contents)
            except FileNotFoundError:
                print(("File not found: {}".format(spec_path)))

        else:
            print(("Directory does not exist: {}".format(spec_path)))

    else:
        print("Directory path not provided. Use '--directory' to specify the directory.")


def main():
    parser = argparse.ArgumentParser(description="My Custom Command")

    # Add a command argument (e.g., "build") to specify the command
    parser.add_argument("command", choices=["build"], help="The command to run")

    # Add other command-specific options as needed
    parser.add_argument("--app", help="Command-specific option")

    args = parser.parse_args()

    # Check the specified command and execute the corresponding function
    if args.command == "build":
        build(args)
    else:
        print("Invalid command. Use 'build' as the command.")


if __name__ == "__main__":
    main()
