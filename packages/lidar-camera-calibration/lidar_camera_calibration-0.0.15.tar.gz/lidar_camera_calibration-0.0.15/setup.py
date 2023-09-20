# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

from setuptools import find_packages, setup

DESCRIPTION = "LiDAR camera calibration"
LONG_DESCRIPTION = "A PyTorch LiDAR camera calibration project that maximises the mutual information between LiDAR and image intensities."
version = "v0.0.15"
if version.startswith("{{"):
    version = "0.0.0"

# Setting up
setup(
    # the name must match the folder name 'image_based_malware_dataloader'
    name="lidar_camera_calibration",
    version=version,
    author="Timothy Farnworth",
    author_email="tkfarnworth@gmail.com",
    description=DESCRIPTION,
    url="https://github.com/kiakahabro/lidar-camera-calibration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "lidar_camera_calibration = lidar_camera_calibration.__main__:main"
        ]
    },
    install_requires=[
        "matplotlib",
        "pathlib2",
        "pyqt5",
        "pyyaml",
        "scikit-learn",
        "scipy",
        "torch",
        "typer[all]",
        "rosbags",
        "natsort",
    ],
    keywords=["python", "calibration", "LiDAR", "camera"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
)
