# coding: utf-8
import os

from pkg_resources import Requirement
from setuptools import setup
from setuptools import find_packages


def _get_requirements(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            req = Requirement(line)
            req_str = req.name + str(req.specifier)
            if req.marker:
                req_str += '; ' + str(req.marker)
            yield req_str


def _read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__),
            fname)).read()
    except IOError:
        return ''

setup(
    name='edupfr',
    url='https://stash.bars-open.ru/projects/EDUBASE/repos/edupfr',
    license='MIT',
    author='BARS Group',
    author_email='bars@bars-open.ru',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description='Клиенты для веб-сервисов Пенсионного фонда РФ',
    install_requires=_get_requirements('requirements.txt'),
    include_package_data=True,
    dependency_links=(
        'http://pypi.bars-open.ru/simple/m3-builder',
    ),
    setup_requires=(
        'm3-builder>=1.0.1',
    ),
    set_build_info=os.path.dirname(__file__),
)
