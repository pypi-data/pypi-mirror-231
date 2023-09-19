from setuptools import setup
from setuptools import find_packages

setup(
    name             = 'lsaf_log_module',
    version          = '0.0.2',
    author           = 'Ricardo Capote',
    maintainer       = 'Sara Luis',
    maintainer_email = 'sm.luis16@gmail.com',
    description      = 'Python logging module wrapper with extra detail.',
    url              = 'https://gitlab.com/helpdesk.landsaf/log_module',
    license          = 'APL 2',
    packages         = find_packages(),
    install_requires = ['pyyaml']
)
