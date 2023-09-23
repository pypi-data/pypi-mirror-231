import os
import argparse
from django.core.management.base import BaseCommand
from drf_swagger_utils.server.constants.cleanapp import *
from drf_swagger_utils.server.templates.app_template import APP_CONFIG


class Command(BaseCommand):
    help = 'My custom Django management command'

    def handle(self, *args, **kwargs):
        # Your custom command logic goes here
        main()
        self.stdout.write(self.style.SUCCESS('Custom command executed successfully!'))


def create_app(args):
    help = 'Create a Clean App for your project'

    if args['app']:
        app_name = args['app']

        if not os.path.exists(app_name):
            try:
                app_directory = os.path.join(app_name)
                os.makedirs(app_directory)
                create_file(app_directory, '__init__.py')
                create_app_required_files(app_directory, app_name)

                # Create modules
                for module in directory_list:
                    module_directory = os.path.join(app_directory, module)
                    os.makedirs(module_directory)
                    create_file(module_directory, '__init__.py')
                    if module == "tests":
                        for sub_module in tests_directory_list:
                            create_tests_directory(module_directory, sub_module)
                    elif module == "interactors":
                        for sub_module in interactors_directory:
                            create_tests_directory(module_directory, sub_module)

                print('App "{}" created successfully in "{}".'.format(app_name, app_directory))
            except OSError:
                print('Error creating app directory.', OSError)

        else:
            print(("App already exists: {}".format(app_name)))
    else:
        print("App already exists: ")


def create_file(directory, file_name, content=''):
    with open(os.path.join(directory, file_name), 'w') as file:
        file.write(content)


def create_directory(directory_path, package_name):
    os.makedirs(directory_path, package_name)


def create_tests_directory(directory, sub_module):
    module_directory = os.path.join(directory, sub_module)
    os.makedirs(module_directory)
    create_file(module_directory, '__init__.py')


def create_app_required_files(app_directory, app_name):
    for file in ['admin.py', 'app.py', 'db_dicts.py', 'db_fixtures.py']:
        create_file(app_directory, file)
    app_config_code = APP_CONFIG.replace("{{app}}", app_name)
    create_file(app_directory, 'app.py', app_config_code)


def main():
    parser = argparse.ArgumentParser(description="Create Clean App")
    parser.add_argument("command", choices=["create_app"], help="The command to run")
    args = parser.parse_args()

    # Check the specified command and execute the corresponding function
    if args.command == "create_app":
        create_app(args)
    else:
        print("Invalid command. Use 'create_app' as the command.")


if __name__ == "__main__":
    main()
