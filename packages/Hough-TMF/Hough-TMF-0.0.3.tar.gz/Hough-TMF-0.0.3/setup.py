import setuptools

'''
import pandas
import os
import cv2
from skimage.transform import hough_line, hough_line_peaks
from skimage.feature import canny
import numpy as np
import scipy
from scipy.optimize import curve_fit

import torch
import torch.nn.functional as F
#ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from numpy import roll

'''
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hough-TMF",
    version="0.0.3",
    author="Hao Lv",
    author_email="lh21@apm.ac.cn",
    description="A package for template matching using Torch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)


