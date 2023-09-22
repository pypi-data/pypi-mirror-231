from pprint import pprint
from typing import List
from .calib import DEFAULT_CALIB
import json

try:
    from bliss import setup_globals
except ImportError:
    setup_globals = None
from ..id22.stscan_processor import StScanProcessor
from ..id22.xrpd_processor import Id22XrpdProcessor


class DemoStScanProcessor(StScanProcessor):
    def __init__(self) -> None:
        super().__init__(
            convert_workflow="/tmp/demo/convert.json",
            rebinsum_workflow="/tmp/demo/rebinsum.json",
            extract_workflow="/tmp/demo/extract.json",
        )

    def _submit_job(self, workflow, inputs, **kw):
        print("\nSubmit workfow")
        print(workflow)
        print("Inputs:")
        pprint(inputs)
        print("Options:")
        pprint(kw)


class DemoId22XrpdProcessor(Id22XrpdProcessor):
    def __init__(self, **defaults) -> None:
        defaults.setdefault("lima_names", ["perkinelmer"])
        defaults.setdefault(
            "integration_options",
            {
                "method": "no_csr_cython",
                "nbpt_rad": 4096,
                "radial_range_min": 1,
                "unit": "q_nm^-1",
            },
        )
        super().__init__(**defaults)
        self._ensure_config_filename()

    def get_integrate_1d_inputs(self, scan, lima_name: str) -> List[dict]:
        inputs = super().get_integrate_1d_inputs(scan, lima_name)
        inputs.append({"task_identifier": "Integrate1D", "name": "demo", "value": True})
        return inputs

    def _ensure_config_filename(self):
        if self.pyfai_config:
            return
        cfgfile = "/tmp/test.json"
        poni = DEFAULT_CALIB
        with open(cfgfile, "w") as f:
            json.dump(poni, f)
        self.pyfai_config = cfgfile


if setup_globals is None:
    stscan_processor = None
    xrpd_processor = None
else:
    stscan_processor = DemoStScanProcessor()
    xrpd_processor = DemoId22XrpdProcessor()
