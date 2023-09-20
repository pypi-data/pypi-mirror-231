"""
How this works.

In the tests fodler, the test_perturbo.py script runs Perturbo for
a given 'test_name'. The idea is to use the same function (test_perturbo())
to run all of the calc. modes, epr files, etc. All of this should be
happening under the pytest environment (ran by `pytest`).

In this file (conftest.py), we parametrize pytest to make this work.
"""

from perturbopy.test_utils.run_test.run_utils import get_all_tests
from perturbopy.test_utils.run_test.run_utils import filter_tests
from perturbopy.test_utils.run_test.test_driver import clean_epr_folders
import pytest
import os

# define all supplementary arguments for the test running. This function declared in the PyTest itself


def pytest_addoption(parser):

    parser.addoption('--source_folder',
                     help='address of the folder with all reference files for the test performance',
                     nargs="?",
                     default='./')

    parser.addoption('--tags',
                     help='List of tests tags to include in this testsuite run.',
                     nargs='*', default=None)

    parser.addoption('--exclude-tags',
                     help='List of tests tags to exclude from this testsuite run.',
                     nargs='*', default=None)
                     
    parser.addoption('--epr_tags',
                     help='List of epr_tags to include in this testsuite run.',
                     nargs='*', default=None)

    parser.addoption('--exclude-epr_tags',
                     help='List of epr_tags to exclude from this testsuite run.',
                     nargs='*', default=None)

    parser.addoption('--epr',
                     help='List of epr files to test.',
                     nargs='*', default=None)

    parser.addoption('--test-names',
                     help='List of test names to include in this testsuite run.',
                     nargs='*', default=None)

    parser.addoption('--run_qe2pert',
                     help='Include the qe2pert tests',
                     action='store_true')
                     
    parser.addoption('--config_machine',
                     help='Name of file with computational information for qe2pert computation. Should be in the folder tests_f90/comp_qe2pert',
                     nargs="?", default='config_machine.yml')
                     
    parser.addoption('--keep_perturbo',
                     help='Save all the materials related to perturbo tests',
                     action='store_true')
                     
    parser.addoption('--keep_epr',
                     help='Save all epr-files from the qe2pert testing',
                     action='store_true')
                     
    parser.addoption('--keep_preliminary',
                     help='Save all preliminary files for epr files calculations',
                     action='store_true')

# generation of test for each type of test function. This function automatically called,
# when we run tests from the subfolders of folder, where this function is saved.


def pytest_generate_tests(metafunc):
    """
    The purpose of this function is to feed multiple test names to the
    tests/test_perturbo.py test_perturbo(test_name) function.
    Here, this function is referred as 'metafunc'.

    First, we get the list of all of the test folders using the tests/epr_info.yml file.
    We retrieve the test folder as <epr name>-<test name>. This is done by the get_all_tests()
    function.

    Next, we remove some of the tests based on the command line options and obtain the target
    test_list using the filer_tests() function.

    Finally, we feed the elements of the test_list to the test_perturbo() (metafunction)
    as the test_name input argument of the function.
    """
    if 'test_name' in metafunc.fixturenames:
        
        # define folder with supplementary information
        source_folder = os.path.abspath(metafunc.config.getoption('source_folder'))
        
        if not os.path.exists((os.path.join(source_folder, f'config_machine/{metafunc.config.getoption("config_machine")}'))):
            raise FileNotFoundError(f"File {metafunc.config.getoption('config_machine')} not found in the {source_folder}/config_machine folder. "
                                    f"Please create this file. In the folder {source_folder}/config_machine you can find examples of configurational files. "
                                    "Make your own copy with the name config_machine.yml in the same folder and run the testsuite again.")

        # Get the list of all test folders
        all_test_list, all_dev_test_list = get_all_tests(metafunc.function.__name__, source_folder)

        if (metafunc.function.__name__ == 'test_perturbo') or (metafunc.function.__name__ == 'test_perturbo_for_qe2pert'):
            # sort out test folders based on command-line options (if present)
            test_list = filter_tests(
                all_test_list,
                metafunc.config.getoption('tags'),
                metafunc.config.getoption('exclude_tags'),
                metafunc.config.getoption('epr'),
                metafunc.config.getoption('test_names'),
                metafunc.function.__name__,
                metafunc.config.getoption('run_qe2pert'),
                source_folder
            )
        elif (metafunc.function.__name__ == 'test_qe2pert'):
            test_list = filter_tests(
                all_test_list,
                metafunc.config.getoption('epr_tags'),
                metafunc.config.getoption('exclude_epr_tags'),
                metafunc.config.getoption('epr'),
                None,
                metafunc.function.__name__,
                metafunc.config.getoption('run_qe2pert'),
                source_folder
            )
        
        if metafunc.function.__name__ == 'test_perturbo_for_qe2pert':
            metafunc.parametrize('test_name', test_list, indirect=True)
            metafunc.parametrize('config_machine', [metafunc.config.getoption('config_machine')], indirect=True)
            metafunc.parametrize('keep_perturbo', [metafunc.config.getoption('keep_perturbo')], indirect=True)
            metafunc.parametrize('run_qe2pert', [metafunc.config.getoption('run_qe2pert')], indirect=True)
            metafunc.parametrize('source_folder', [source_folder], indirect=True)
        elif metafunc.function.__name__ == 'test_qe2pert':
            metafunc.parametrize('test_name', test_list, indirect=True)
            metafunc.parametrize('run_qe2pert', [metafunc.config.getoption('run_qe2pert')], indirect=True)
            metafunc.parametrize('config_machine', [metafunc.config.getoption('config_machine')], indirect=True)
            metafunc.parametrize('source_folder', [source_folder], indirect=True)
        elif metafunc.function.__name__ == 'test_perturbo':
            metafunc.parametrize('test_name', test_list, indirect=True)
            metafunc.parametrize('config_machine', [metafunc.config.getoption('config_machine')], indirect=True)
            metafunc.parametrize('keep_perturbo', [metafunc.config.getoption('keep_perturbo')], indirect=True)
            metafunc.parametrize('source_folder', [source_folder], indirect=True)
        
# in order to properly run pytest functions, we need to declare fixtures,
# which allow us to use parametrization of test functions


@pytest.fixture
def test_name(request):
    return request.param
    

@pytest.fixture
def run_qe2pert(request):
    return request.param


@pytest.fixture
def config_machine(request):
    return request.param
    

@pytest.fixture
def keep_perturbo(request):
    return request.param


@pytest.fixture
def source_folder(request):
    return request.param


# Global variable to store the number of failed tests
FAILED_TESTS_COUNT = 0

def pytest_report_teststatus(report):
    global FAILED_TESTS_COUNT
    if report.when == "call" and report.failed:
        FAILED_TESTS_COUNT += 1
    return None  # Let pytest handle the default behavior

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # Access the summary sections
    short_summary = terminalreporter.stats.get('failed', [])
    passed_summary = terminalreporter.stats.get('passed', [])
    skipped_summary = terminalreporter.stats.get('skipped', [])

    # Capture the total counts
    total_failed = len(short_summary)
    total_passed = len(passed_summary)
    total_skipped = len(skipped_summary)

    # Calculate the test session's total duration
    start_time = terminalreporter._session._inicheck_timestamp
    stop_time = terminalreporter._session._stop_timestamp
    total_duration = stop_time - start_time

    # If there are no failed tests, just return without making any modifications.
    if not short_summary:
        terminalreporter.write_sep("=", f"{total_passed} passed, {total_skipped} skipped in {total_duration:.2f}s")
        return

    # Construct the summary line
    summary_line = f"{total_failed} failed, {total_passed} passed, {total_skipped} skipped in {total_duration:.2f}s"
    terminalreporter.write_sep("=", summary_line)
















