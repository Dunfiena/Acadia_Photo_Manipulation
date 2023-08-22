import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import skimage
from PIL import Image
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QFileDialog, \
    QSpinBox, QCheckBox, QGroupBox, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QToolButton, QProgressBar, \
    QPlainTextEdit, QDoubleSpinBox, QLineEdit, QRadioButton, QSlider
from matplotlib import image as mpimg
from skimage import color
from PIL import Image

img_grey = np.array(Image.open("Images_Input/Flower.JPG").convert('L'))
print("a")
a = 0
print(img_grey)

img_grey[img_grey > 230] = 0
img_grey[img_grey < 50] = 0
print("b")
print(img_grey)
plt.imshow(img_grey)
plt.pause(100)
