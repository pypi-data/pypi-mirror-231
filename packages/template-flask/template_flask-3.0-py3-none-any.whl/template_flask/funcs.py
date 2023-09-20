import os
import site
import venv
import subprocess
import sys
import time
from random import choice, randrange
from .constants import *


def generate_random_secret_key():
    key = ''
    for i in range(32):
        alpha = choice([chr(randrange(65, 91)), chr(randrange(97, 123))])
        num = chr(randrange(48, 58))
        sym = choice([chr(randrange(33, 48)), chr(randrange(58, 65)), chr(randrange(123, 127))])
        key += choice([alpha, num, sym])
    return key


def copy_bootstrap(dest_path, bs_type):
    if bs_type in ['css', 'js']:
        end_path = os.path.join(os.path.join('bootstrap', 'static'), bs_type)
    else:
        end_path = os.path.join('bootstrap', bs_type)
    src_path = os.path.join(os.path.dirname(__file__), end_path)

    for filename in os.listdir(src_path):
        iterables = []
        src_file = os.path.join(src_path, filename)
        with open(src_file, 'r') as f:
            for line in f.readlines():
                fill = line.replace('\n', '')
                iterables.append([f'''{fill}''', False])

        dest_file = os.path.abspath(os.path.join(dest_path, filename))
        write_file(dest_file, iterables)


def write_file(file_path, iterable_lines, fills: dict={}):
    with open(file_path, 'w') as f:
        for line in iterable_lines:
            line_to_write, needs_fill = line

            if needs_fill:
                f.write(f'{line_to_write.format(**fills)}\n')
            else:
                f.write(f'{line_to_write}\n')


def create_dir_and_venv(project_name: str, full_path: str):
    FILLS = {
        'app': project_name,
        'secret_key': generate_random_secret_key(),
        'py_version': f'{sys.version_info.major}.{sys.version_info.minor}'
    }

    venv_path = os.path.join(full_path, 'venv')
    venv.create(venv_path, with_pip=True)

    package_path = os.path.join(full_path, f'{project_name}_app')
    config_dir = os.path.join(package_path, 'config')
    models_dir = os.path.join(package_path, 'models')
    routes_dir = os.path.join(package_path, 'routes')

    static_dir = os.path.join(package_path, 'static')
    css_dir = os.path.join(static_dir, 'css')
    img_dir = os.path.join(static_dir, 'img')
    js_dir = os.path.join(static_dir, 'js')
    css_boot = os.path.join(css_dir, 'bootstrap')
    js_boot = os.path.join(js_dir, 'bootstrap')
    js_fetcher = os.path.join(js_dir, 'fetcher.js')

    templates_dir = os.path.join(package_path, 'templates')
    templates_boot = os.path.join(templates_dir, 'bootstrap')
    index_path = os.path.join(templates_dir, 'index.html')

    config_init = os.path.join(config_dir, '__init__.py')
    config_config = os.path.join(config_dir, 'config.py')

    models_init_hint = os.path.join(models_dir, '_LOOK IN MODELS __INIT__.txt')
    models_init = os.path.join(models_dir, '__init__.py')
    models_db = os.path.join(models_dir, 'db.py')
    models_datatypes = os.path.join(models_dir, 'datatypes.py')
    models_user = os.path.join(models_dir, 'user.py')
    models_other_model = os.path.join(models_dir, 'other_model.py')

    routes_init = os.path.join(routes_dir, '__init__.py')
    routes_routes = os.path.join(routes_dir, 'routes.py')

    run_main = os.path.join(full_path, 'wsgi.py')
    init_main = os.path.join(package_path, '__init__.py')

    dockerfile = os.path.join(full_path, 'Dockerfile')
    dockerignore = os.path.join(full_path, '.dockerignore')

    os.mkdir(package_path)
    os.mkdir(config_dir)
    os.mkdir(models_dir)
    os.mkdir(routes_dir)
    os.mkdir(static_dir)
    os.mkdir(css_dir)
    os.mkdir(img_dir)
    os.mkdir(js_dir)
    os.mkdir(css_boot)
    os.mkdir(js_boot)
    os.mkdir(templates_dir)
    os.mkdir(templates_boot)

    write_file(index_path, INDEX_HTML, fills=FILLS)

    write_file(config_init, CONFIG_INIT)
    write_file(config_config, CONFIG_CONFIG, fills=FILLS)

    write_file(js_fetcher, JS_FETCHER)

    write_file(models_init_hint, MODEL_INIT_HINT)
    write_file(models_init, MODEL_INIT, fills=FILLS)
    write_file(models_db, MODEL_DB)
    write_file(models_datatypes, MODEL_DATATYPES)
    write_file(models_user, MODEL_USER, fills=FILLS)
    write_file(models_other_model, MODEL_OTHER_MODEL, fills=FILLS)

    write_file(routes_init, ROUTE_INIT)
    write_file(routes_routes, ROUTE_ROUTE, fills=FILLS)

    write_file(run_main, RUN, fills=FILLS)
    write_file(init_main, INIT, fills=FILLS)

    write_file(dockerfile, DOCKERFILE, fills=FILLS)
    write_file(dockerignore, DOCKERIGNORE, fills=FILLS)

    copy_bootstrap(templates_boot, 'templates')
    copy_bootstrap(css_boot, 'css')
    copy_bootstrap(js_boot, 'js')


def activate_venv_and_install_reqs(project_name: str, full_path: str):
    reqs_path = os.path.join(full_path, 'requirements.txt')
    venv_path = os.path.join(full_path, os.path.join('venv', 'Scripts'))

    os.chdir(venv_path)
    cmd = f'"{sys.executable}" -m pip install {" ".join(REQUIREMENTS)}'
    subprocess.run(cmd, shell=True)
    print()

    cmd = f'"{sys.executable}" -m pip freeze'
    reqs = [x.decode('utf-8').split('==')[0]
            for x in subprocess.run(cmd, check=True, stdout=subprocess.PIPE, shell=True).stdout.splitlines()]

    print('Completed installing requirements into virtual environment\n')
    for req in reqs:
        print(req)
        time.sleep(0.05)
    print()
    print('Packages above have been automatically installed into virtual environment')

    with open(reqs_path, 'w') as f:
        for req in reqs:
            f.write(f"""{req}\n""")

    print('Completed writing initial "requirements.txt"\n')
    print(DIRECTORY_STRUCTURE.format(app=project_name))













