# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.maas import maas_service
from openstack import resource2 as resource


class Version(resource.Resource):

    resouces_key = "versions"
    base_path = '/objectstorage/version'
    service = maas_service.MaaSService()

    # capabilities
    allow_list = True

    # Properties
    links = resource.Body('links')
    version = resource.Body('version')
    status = resource.Body('current')
    updated = resource.Body('updated')
