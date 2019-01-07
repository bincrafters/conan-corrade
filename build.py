#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default
from conans import tools
import shutil


package_name = "corrade"
package_version = "2018.10"
package_download_sha256sum = "b8a81bd003a66596fdacc9c1f0751c51792be67d42fc04eaf76b766ee61d4698"
package_files = {
    "/package/conan/test_package/": "test_package/",
    "/package/conan/conanfile.py": "conanfile.py",
    "/package/conan/CMakeLists.txt": "CMakeLists.txt"
}
package_download_url = "https://github.com/Croydon/conan-corrade/archive/stable/" + package_version
extracted_dir = "conan-" + package_name + "-stable-" + package_version

# This conan file is getting maintained upstream at https://github.com/mosra/corrade
# while we are providing CI / CD
# download the release and move it accordingly to the places our scripts are expecting the files

tools.get(package_download_url, sha256=package_download_sha256sum)

for key, value in package_files.items():
    shutil.move(extracted_dir + key, value)

tools.rmdir(extracted_dir)

if __name__ == "__main__":

    builder = build_template_default.get_builder()

    builder.run()
