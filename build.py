#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default
from conans import tools
import shutil
import os


package_name = "corrade"
package_version = "2019.01"
package_download_sha256sum = "b7658467e7d2c3d83e2bc8ad902d3839d34e0fc7bbe8941e9c8d80ded6601489"
package_download_url = "https://github.com/Croydon/corrade/archive/" + package_version + ".zip"
extracted_dir = package_name + "-" + package_version

# This conan file is getting maintained upstream at https://github.com/mosra/corrade
# while we are providing CI / CD
# download the release and move it accordingly to the places our scripts are expecting the files

tools.get(package_download_url, sha256=package_download_sha256sum)

files_list = os.listdir(extracted_dir)
for files in files_list:
    if not os.path.exists("./" + files):
        shutil.move(os.path.join(extracted_dir, files), "./")
    else:
        shutil.copy(os.path.join(extracted_dir, files), "./")

tools.rmdir(extracted_dir)

if __name__ == "__main__":

    builder = build_template_default.get_builder()

    builder.run()
