# Copyright 2023 by Jihong Kim, The Kyonggi Univ.
# All rights reserved.
# This file is part of the Graphic User Interface that can output custom messages,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, 
                             QSlider, QLineEdit, QPushButton, QGroupBox, QWidget, QFormLayout, 
                             QFrame, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setWindowTitle("Controller GUI")
        self.setGeometry(100, 100, 1500, 1300)

        # Set background color to white
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor('white'))
        self.setPalette(palette)

        # Main layout
        layout = QVBoxLayout()

        # Image
        pixmap = QPixmap("rodel_logo.png")
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio)
        label_image = QLabel(self)
        label_image.setPixmap(pixmap)

        # Layout for image in the top right corner
        topLayout = QHBoxLayout()
        topLayout.addStretch(1)
        topLayout.addWidget(label_image)
        layout.addLayout(topLayout)

        # Skid steering group
        self.skidSteeringGroup = QGroupBox("Slider Controller")
        skidLayout = QHBoxLayout()

        slider_names = ["Slider 1", "Slider 2", "Slider 3", "Slider 4", 
                        "Slider 5", "Slider 6", "Slider 7", "Slider 8"]

        self.sliders = []
        self.slider_values = []
        self.min_ranges = []
        self.max_ranges = []
        self.min_labels = []
        self.max_labels = []
        self.stop_buttons_slider = []
        self.zero_buttons_slider = []

        for i in range(4):
            vLayout = QVBoxLayout()
            for j in range(2):
                hLayout = QHBoxLayout()
                formLayout = QFormLayout()

                label = QLabel(slider_names[i*2 + j])
                
                slider = QSlider(Qt.Vertical)
                slider.setMinimum(-10)
                slider.setMaximum(10)
                slider.setValue(0)
                slider.setTickPosition(QSlider.TicksLeft)
                slider.setTickInterval(5)
                slider.setFixedHeight(150)
                
                slider_value = QLabel("0")
                self.slider_values.append(slider_value)

                min_range = QLineEdit(self)
                min_range.setPlaceholderText("Min Range")
                max_range = QLineEdit(self)
                max_range.setPlaceholderText("Max Range")

                min_label = QLabel("-10")
                max_label = QLabel("10")
                
                self.min_labels.append(min_label)
                self.max_labels.append(max_label)
                
                self.min_ranges.append(min_range)
                self.max_ranges.append(max_range)

                self.sliders.append(slider)

                stop_button = QPushButton("Stop")
                zero_button = QPushButton("Zero")
                self.stop_buttons_slider.append(stop_button)
                self.zero_buttons_slider.append(zero_button)

                # Slider on the left
                hLayout.addWidget(slider)
                
                # Value, Stop, and Zero on the right
                vBtnLayout = QVBoxLayout()
                vBtnLayout.addWidget(slider_value)
                vBtnLayout.addWidget(stop_button)
                vBtnLayout.addWidget(zero_button)
                hLayout.addLayout(vBtnLayout)

                formLayout.addRow(label)
                formLayout.addRow("Min:", min_range)
                formLayout.addRow("Max:", max_range)
                formLayout.addRow(max_label)
                formLayout.addRow(hLayout)
                formLayout.addRow(min_label)

                vLayout.addLayout(formLayout)
            skidLayout.addLayout(vLayout)

        self.skidSteeringGroup.setLayout(skidLayout)
        layout.addWidget(self.skidSteeringGroup)

        # Number input group
        self.numberInputGroup = QGroupBox("Enter numbers")
        numberLayout = QVBoxLayout()

        input_names = ["Number 1", "Number 2", "Number 3", "Number 4", 
                       "Number 5", "Number 6", "Number 7", "Number 8"]

        self.line_edits = []
        self.submit_buttons = []
        self.stop_buttons_number = []
        self.zero_buttons_number = []
        for i in range(2):
            hLayout = QHBoxLayout()
            for j in range(4):
                vLayout = QVBoxLayout()
                label = QLabel(input_names[i*4 + j])
                line_edit = QLineEdit(self)
                submit_button = QPushButton("Submit")
                stop_button = QPushButton("Stop")
                zero_button = QPushButton("Zero")
                
                vLayout.addWidget(label)
                vLayout.addWidget(line_edit)
                vLayout.addWidget(submit_button)
                vLayout.addWidget(stop_button)
                vLayout.addWidget(zero_button)

                self.line_edits.append(line_edit)
                self.submit_buttons.append(submit_button)
                self.stop_buttons_number.append(stop_button)
                self.zero_buttons_number.append(zero_button)

                hLayout.addLayout(vLayout)
            numberLayout.addLayout(hLayout)

        self.numberInputGroup.setLayout(numberLayout)
        layout.addWidget(self.numberInputGroup)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
