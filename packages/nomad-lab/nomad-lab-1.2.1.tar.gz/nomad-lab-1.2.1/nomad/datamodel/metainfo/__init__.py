#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import importlib
from pydantic import parse_obj_as

from nomad import config
from nomad.config import Schema, Plugin

from . import annotations  # Should be imported first to register the annotations before they are used
from .simulation import m_env
from .eln.perovskite_solar_cell_database import m_package
from .downloads import m_package
from .eln.labfolder import m_package

for plugin in config.plugins.filtered_values():
    if isinstance(plugin, Schema):
        importlib.import_module(plugin.python_package)
