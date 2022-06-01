# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test suite for code."""
from http import HTTPStatus
from urllib.parse import urljoin


API_BASE_URL = '/api/v1/'


def test_get_code_by_type(client, jwt, access_token):
    """Test get code by type."""
    url = urljoin(API_BASE_URL, 'codes/work_types')
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        "content-type": "application/json",
    }
    print('*' * 100)
    print(f'HEADERS:: {headers}')
    print('*' * 100)
    result = client.get(url, headers=headers)
    print(result.json)
    assert result.status_code == HTTPStatus.OK


# def test_get_code_by_type_and_code(client):
#     """Test get code by type and code."""
#     url = urljoin(API_BASE_URL, 'codes/work_types/1')
#     result = client.get(url)
#     assert result.status_code == HTTPStatus.OK
