# IPD Calculator

A Python project to calculate Interpupillary Distance (IPD) using OpenCV, NumPy, and dlib libraries. This tool allows you to measure the IPD of a user either from a live camera feed or from an image.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Interpupillary Distance (IPD) is an important measurement for various applications, such as virtual reality and human-computer interaction. This project offers a Python-based solution to calculate IPD from a user's eyes.

## Features

- Calculate IPD from live camera feed.
- Measure IPD from an image.
- Utilizes OpenCV for image processing.
- Uses dlib for face detection and facial landmarks detection
- Uses NumPy for mathematical operations.
  

## Prerequisites

Before using this project, you need to have the following dependencies installed:

- Python 3.x
- OpenCV
- NumPy
- dlib
- The facial landmarks model file (landmarks.dat) for dlib (Download and place it in the project directory).

## Getting Started

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sammigul/IPD-Measurement-.git
   cd IPD-Measurement-
   
2. Install required python libraries using pip:
   ```bash
   pip install opencv-python numpy dlib
   
3. Download the facial landmarks model (landmarks.dat) from the dlib website and place it in the project directory.

## Usage

To calculate the IPD from a live camera feed, 
uncomment the live_image_analysis method call in the main.py file, similarly you can call the image_analysis method in the main.py folder
but make sure that the image path, aruco Marker size and aruco dictionary are provided in the arguments. 

## Contributing

Contributions are welcome! If you have any ideas for improvement or new features, please submit a pull request or open an issue.

## Acknowledgments

Thanks to the dlib community for providing the facial landmarks model.

## Contact

For questions or support, you can reach out to Abdul Sammi Gul at [gulsammi20@gmail.com].

