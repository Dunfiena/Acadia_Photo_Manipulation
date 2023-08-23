import os
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, \
    QGroupBox, QWidget, QGridLayout, QRadioButton, QSlider


class MainWindow(QMainWindow):

    def set_grey_low(self, x):
        self._value_low = x

    def get_grey_low(self):
        return self._value_low

    def set_grey_high(self, x):
        self._value_high = x

    def get_grey_high(self):
        return self._value_high

    def set_filename(self, x):
        self._filename = x

    def get_filename(self):
        return self._filename

    def __init__(self):
        # region setup
        super().__init__()
        self._value_low = 0
        self._value_high = 255
        self._output_dir = None
        self._filename = None
        self.title = "Photo Manipulation"
        self.setWindowIcon(QIcon("Assets/project_icon_2.png"))
        self.left = 0
        self.top = 0
        self.width = 1200
        self.height = 900
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        app.setStyleSheet('QLabel{font: 12pt; color:grey}'
                          'QRadioButton{font-size: 16pt;}'
                          'QComboBox{font-size: 12pt;}'
                          'QLineEdit{font-size: 16pt;}'
                          'QPushButton{font-size: 12pt;}'
                          'QSpinBox{font-size: 12pt;}'
                          'QDoubleSpinBox{font-size: 12pt;}'
                          'QCheckBox{font-size: 12pt;}'
                          'QGroupBox{border: 2px solid gray;border-radius: 5px;background: rgb(211, 218, 235);}'
                          'Selection-color: grey;')
        # endregion

        # region Widgets
        sub = QWidget(self)
        sub.setGeometry(self.left, self.top, self.width, self.height)
        layout = QGridLayout(self)

        logo_img = QLabel(self)
        self.logo_map = QPixmap('./Assets/logo.png')
        self.logo_resize = self.logo_map.scaled(450, 150, Qt.KeepAspectRatio)
        logo_img.setPixmap(self.logo_resize)
        logo_img.adjustSize()

        logo = QLabel('Photo Manipulation', self)
        logo.setStyleSheet('color: white;font-size: 16pt;')

        bottom_text = QLabel("Acadia Physics 2023", self)
        bottom_text.setStyleSheet('font-size: 8pt;')

        search = QPushButton('Select File', self)
        search.clicked.connect(self.input_file)
        search.setFixedSize(250, 50)

        save = QPushButton('Save', self)
        save.clicked.connect(self.save_image)
        save.setFixedSize(250, 50)

        pop_window = QPushButton('Inspect', self)
        pop_window.clicked.connect(self.pop_out)
        pop_window.setFixedSize(250, 50)

        self.photo = QLabel(self)

        # region Grey_generate
        grey_group = QGroupBox(self)
        self.Man_select_1 = QRadioButton("Grey", self)

        grey_high_label = QLabel("High Cutoff", self)
        grey_low_label = QLabel("Low Cutoff", self)

        self.grey_slider_low = QSlider(Qt.Horizontal)
        self.grey_slider_low.setGeometry(30, 40, 200, 30)
        self.grey_slider_low.setMaximum(255)
        self.grey_slider_low.setMinimum(0)
        self.grey_slider_low.setValue(0)
        self.grey_slider_low.valueChanged.connect(self.grey_change_value)
        self.grey_slider_low.setSingleStep(1)

        self.slide_value = QLabel("0", self)

        self.grey_slider_high = QSlider(Qt.Horizontal)
        self.grey_slider_high.setGeometry(30, 40, 200, 30)
        self.grey_slider_high.setMaximum(255)
        self.grey_slider_high.setMinimum(0)
        self.grey_slider_high.setValue(255)
        self.grey_slider_high.valueChanged.connect(self.grey_change_value)
        self.grey_slider_high.setSingleStep(1)

        self.slide_value2 = QLabel("255", self)

        self.grey_generate = QPushButton("Apply")
        self.grey_generate.clicked.connect(self.generate_grey)
        self.grey_generate.setFixedSize(150, 50)
        # endregion

        # region color
        color_group = QGroupBox(self)

        self.Man_select_2 = QRadioButton("Color", self)

        red_label_low = QLabel("Low Cutoff (red)", self)
        blue_label_low = QLabel("Low Cutoff (blue)", self)
        green_label_low = QLabel("Low Cutoff (green)", self)

        red_label_high = QLabel("High Cutoff (red)", self)
        blue_label_high = QLabel("High Cutoff (blue)", self)
        green_label_high = QLabel("High Cutoff (green)", self)

        self.slider_red = QSlider(Qt.Horizontal)
        self.slider_red.setGeometry(30, 40, 200, 30)
        self.slider_red.setMaximum(255)
        self.slider_red.setMinimum(0)
        self.slider_red.setValue(255)
        self.slider_red.valueChanged.connect(self.color_change_value)
        self.slider_red.setSingleStep(1)

        self.slide_value_red = QLabel("255", self)

        self.slider_red_low = QSlider(Qt.Horizontal)
        self.slider_red_low.setGeometry(30, 40, 200, 30)
        self.slider_red_low.setMaximum(255)
        self.slider_red_low.setMinimum(0)
        self.slider_red_low.setValue(0)
        self.slider_red_low.valueChanged.connect(self.color_change_value)
        self.slider_red_low.setSingleStep(1)

        self.slide_value_red_low = QLabel("0", self)

        self.slider_green = QSlider(Qt.Horizontal)
        self.slider_green.setGeometry(30, 40, 200, 30)
        self.slider_green.setMaximum(255)
        self.slider_green.setMinimum(0)
        self.slider_green.setValue(255)
        self.slider_green.valueChanged.connect(self.color_change_value)
        self.slider_green.setSingleStep(1)

        self.slide_value_green = QLabel("255", self)

        self.slider_green_low = QSlider(Qt.Horizontal)
        self.slider_green_low.setGeometry(30, 40, 200, 30)
        self.slider_green_low.setMaximum(255)
        self.slider_green_low.setMinimum(0)
        self.slider_green_low.setValue(0)
        self.slider_green_low.valueChanged.connect(self.color_change_value)
        self.slider_green_low.setSingleStep(1)

        self.slide_value_green_low = QLabel("0", self)

        self.slider_blue = QSlider(Qt.Horizontal)
        self.slider_blue.setGeometry(30, 40, 200, 30)
        self.slider_blue.setMaximum(255)
        self.slider_blue.setMinimum(0)
        self.slider_blue.setValue(255)
        self.slider_blue.valueChanged.connect(self.color_change_value)
        self.slider_blue.setSingleStep(1)

        self.slide_value_blue = QLabel("255", self)

        self.slider_blue_low = QSlider(Qt.Horizontal)
        self.slider_blue_low.setGeometry(30, 40, 200, 30)
        self.slider_blue_low.setMaximum(255)
        self.slider_blue_low.setMinimum(0)
        self.slider_blue_low.setValue(0)
        self.slider_blue_low.valueChanged.connect(self.color_change_value)
        self.slider_blue_low.setSingleStep(1)

        self.slide_value_blue_low = QLabel("0", self)

        self.color_generate = QPushButton("Apply")
        self.color_generate.clicked.connect(self.generate_color)
        self.color_generate.setFixedSize(150, 50)
        # endregion

        space = QLabel()

        layout.addWidget(space, 0, 0, 72, 0)  # left side
        layout.addWidget(space, 0, 0, 0, 96)  # top

        layout.addWidget(bottom_text, 70, 80, 2, 20)
        layout.addWidget(logo_img, 1, 0, 2, 20)
        layout.addWidget(logo, 2, 0, 2, 20)

        layout.addWidget(search, 0, 25, 2, 15)
        layout.addWidget(pop_window, 1, 25, 3, 15)
        layout.addWidget(save, 2, 25, 5, 15)

        layout.addWidget(self.photo, 2, 1, 72, 45, Qt.AlignCenter)

        layout.addWidget(grey_group, 1, 50, 15, 50)
        layout.addWidget(self.Man_select_1, 0, 52, 3, 5)
        layout.addWidget(self.slide_value, 2, 87, 1, 10)
        layout.addWidget(self.slide_value2, 3, 87, 1, 10)
        layout.addWidget(grey_high_label, 3, 52, 1, 10)
        layout.addWidget(grey_low_label, 2, 52, 1, 10)
        layout.addWidget(self.grey_generate, 0, 67, 3, 20)
        layout.addWidget(self.grey_slider_low, 2, 52, 3, 40)
        layout.addWidget(self.grey_slider_high, 4, 52, 2, 40)

        layout.addWidget(color_group, 19, 50, 40, 50)
        layout.addWidget(self.Man_select_2, 20, 52, 4, 10)

        layout.addWidget(red_label_low, 26, 52, 1, 20)
        layout.addWidget(red_label_high, 31, 52, 1, 20)
        layout.addWidget(blue_label_low, 36, 52, 1, 20)
        layout.addWidget(blue_label_high, 41, 52, 1, 20)
        layout.addWidget(green_label_low, 46, 52, 1, 20)
        layout.addWidget(green_label_high, 51, 52, 1, 20)

        layout.addWidget(self.slider_red_low, 27, 52, 2, 40)
        layout.addWidget(self.slider_red, 32, 52, 2, 40)

        layout.addWidget(self.slider_green_low, 37, 52, 2, 40)
        layout.addWidget(self.slider_green, 42, 52, 2, 40)

        layout.addWidget(self.slider_blue_low, 47, 52, 2, 40)
        layout.addWidget(self.slider_blue, 52, 52, 2, 40)

        layout.addWidget(self.slide_value_red_low, 26, 87, 1, 10)
        layout.addWidget(self.slide_value_red, 31, 87, 1, 10)

        layout.addWidget(self.slide_value_green_low, 36, 87, 1, 10)
        layout.addWidget(self.slide_value_green, 41, 87, 1, 10)

        layout.addWidget(self.slide_value_blue_low, 46, 87, 1, 10)
        layout.addWidget(self.slide_value_blue, 51, 87, 1, 10)

        layout.addWidget(self.color_generate, 21, 67, 2, 20)

        sub.setLayout(layout)
        self.show()
        # endregion

    def grey_change_value(self):
        value = self.grey_slider_high.value()
        self.slide_value2.setText(str(value))

        value = self.grey_slider_low.value()
        self.slide_value.setText(str(value))

    def color_change_value(self):
        value = self.slider_red.value()
        self.slide_value_red.setText(str(value))

        value = self.slider_green.value()
        self.slide_value_green.setText(str(value))

        value = self.slider_blue.value()
        self.slide_value_blue.setText(str(value))

        value = self.slider_blue_low.value()
        self.slide_value_blue_low.setText(str(value))

        value = self.slider_green_low.value()
        self.slide_value_green_low.setText(str(value))

        value = self.slider_red_low.value()
        self.slide_value_red_low.setText(str(value))

    def generate_grey(self):
        if self.Man_select_1.isChecked():
            if window.get_filename():
                img_grey = np.array(Image.open(window.get_filename()).convert('L'))
                print("a")
                x = self.grey_slider_high.value()
                y = self.grey_slider_low.value()
                img_grey[img_grey >= x] = 255
                img_grey[img_grey <= y] = 255
                print(img_grey)
                self.photo.clear()
                print("b")
                plt.imshow(img_grey, cmap='gray')
                plt.savefig('tmp_files/tmp_grey.png', dpi=1000)

                pixmap = QPixmap("tmp_files/tmp_grey.png")
                pixmap_resized = pixmap.scaled(650, 650, QtCore.Qt.KeepAspectRatio)
                self.photo.setPixmap(pixmap_resized)
                self.photo.adjustSize()
                plt.clf()

    def generate_color(self):
        if self.Man_select_2.isChecked():
            img = cv2.imread(window.get_filename())
            blue = img[:, :, 0]
            green = img[:, :, 1]
            red = img[:, :, 2]
            print(blue)
            x = self.slider_blue.value()
            y = self.slider_blue_low.value()
            blue[blue >= x] = 255
            blue[blue <= y] = 255

            x = self.slider_green.value()
            y = self.slider_green_low.value()
            green[green >= x] = 255
            green[green <= y] = 255

            x = self.slider_red.value()
            y = self.slider_red_low.value()
            red[red >= x] = 255
            red[red <= y] = 255

            im_dec = cv2.merge([blue, green, red])
            im_dec = np.array(im_dec)
            im_deca = im_dec.astype(int)
            print(im_deca)
            cv2.imwrite("tmp_files/tmp_color.png", im_deca)

            pixmap = QPixmap("tmp_files/tmp_color.png")
            pixmap_resized = pixmap.scaled(650, 650, QtCore.Qt.KeepAspectRatio)
            self.photo.setPixmap(pixmap_resized)
            self.photo.adjustSize()
            plt.clf()

    def input_file(self):
        plt.clf()
        self.photo.clear()
        tmp = "tmp_files/tmp.png"
        if os.path.isfile(tmp):
            os.remove(tmp)

        file_dialog = QFileDialog().getOpenFileName(self, 'Open file',
                                                    './Images_Input', "Image files (*.jpg *.tif *.png)")
        image_path = file_dialog[0]
        res = os.path.isfile(image_path)
        if res:
            window.set_filename(image_path)
            pixmap = QPixmap(image_path)
            pixmap_resized = pixmap.scaled(650, 650, QtCore.Qt.KeepAspectRatio)
            self.photo.setPixmap(pixmap_resized)
            self.photo.adjustSize()
            plt.clf()

    def save_image(self):
        print("a")

    def pop_out(self):
        print("a")

    def color(self):
        img = window.get_filename()
        pixmap = QPixmap(img)
        pixmap_resized = pixmap.scaled(650, 650, QtCore.Qt.KeepAspectRatio)
        self.photo.setPixmap(pixmap_resized)
        self.photo.adjustSize()
        plt.clf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
