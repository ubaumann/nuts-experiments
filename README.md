```bash
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /home/urs/.cache/pypoetry/virtualenvs/nuts-experiments-daYRvPSx-py3.8/bin/python
cachedir: .pytest_cache
rootdir: /home/urs/projects/nuts-experiments/playground
plugins: cov-2.12.0, nuts-3.0.1
collecting ... collected 4 items

tests/test_vrf.yaml::TestVrfs::test_vrfs[R1_0] PASSED                    [ 25%]
tests/test_vrf.yaml::TestVrfs::test_vrfs[R1_1] FAILED                    [ 50%]
tests/test_vrf.yaml::TestVrfs::test_vrfs[R3_0] FAILED                    [ 75%]
tests/test_vrf.yaml::TestVrfs::test_vrfs[R3_1] FAILED                    [100%]

=================================== FAILURES ===================================
___________________________ TestVrfs.test_vrfs[R1_1] ___________________________

self = <nuts_experiments.scrapli_show_vrf.TestVrfs object at 0x7f4694c204f0>
single_result = <nuts.helpers.result.NutsResult object at 0x7f4684174f70>
vrfs = ['mgmt', 'test', 'test2']

    @pytest.mark.nuts("vrfs")
    def test_vrfs(self, single_result, vrfs):
        device_vrfs = set(single_result.result.get("vrf", {}))
>       assert set(vrfs).issubset(device_vrfs)
E       AssertionError

device_vrfs = {'mgmt', 'test'}
self       = <nuts_experiments.scrapli_show_vrf.TestVrfs object at 0x7f4694c204f0>
single_result = <nuts.helpers.result.NutsResult object at 0x7f4684174f70>
vrfs       = ['mgmt', 'test', 'test2']

../nuts_experiments/scrapli_show_vrf.py:51: AssertionError
___________________________ TestVrfs.test_vrfs[R3_0] ___________________________

self = <nuts_experiments.scrapli_show_vrf.TestVrfs object at 0x7f46524ee280>
single_result = <nuts.helpers.result.NutsResult object at 0x7f46841712b0>
vrfs = ['mgmt', 'test', 'test2']

    @pytest.mark.nuts("vrfs")
    def test_vrfs(self, single_result, vrfs):
        device_vrfs = set(single_result.result.get("vrf", {}))
>       assert set(vrfs).issubset(device_vrfs)
E       AssertionError

device_vrfs = set()
self       = <nuts_experiments.scrapli_show_vrf.TestVrfs object at 0x7f46524ee280>
single_result = <nuts.helpers.result.NutsResult object at 0x7f46841712b0>
vrfs       = ['mgmt', 'test', 'test2']

../nuts_experiments/scrapli_show_vrf.py:51: AssertionError
___________________________ TestVrfs.test_vrfs[R3_1] ___________________________

self = <nuts_experiments.scrapli_show_vrf.TestVrfs object at 0x7f4652413100>
single_result = <nuts.helpers.result.NutsResult object at 0x7f46841712b0>
vrfs = ['mgmt']

    @pytest.mark.nuts("vrfs")
    def test_vrfs(self, single_result, vrfs):
        device_vrfs = set(single_result.result.get("vrf", {}))
>       assert set(vrfs).issubset(device_vrfs)
E       AssertionError

device_vrfs = set()
self       = <nuts_experiments.scrapli_show_vrf.TestVrfs object at 0x7f4652413100>
single_result = <nuts.helpers.result.NutsResult object at 0x7f46841712b0>
vrfs       = ['mgmt']

../nuts_experiments/scrapli_show_vrf.py:51: AssertionError
=========================== short test summary info ============================
FAILED tests/test_vrf.yaml::TestVrfs::test_vrfs[R1_1] - AssertionError
FAILED tests/test_vrf.yaml::TestVrfs::test_vrfs[R3_0] - AssertionError
FAILED tests/test_vrf.yaml::TestVrfs::test_vrfs[R3_1] - AssertionError
========================= 3 failed, 1 passed in 7.65s ==========================
```