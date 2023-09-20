import os
from time import sleep
from .funcs import create_dir_and_venv, activate_venv_and_install_reqs


if __name__ == '__main__':

    full_path = None

    try:
        project_name = input('\nPROJECT NAME: ')
        full_path = os.path.join(os.getcwd(), project_name)
        os.mkdir(full_path)

        print('\nStarting creation of virtual environment and directory structure')
        create_dir_and_venv(project_name, full_path)
        print('Created virtual environment and directory structure')

        print('Starting installation of packages into virtual environment')
        activate_venv_and_install_reqs(project_name, full_path)

        print('Successfully Completed Setup\nExiting template_flask...')
        sleep(1)

    except KeyboardInterrupt:
        if full_path is None:
            m = ''
        else:
            m = f'Partial Flask Directory created at {full_path}, delete if not needed\n'
        print(f'\n\n{m}Exiting template_flask...')
        sleep(1)
