from setuptools import find_packages, setup, Command
from pathlib import Path
# Package meta-data.

NAME = 'get-version'
DESCRIPTION = 'Get the version of so many things.'
URL = 'https://github.com/duyixian1234/get_version'
EMAIL = 'duyixian1234@qq.com'
AUTHOR = 'Yixian Du'

# What packages are required for this module to be executed?

REQUIRED = [
    'click',
]

here = Path(__file__).cwd()

class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')
        sys.exit()

setup(
    name=NAME,
    version='0.1.0',
    description=DESCRIPTION,
    long_description='',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    entry_points={
         'console_scripts': ['get-version=get_version.__main__:main'],
     },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
