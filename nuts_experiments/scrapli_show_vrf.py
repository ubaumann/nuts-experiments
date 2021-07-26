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
        vrfs = self._simple_extract(single_result)
        return vrfs

    def single_result(self, nuts_test_entry: Dict[str, Any]) -> NutsResult:
        tag = nuts_test_entry["tag"]

        ctx = self._nuts_ctx
        nr = ctx.nornir.filter(F(tags__contains=tag))
        hosts = nr.inventory.hosts.keys()
        return NutsResult({ host: self.transformed_result[host] for host in hosts})


class VrfContext(NornirNutsContext):
    def nuts_task(self) -> Callable[..., Result]:
        return send_command

    def nuts_arguments(self) -> Dict[str, Any]:
        return {"command": "show vrf"}

    def nornir_filter(self) -> F:
        tags: Set[str] = {entry["tag"] for entry in self.nuts_parameters["test_data"]}
        return F(tags__any=tags)

    def nuts_extractor(self) -> VrfExtractor:
        return VrfExtractor(self)


CONTEXT = VrfContext


class TestVrfs:
    @pytest.mark.nuts("vrfs")
    def test_vrfs(self, single_result, vrfs):
        # breakpoint()
        for host, result in single_result.result.items():
            result.validate()
            for vrf in vrfs:
                assert vrf in result.result, f"{host} does not have vrf {vrf}"
