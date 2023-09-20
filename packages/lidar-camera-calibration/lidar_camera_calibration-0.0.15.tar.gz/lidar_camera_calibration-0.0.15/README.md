# lidar-camera-calibration

[TOC]

## Summary

A PyTorch LiDAR camera calibration project that maximises the mutual information between LiDAR and image intensities.

## Installation

```bash
pip install lidar_camera_calibration
```

## Usage

The `lidar_camera_calibration` package expects a path to be passed that contains the directory with the calibration data. For a calibration dataset, the following directory structure is expected:

```bash
.
├── raw
│   ├── camera_config.yaml # Camera configuration file
│   ├── camera_params.yaml # Initial camera parameters
│   ├── calibrationBagFile-0.bag  # Works with single bag too
│   ├── ...
│   └── calibrationBagFile-K.bag
├── compressed # automatically generated
│   ├── frame-000.mat
│   ├── ...
│   └── frame-NNN.mat
└── results # automatically generated
    ├── calibration_joint_euler_<nepochs>.mat
    ├── calibration_joint_euler_<nepochs>.yaml
    └── camera_params_<nepochs>.yaml
```
