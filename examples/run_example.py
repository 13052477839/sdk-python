# Copyright 2017 HuaWei Tld
# Copyright 2017 OpenStack.org
#
# Licensed under the Apache License, Version 2.0 (the 'License'); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging
import os
from examples.cloud_eye import alarms
from examples.cloud_eye import metric_data
from examples.cloud_eye import metrics
from examples.cloud_eye import quotas

from examples.connect import create_connection_from_config

# utils.enable_logging(debug=False, stream=sys.stdout)
from openstack import connection
from openstack import profile

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
root_log = logging.getLogger()
root_log.setLevel(logging.DEBUG)
requests_log = logging.getLogger('requests.packages.urllib3')
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# setup endpoint overrides
os.environ.setdefault(
    'OS_CLOUD_EYE_ENDPOINT_OVERRIDE',
    'https://ces.eu-de.otc.t-systems.com/V1.0/%(project_id)s'
)

# initial connection
# conn = create_connection_from_config()
conn = connection.Connection(auth_url="https://iam.eu-de.otc.t-systems.com/v3",
                             project_id="d4f2557d248e4860829f5fef030b209c",
                             user_domain_id="bb42e2cd2b784ac4bdc350fb660a2bdb",
                             username="replace-with-your-username",
                             password="hw@otc2017")

zones = conn.dns.zones(limit=20)
for zone in zones:
    print zone

# Cloud Eye Examples
# metrics.list_metrics(conn)
# metrics.list_favorite_metrics(connection)

# alarms.list_alarms(connection)
# alarms.enable_alarm(connection)
# alarms.get_alarm(connection)
# alarms.disable_alarm(connection)

# metric_data.list_metric_aggregations(connection)
# metric_data.add_metric_data(connection)

# quotas.list_quotas(connection)
