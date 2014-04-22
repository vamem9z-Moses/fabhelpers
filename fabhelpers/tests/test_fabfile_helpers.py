import os
import types

from fabhelpers.fabfile import taskhelp, mod_test

FABHELPERS_PATH = os.path.split(os.path.dirname(__file__))[0]

def test_get_docstring_for_function_in_fabfile():
    """
     Test that taskhelp can produce doc string for a function in a fabfile
    """
    out = taskhelp('level_one_fab_test', base_module_name='fabhelpers.test_fixtures.fabfile')
    assert out == 'Level One Test'

def test_get_docstring_for_function_in_fabfile_submodule():
    """
     Test that taskhelp can produce a doc string for a function in fabfile submodule
    """
    out = taskhelp('level_two_fab_test', base_module_name='fabhelpers.test_fixtures.fabfile.deploy')
    assert out == 'Level Two Test'


def test_mod_test_runs_tests_if_module_exists():
    """
     Test that mod_test runs when module exists
    """
    result = mod_test(os.path.join(FABHELPERS_PATH, "test_fixtures"), "fabfile")
    assert result is None

def test_mod_test_returns_string_if_module_does_not_exist():
    """
     Test that mod_test doesn't run when module exists
    """
    result = mod_test(os.path.join(FABHELPERS_PATH, "test_fixtures"), "wrong")
    assert result == "The tests at {path} do not appear to exist.".format(path=os.path.join(FABHELPERS_PATH, "test_fixtures", "wrong"))

def test_mod_test_runs_when_module_is_not_in_a_package():
    """
     Test that mod_test runs if module passed in not a package
    """
    result = mod_test(os.path.join(FABHELPERS_PATH, "test_fixtures", "fabfile"), "deploy")
    assert result is None

def test_mod_test_runs_when_module_is_in_a_package():
    """
     Test that mod_test runs if module passed in not a package
    """
    result = mod_test(os.path.join(FABHELPERS_PATH, "test_fixtures"), "fabfile")
    assert result is None