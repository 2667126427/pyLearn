import os
import pip

installed = pip.get_installed_distributions()
packages = []
for install in installed:
    packages.append(str(install).split()[0])

update = "pip install --upgrade {0}"
# os.system(update.format(packages[0]))
for package in packages:
    print("updating " + package)
    os.system(update.format(package))
