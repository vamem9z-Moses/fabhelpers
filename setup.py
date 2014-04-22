from setuptools import setup, find_packages, Command

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name = "fabhelpers",
    version = "0.1",
    description = "Helpers for Fabric",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir = {"":"."},
    package_data ={},license = 'MIT',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
    ],

    install_requires = [
        'fabric',
    ],
    tests_require=['pytest'],
    test_suite="fabhelpers.tests"
)