============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/bin/python
cachedir: .pytest_cache
rootdir: /home/urs/projects/nuts-experiments/playground
plugins: cov-2.12.0, nuts-3.0.1
collecting ... collected 10 items

tests/test_user.yaml::TestNapalmUsers::test_username[0] PASSED           [ 10%]
tests/test_user.yaml::TestNapalmUsers::test_username[1] PASSED           [ 20%]
tests/test_user.yaml::TestNapalmUsers::test_password[0] SKIPPED (req...) [ 30%]
tests/test_user.yaml::TestNapalmUsers::test_password[1] SKIPPED (req...) [ 40%]
tests/test_user.yaml::TestNapalmUsers::test_privilege_level[0] SKIPPED   [ 50%]
tests/test_user.yaml::TestNapalmUsers::test_privilege_level[1] SKIPPED   [ 60%]
tests/test_vrf.yaml::TestVrfs::test_vrfs[R1_0] FAILED                    [ 70%]
tests/test_vrf.yaml::TestVrfs::test_vrfs[R1_1] FAILED                    [ 80%]
tests/test_vrf.yaml::TestVrfs::test_vrfs[R3_0] ERROR                     [ 90%]
tests/test_vrf.yaml::TestVrfs::test_vrfs[R3_1] ERROR                     [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of TestVrfs.test_vrfs[R3_0] __________________

nuts_ctx = <nuts_experiments.scrapli_show_vrf.VrfContext object at 0x7fb12463baf0>
nuts_test_entry = {'host': 'R3', 'tag': 'csr1knxos', 'vrfs': ['mgmt', 'test', 'test2']}

    @pytest.fixture
    def single_result(nuts_ctx: NutsContext, nuts_test_entry: Dict[str, Any]) -> NutsResult:
        """
        Returns the result which belongs to a specific host
        out of the overall set of results that has been returned by nornir's task.
        In addition, ensures that the result has no exception and has not failed.
    
        :param nuts_ctx: The context for a test
        :param nuts_test_entry: The entry from the test bundle (yaml-file) for which
            the corresponding result should be returned
        :return: The `NutsResult` that belongs to a host or host/destination pair
        """
        res = nuts_ctx.extractor.single_result(nuts_test_entry)
>       res.validate()

../../../.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nuts/plugin.py:37: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <nuts.helpers.result.NutsResult object at 0x7fb1207b76d0>

    def validate(self) -> None:
        """Make sure the underlying result is a valid (i.e. non-failed) one."""
        if self.exception:
            header = "".join(
                traceback.format_exception_only(type(self.exception), self.exception)
            )
>           raise NutsNornirError(
                f"An exception has occurred while executing nornir:\n"
                f"{header}\n"
                f"{self._result}"
            )
E           nuts.helpers.errors.NutsNornirError: An exception has occurred while executing nornir:
E           nornir_scrapli.exceptions.NornirScrapliInvalidPlatform: Provided platform `nxos_ssh` is not a valid scrapli or napalm platform, or is not a valid scrapli-community platform.
E           
E           None

../../../.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nuts/helpers/result.py:45: NutsNornirError
__________________ ERROR at setup of TestVrfs.test_vrfs[R3_1] __________________

nuts_ctx = <nuts_experiments.scrapli_show_vrf.VrfContext object at 0x7fb12463baf0>
nuts_test_entry = {'host': 'R3', 'tag': 'NXOSv', 'vrfs': ['mgmt']}

    @pytest.fixture
    def single_result(nuts_ctx: NutsContext, nuts_test_entry: Dict[str, Any]) -> NutsResult:
        """
        Returns the result which belongs to a specific host
        out of the overall set of results that has been returned by nornir's task.
        In addition, ensures that the result has no exception and has not failed.
    
        :param nuts_ctx: The context for a test
        :param nuts_test_entry: The entry from the test bundle (yaml-file) for which
            the corresponding result should be returned
        :return: The `NutsResult` that belongs to a host or host/destination pair
        """
        res = nuts_ctx.extractor.single_result(nuts_test_entry)
>       res.validate()

../../../.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nuts/plugin.py:37: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <nuts.helpers.result.NutsResult object at 0x7fb1207b76d0>

    def validate(self) -> None:
        """Make sure the underlying result is a valid (i.e. non-failed) one."""
        if self.exception:
            header = "".join(
                traceback.format_exception_only(type(self.exception), self.exception)
            )
>           raise NutsNornirError(
                f"An exception has occurred while executing nornir:\n"
                f"{header}\n"
                f"{self._result}"
            )
E           nuts.helpers.errors.NutsNornirError: An exception has occurred while executing nornir:
E           nornir_scrapli.exceptions.NornirScrapliInvalidPlatform: Provided platform `nxos_ssh` is not a valid scrapli or napalm platform, or is not a valid scrapli-community platform.
E           
E           None

../../../.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nuts/helpers/result.py:45: NutsNornirError
=================================== FAILURES ===================================
___________________________ TestVrfs.test_vrfs[R1_0] ___________________________

self = <nuts_experiments.scrapli_show_vrf.TestVrfs object at 0x7fb12469ba60>
single_result = <nuts.helpers.result.NutsResult object at 0x7fb121049100>
vrfs = ['mgmt', 'test']

    @pytest.mark.nuts("vrfs")
    def test_vrfs(self, single_result, vrfs):
        for vrf in vrfs:
>           assert vrf in single_result.result, f"does not have vrf {vrf}"
E           AssertionError: does not have vrf mgmt

../nuts_experiments/scrapli_show_vrf.py:58: AssertionError
------------------------------ Captured log setup ------------------------------
ERROR    nornir.core.task:task.py:115 Host 'R3': task 'send_command' failed with traceback:
Traceback (most recent call last):
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/scrapli/factory.py", line 158, in _get_community_platform_details
    scrapli_community_platform = importlib.import_module(
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 961, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'scrapli_community.nxos'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nornir_scrapli/connection.py", line 86, in open
    connection = Scrapli(**parameters, platform=platform)  # type: ignore
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/scrapli/factory.py", line 498, in __new__
    final_driver, additional_kwargs = cls._get_driver(platform=platform, variant=variant)
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/scrapli/factory.py", line 327, in _get_driver
    final_driver, additional_kwargs = cls._get_community_driver(
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/scrapli/factory.py", line 289, in _get_community_driver
    platform_details = _get_community_platform_details(
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/scrapli/factory.py", line 169, in _get_community_platform_details
    raise ScrapliModuleNotFound(warning) from exc
scrapli.exceptions.ScrapliModuleNotFound: 

****************************** Module not found! *******************************
Scrapli Community platform 'nxos_ssh` not found!
To resolve this issue, ensure you have the correct platform name, and that a scrapli  community platform of that name exists!
********************************************************************************


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nornir/core/task.py", line 99, in start
    r = self.task(self, **self.params)
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nornir_scrapli/tasks/send_command.py", line 36, in send_command
    scrapli_conn = task.host.get_connection("scrapli", task.nornir.config)
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nornir/core/inventory.py", line 494, in get_connection
    self.open_connection(
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nornir/core/inventory.py", line 546, in open_connection
    conn_obj.open(
  File "/home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/lib/python3.8/site-packages/nornir_scrapli/connection.py", line 88, in open
    raise NornirScrapliInvalidPlatform(
nornir_scrapli.exceptions.NornirScrapliInvalidPlatform: Provided platform `nxos_ssh` is not a valid scrapli or napalm platform, or is not a valid scrapli-community platform.
___________________________ TestVrfs.test_vrfs[R1_1] ___________________________

self = <nuts_experiments.scrapli_show_vrf.TestVrfs object at 0x7fb12074deb0>
single_result = <nuts.helpers.result.NutsResult object at 0x7fb121049100>
vrfs = ['mgmt', 'test', 'test2']

    @pytest.mark.nuts("vrfs")
    def test_vrfs(self, single_result, vrfs):
        for vrf in vrfs:
>           assert vrf in single_result.result, f"does not have vrf {vrf}"
E           AssertionError: does not have vrf mgmt

../nuts_experiments/scrapli_show_vrf.py:58: AssertionError
=========================== short test summary info ============================
FAILED tests/test_vrf.yaml::TestVrfs::test_vrfs[R1_0] - AssertionError: does ...
FAILED tests/test_vrf.yaml::TestVrfs::test_vrfs[R1_1] - AssertionError: does ...
ERROR tests/test_vrf.yaml::TestVrfs::test_vrfs[R3_0] - nuts.helpers.errors.Nu...
ERROR tests/test_vrf.yaml::TestVrfs::test_vrfs[R3_1] - nuts.helpers.errors.Nu...
============== 2 failed, 2 passed, 4 skipped, 2 errors in 25.96s ===============
