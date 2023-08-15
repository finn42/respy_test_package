
# Respiration recording analysis toolbox

This library provides python functions to evaluate single belt chest expansion recordings of human adult respiration during passive tasks (standing still, sitting and listening to music, etc.) It includes functions to find and describe features of individual breaths and to evaluate important phases of the respiratory cycle.

Developed by Finn Upham 2021 

This is not suitable for the evaluation of respiration during high intensity excertions, or for non-human animals, or for respiration measurements taken with other types of sensors (flow meters, double belts).

This toolbox is written in python 3.9 with the following dependencies:
import time
import datetime as dt
import math
import numpy as np 
import pandas as pd
from scipy.signal import butter,filtfilt
from scipy import interpolate
from scipy.interpolate import interp1d

TODO add versions, format like an adult

## Installation
Add the package with pip
> pip install -i https://test.pypi.org/simple/ respy-test-package

## Example respiration analysis

Find demo application this github account Finn42
should be up soon


