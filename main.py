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
click_points = []

def get_points(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        click_points.append((x,y))
        print(click_points)
        print(f'{x}, {y}')

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
    if selection == 'a' or selection == 'A':
        manual_control()
    if selection == 'b' or selection == 'B':
        setup_view()

def manual_control():
    exited = False
    print('WASD Control')
    while not exited:
        key_input = input()
        if key_input == 'w':
            arduino.write(bytes('<10A>', 'utf-8'))
            time.sleep(0.05)
            print(arduino.readline())

def setup_view():
    print('Select Corners (Top Left, Top Right, Bottom Right, Bottom Left)')
    img = cv.imread('/home/siddn/Pictures/standard-grid.jpg')
    img = cv.resize(img, (500,500))
    cv.namedWindow('Main View')
    cv.setMouseCallback('Main View', get_points)
    click_points = []
    while len(click_points) < 4:
        # print(click_points)
        cv.imshow('Main View', img)
        cv.waitKey(1)
    frame_corners = click_points.copy()
    print(frame_corners)
    # cv.waitKey(0)
    cv.destroyAllWindows()


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