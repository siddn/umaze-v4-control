"""
uMAZE microrobot control code

Author: Siddharth R Nathella, Purdue University
Created: July 19, 2021
"""

import cv2 as cv
import math as m
import numpy as np

import serial
import time

# arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
capture = cv.VideoCapture(0)
click_points = []


def get_points(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        click_points.append((x,y))

def mode_select():
    selection = input(
    """Select Operation Mode
    a) Manual Control
    b) Autonomous Control
    c) Preplanned Path
    d) Zone Identification
    e) Color Identifier
    q) Quit
    : """)
    frame_corners = setup_view()

    if selection == 'a' or selection == 'A':
        manual_control(frame_corners, 1)
    if selection == 'b' or selection == 'B':
        autonomous_control()

def manual_control(frame_corners,quadrant):
    exited = False
    print('WASD Control')

    while(True):
        ret, frame = capture.read()
        cv.imshow('Main Frame', frame)
        k = cv.waitKey(1)
        if k & 0xFF == ord('w'):
            print('w')
        if k & 0xFF == ord('a'):
            print('a')
        if k & 0xFF == ord('q'):
            break

    # while not exited:
    #     key_input = input()
    #     if key_input == 'w':
    #         arduino.write(bytes('<10A>', 'utf-8'))
    #         time.sleep(0.05)
    #         print(arduino.readline())
        

def autonomous_control():
    pass

def setup_view():
    print('Select Corners (Top Left, Top Right, Bottom Right, Bottom Left)')

    # Create Window and Frame
    cv.namedWindow('Main View')
    ret, frame = capture.read()

    # Set Mouse Callback to get clicked points
    cv.setMouseCallback('Main View', get_points)
    # Get Corner Points
    while len(click_points) < 4:
        cv.imshow('Main View', frame)
        cv.waitKey(1)
    cv.destroyAllWindows()
    frame_corners = np.array(click_points)
    print(frame_corners)
    return frame_corners



def main():
    mode_select()


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


# while True:
#     num = input("Enter a number: ")
#     value = write_read(num)
#     print(value)

if __name__ == "__main__":
    main()