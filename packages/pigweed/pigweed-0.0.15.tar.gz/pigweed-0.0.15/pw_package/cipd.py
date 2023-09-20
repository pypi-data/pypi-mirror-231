# Copyright 2020 The Pigweed Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Install and check status of teensy-core."""

def populate_download_cache_from_cipd(
    path: Path,
    download_path: Path,
    cipd_package_subpath: str,
) -> None:
    """Check for CIPD package availability."""
    package_path = path.parent.resolve()
    core_name = self.name
    core_cache_path = package_path / ".cache" / core_name
    core_cache_path.mkdir(parents=True, exist_ok=True)

    cipd_package_subpath = "pigweed_internal/third_party/"
    cipd_package_subpath += core_name
    cipd_package_subpath += "/${platform}"

    with tempfile.NamedTemporaryFile(
        prefix='cipd', delete=True, dir=core_cache_path
    ) as temp_json:
        temp_json_path = Path(temp_json.name)
        cipd_acl_check_command = [
            "cipd",
            "acl-check",
            cipd_package_subpath,
            "-reader",
            "-json-output",
            str(temp_json_path),
        ]
        subprocess.run(cipd_acl_check_command, capture_output=True)
        # Return if no packages are readable.
        if not temp_json_path.is_file():
            return
        result_text = temp_json.read_text()
        result_dict = json.loads(result_text)
        if 'result' not in result_dict:
            return
