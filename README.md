# README for Face Detection in Video Script

## Overview

This Python script uses Dlib's face detection capabilities to analyze a video file, detect faces in key frames, and save these faces as separate image files in a specified output folder. It's designed to be user-friendly, even for those not familiar with GitHub or Python programming.

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

1. **Python**: The script is written in Python, so you need Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. **Required Libraries**:
    - **Dlib**: A toolkit for making real world machine learning and data analysis applications in C++ and Python. 
    - **OpenCV (cv2)**: An open source computer vision and machine learning software library.
    - **NumPy**: A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices.
    - **tqdm**: A library for adding progress meters to Python loops.

   You can install these libraries using pip (Python's package installer). Run the following command in your terminal or command prompt:

   ```bash
   pip install dlib opencv-python numpy tqdm
   ```

## Installation

1. **Download the Script**: 
   If you're not familiar with GitHub, simply download the script file directly from the GitHub repository. Look for a button or link named 'Download' or 'Clone' and choose the option to download the file.

2. **Save the Script**: 
   Save the script on your computer in a location where you can easily access it, like your desktop or a specific folder dedicated to scripts or projects.

## Running the Script

1. **Open Command Line**:
   - On Windows, press `Win + R`, type `cmd`, and press Enter.
   - On MacOS, open the Terminal app.
   - On Linux, open your preferred terminal emulator.

2. **Navigate to the Script Location**:
   Use the `cd` command to navigate to the directory where you saved the script. For example, if you saved it on the desktop, you would use:

   ```bash
   cd Desktop
   ```

3. **Run the Script**:
   Type `python script_name.py` in the terminal, replacing `script_name.py` with the actual name of the script file.

## Usage

When you run the script, it will ask for two inputs:

1. **Video File Path**: Enter the full path to the video file you want to process. Ensure there are no quote marks around the path.

2. **Output Folder Path**: Enter the path to the folder where you want to save the extracted face images. If the folder does not exist, the script will create it.

## Troubleshooting

If you encounter any errors:

- Make sure all required libraries are installed.
- Check the video file path and output folder path for accuracy.
- Ensure Python is correctly installed on your system.

