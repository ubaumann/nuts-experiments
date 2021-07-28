"""Query VRF with scrapli"""
from typing import Callable, Dict, Any, Optional, List, Set

import pytest
from nornir.core.filter import F
from nornir.core.task import MultiResult, Result
from nornir_scrapli.tasks import send_command

from nuts.helpers.filters import filter_hosts
from nuts.helpers.result import AbstractHostResultExtractor, NutsResult
from nuts.context import NornirNutsContext


class VrfExtractor(AbstractHostResultExtractor):
    def single_transform(self, single_result: MultiResult) -> Dict[str, Dict[str, Any]]:
        return single_result[0].scrapli_response.genie_parse_output()


class VrfContext(NornirNutsContext):

    id_format = "{host}_"

    def nuts_task(self) -> Callable[..., Result]:
        return send_command

    def nuts_arguments(self) -> Dict[str, Any]:
        return {"command": "show vrf"}

    def nornir_filter(self) -> F:
        tags: Set[str] = {entry["tag"] for entry in self.nuts_parameters["test_data"]}
        return F(tags__any=tags)

    def nuts_extractor(self) -> VrfExtractor:
        return VrfExtractor(self)

    def parametrize(self, test_data: Any) -> Any:
        tests = []
        for data in test_data:
            nr = self.nornir.filter(F(tags__contains=data.get("tag")))
            for host in nr.inventory.hosts.keys():
                tests.append({**data, "host": host})
        return tests


CONTEXT = VrfContext


class TestVrfs:
    @pytest.mark.nuts("vrfs")
    def test_vrfs(self, single_result, vrfs):
        device_vrfs = set(single_result.result.get("vrf"))
        assert set(vrfs).issubset(device_vrfs)
