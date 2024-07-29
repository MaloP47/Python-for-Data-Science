"""Setup for package"""

from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    long_description=open('README.md').read(),
    author='mpeulet',
    author_email='mpeulet@student.42.fr',
    url='https://github.com/MaloP47',
    find_packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license='GPLv3',
    installer='pip'
)
