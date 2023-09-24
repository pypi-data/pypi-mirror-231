
from setuptools import setup, find_packages


version = '1.1.0'
url = 'https://github.com/pmaigutyak/mp-history'

setup(
    name='django-mp-history',
    version=version,
    description='Django history app',
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
)
