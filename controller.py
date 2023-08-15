# Copyright 2023 by Jihong Kim, The Kyonggi Univ.
# All rights reserved.
# This file is part of the Graphic User Interface that can output custom messages,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from main_window import MainWindow

class Controller(Node, MainWindow):
    def __init__(self):
        # ROS2 node initialization
        rclpy.init()
        Node.__init__(self, 'gui_controller')
        MainWindow.__init__(self)

       # ROS2 publisher
       # Allow for the replacement of another topic message here
        self.publisher0 = self.create_publisher(JointState, 'joint_states1', 10)
        self.publisher1 = self.create_publisher(JointState, 'joint_states2', 10)
        self.publisher2 = self.create_publisher(JointState, 'joint_states3', 10)
        self.publisher3 = self.create_publisher(JointState, 'joint_states4', 10)
        self.publisher4 = self.create_publisher(JointState, 'joint_states5', 10)
        self.publisher5 = self.create_publisher(JointState, 'joint_states6', 10)
        self.publisher6 = self.create_publisher(JointState, 'joint_states7', 10)
        self.publisher7 = self.create_publisher(JointState, 'joint_states8', 10)

        # Active sliders and numbers lists
        self.active_sliders = [False] * len(self.sliders)
        self.active_numbers = [False] * len(self.line_edits)

        # Connect sliders to corresponding functions
        # Whenever the slider value shifts, all related values are determined independently
        self.sliders[0].valueChanged.connect(self.slider1_value_changed)
        self.sliders[1].valueChanged.connect(self.slider2_value_changed)
        self.sliders[2].valueChanged.connect(self.slider3_value_changed)
        self.sliders[3].valueChanged.connect(self.slider4_value_changed)
        self.sliders[4].valueChanged.connect(self.slider5_value_changed)
        self.sliders[5].valueChanged.connect(self.slider6_value_changed)
        self.sliders[6].valueChanged.connect(self.slider7_value_changed)
        self.sliders[7].valueChanged.connect(self.slider8_value_changed)
            
        # Connect range inputs to corresponding functions
        for i in range(len(self.min_ranges)):
            self.min_ranges[i].editingFinished.connect(self.create_set_min_func(i))
            self.max_ranges[i].editingFinished.connect(self.create_set_max_func(i))
            
        # Connect number inputs to corresponding functions
        for i, submit_button in enumerate(self.submit_buttons):
            submit_button.clicked.connect(self.create_number_func(i))

        # Connect stop and zero buttons for sliders
        for i in range(len(self.stop_buttons_slider)):
            self.stop_buttons_slider[i].clicked.connect(self.create_stop_slider_func(i))
            self.zero_buttons_slider[i].clicked.connect(self.create_zero_slider_func(i))
        
        # Connect stop and zero buttons for numbers
        for i in range(len(self.stop_buttons_number)):
            self.stop_buttons_number[i].clicked.connect(self.create_stop_number_func(i))
            self.zero_buttons_number[i].clicked.connect(self.create_zero_number_func(i))

        ''' 
        Timer for (n)Hz update
        
        self.timer.start(10) sets the timer to trigger the connected slot
        This method is being called every 10 milliseconds
        
        1000/10 = 100(Hz)
        '''
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(10)



    def slider1_value_changed(self):
        self.active_sliders[0] = True

    def slider2_value_changed(self):
        self.active_sliders[1] = True
    
    def slider3_value_changed(self):
        self.active_sliders[2] = True

    def slider4_value_changed(self):
        self.active_sliders[3] = True

    def slider5_value_changed(self):
        self.active_sliders[4] = True

    def slider6_value_changed(self):
        self.active_sliders[5] = True

    def slider7_value_changed(self):
        self.active_sliders[6] = True

    def slider8_value_changed(self):
        self.active_sliders[7] = True


    def create_set_min_func(self, i):
        def func():
            try:
                val = int(self.min_ranges[i].text())
                self.sliders[i].setMinimum(val)
                self.min_labels[i].setText(str(val))
            except ValueError:
                pass
        return func

    def create_set_max_func(self, i):
        def func():
            try:
                val = int(self.max_ranges[i].text())
                self.sliders[i].setMaximum(val)
                self.max_labels[i].setText(str(val))
            except ValueError:
                pass
        return func

    def create_number_func(self, i):
        def func():
            self.active_numbers[i] = True
        return func

    def create_stop_slider_func(self, i):
        def func():
            self.active_sliders[i] = False
        return func

    def create_zero_slider_func(self, i):
        def func():
            self.sliders[i].setValue(0)
        return func

    def create_stop_number_func(self, i):
        def func():
            self.active_numbers[i] = False
        return func

    def create_zero_number_func(self, i):
        def func():
            self.line_edits[i].setText('0')
        return func


    '''
    sensor_msgs/JointState Message configurations
    
    * the position of the joint (rad or m)
    * the velocity of the joint (rad/s or m/s)
    * the effort that is applied in the joint (Nm or N)

    Header header
    string[] name
    float64[] position
    float64[] velocity
    float64[] effort
    
    slider1 -> publisher0
    slider2 -> publisher1
            .
            .
    slider8 -> publisher7
    '''
    
    def publish1_joint_state(self, slider_index):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f"joint{1}"]
        msg.position = [float(self.sliders[0].value())]
        #msg.velocity = [float(value)]
        #msg.effort = [float(value)]
        self.publisher0.publish(msg)

    def publish2_joint_state(self, slider_index):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f"joint{2}"]
        msg.position = [float(self.sliders[1].value())]
        self.publisher1.publish(msg)
        
    def publish3_joint_state(self, slider_index):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f"joint{3}"]
        msg.position = [float(self.sliders[2].value())]
        self.publisher2.publish(msg)

    def publish4_joint_state(self, slider_index):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f"joint{4}"]
        msg.position = [float(self.sliders[3].value())]
        self.publisher3.publish(msg)

    def publish5_joint_state(self, slider_index):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f"joint{5}"]
        msg.position = [float(self.sliders[4].value())]
        self.publisher4.publish(msg)

    def publish6_joint_state(self, slider_index):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f"joint{6}"]
        msg.position = [float(self.sliders[5].value())]
        self.publisher5.publish(msg)

    def publish7_joint_state(self, slider_index):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f"joint{7}"]
        msg.position = [float(self.sliders[6].value())]
        self.publisher6.publish(msg)

    def publish8_joint_state(self, slider_index):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f"joint{8}"]
        msg.position = [float(self.sliders[7].value())]
        self.publisher7.publish(msg)
        


    def update(self):
        # This method gets called at 100Hz
        # Output messages enable us to verify that each slider is connected well to the ROS
        if self.active_sliders[0]:
            self.publish1_joint_state(0)
            print(f"{{ Slider 1 output : {self.sliders[0].value()} }}")
        if self.active_sliders[1]:
            self.publish2_joint_state(1)
            print(f"{{ Slider 2 output : {self.sliders[1].value()} }}")
        if self.active_sliders[2]:
            self.publish3_joint_state(2)
            print(f"{{ Slider 3 output : {self.sliders[2].value()} }}")
        if self.active_sliders[3]:
            self.publish4_joint_state(3)
            print(f"{{ Slider 4 output : {self.sliders[3].value()} }}")
        if self.active_sliders[4]:
            self.publish5_joint_state(4)
            print(f"{{ Slider 5 output : {self.sliders[4].value()} }}")
        if self.active_sliders[5]:
            self.publish6_joint_state(5)
            print(f"{{ Slider 6 output : {self.sliders[5].value()} }}")
        if self.active_sliders[6]:
            self.publish7_joint_state(6)
            print(f"{{ Slider 7 output : {self.sliders[6].value()} }}")
        if self.active_sliders[7]:
            self.publish8_joint_state(7)
            print(f"{{ Slider 8 output : {self.sliders[7].value()} }}")
        
        
        
        '''
        gogogo
        '''
        for i, active in enumerate(self.active_numbers):
            if active:
                try:
                    val = int(self.line_edits[i].text())
                    print(f"{{ Number {i+1} output : {val} }}")
                except ValueError:
                    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec_())
