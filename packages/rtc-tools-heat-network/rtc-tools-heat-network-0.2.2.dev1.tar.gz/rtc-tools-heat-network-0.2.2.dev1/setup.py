"""Heat network models for RTC-Tools 2.

Includes Modelica models and their accompanying Mixins for heat networks.
"""
import sys
from pathlib import Path

from setuptools import find_packages, setup

import versioneer

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

DOCLINES = __doc__.split("\n")

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Intended Audience :: Information Technology
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
Programming Language :: Other
Topic :: Scientific/Engineering :: GIS
Topic :: Scientific/Engineering :: Mathematics
Topic :: Scientific/Engineering :: Physics
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

if sys.version_info < (3, 8):
    sys.exit(f"Sorry, Python 3.8 to 3.10 is required. You are using {sys.version_info}")

if sys.version_info > (3, 11):
    sys.exit(f"Sorry, Python 3.8 to 3.10 is required. You are using {sys.version_info}")

setup(
    name="rtc-tools-heat-network",
    version=versioneer.get_version(),
    description=DOCLINES[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[_f for _f in CLASSIFIERS.split("\n") if _f],
    url="https://github.com/Nieuwe-Warmte-Nu/rtc-tools-heat-network",
    author="Jim Rojer",
    author_email="jim.rojer@tno.nl",
    maintainer="Jim Rojer, Kobus van Rooyen, Kelbij Star, "
    "Femke Janssen, Jesús Andrés Rodríguez Sarasty, "
    "Thijs van der Klauw",
    license="LGPLv3",
    keywords="heat network optimization rtc tools",
    platforms=["Windows", "Linux", "Mac OS-X", "Unix"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "influxdb >= 5.3.1",
        "pyecore",
        "pymoca >= 0.9.0",
        "rtc-tools >= 2.5.0, < 2.6.0",
        "pyesdl >= 21.11.0",
        "pandas >= 1.3.1, < 2.0",
    ],
    tests_require=["pytest", "pytest-runner", "numpy"],
    include_package_data=True,
    python_requires=">=3.8,<3.11",
    cmdclass=versioneer.get_cmdclass(),
    entry_points={
        "rtctools.libraries.modelica": ["library_folder = rtctools_heat_network:modelica"]
    },
)
