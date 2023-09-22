import json
from typing import Optional, List
from .calib import DEFAULT_CALIB

try:
    from bliss import setup_globals
except ImportError:
    setup_globals = None

from ..xrpd.processor import XrpdProcessor
from ..persistent import ParameterInfo


class DemoXrpdProcessor(
    XrpdProcessor,
    parameters=[
        ParameterInfo("config_filename", category="PyFai"),
        ParameterInfo("integration_options", category="PyFai"),
    ],
):
    def __init__(self, **defaults) -> None:
        defaults.setdefault("lima_names", ["difflab6"])
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

    def get_integrate_inputs(
        self, scan, lima_name: str, task_identifier: str
    ) -> List[dict]:
        self._ensure_config_filename()
        inputs = super().get_integrate_inputs(scan, lima_name, task_identifier)
        inputs.append(
            {"task_identifier": task_identifier, "name": "demo", "value": True}
        )
        return inputs

    def _ensure_config_filename(self):
        if self.config_filename:
            return
        cfgfile = "/tmp/test.json"
        poni = DEFAULT_CALIB
        with open(cfgfile, "w") as f:
            json.dump(poni, f)
        self.config_filename = cfgfile

    def get_config_filename(self, lima_name: str) -> Optional[str]:
        return self.config_filename

    def get_integration_options(self, lima_name: str) -> Optional[dict]:
        return self.integration_options.to_dict()


if setup_globals is None:
    xrpd_processor = None
else:
    try:
        xrpd_processor = DemoXrpdProcessor()
    except ImportError:
        xrpd_processor = None
