# Clean dist folder prior to new sdist and bdist_wheel
import os
import setuptools

dist = os.path.join(os.path.dirname(__file__), 'dist')
dist_archive = os.path.join(os.path.dirname(__file__), 'dist_archive')
for file in os.listdir(dist):
    current = os.path.join(dist, file)
    with open(current, mode='rb') as f:
        contents = f.read()
    with open(os.path.join(dist_archive, file), mode='wb') as f:
        f.write(contents)
    os.remove(current)
##################################################################################


keywords = ['flask', 'directory structure', 'cookie cutter'
            'venv', 'bootstrap']

with open("README.txt", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='template_flask',
    version="3.2",
    author='Zach Beebe',
    author_email='z.beebe@yahoo.com',
    description='Python module for creating a template flask app structure and virtual environment, along with Bootstrap examples',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/zacharybeebe/template_flask',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    keywords=keywords,
    python_requires='>=3.6',
    py_modules=['template_flask'],
    include_package_data=True
)
