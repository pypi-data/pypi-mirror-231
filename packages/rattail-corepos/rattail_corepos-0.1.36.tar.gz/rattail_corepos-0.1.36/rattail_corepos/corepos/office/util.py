# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2023 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
CORE Office utility logic
"""

import json
import os
import subprocess

from rattail.files import resource_path


def get_fannie_config_value(config, name):
    """
    Retrieve a config value from `fannie/config.php`

    :param config: Rattail config object.

    :param name: Name of the config value to be returned.  This need
       not be prefixed with ``FANNIE_`` although it can be.

    :returns: Config value as Python object, e.g. a string or dict.
       This is believed to work okay but since the Fannie config file
       represents data with PHP code, which is then converted to JSON
       and finally to Python, some discrepancies may be possible.
    """
    if not name.startswith('FANNIE_'):
        name = f'FANNIE_{name}'

    is4c = config.require('corepos', 'srcdir')
    path = os.path.join(is4c, 'fannie', 'config.php')
    script = resource_path('rattail_corepos.corepos.office:scripts/parse-fannie-config.php')

    try:
        output = subprocess.check_output(['php', script,
                                          '--path', path,
                                          '--setting', name])
    except subprocess.CalledProcessError as error:
        raise ValueError(f"failed to read value: {error.output.decode('utf_8')}")

    return json.loads(output.decode('utf_8'))
