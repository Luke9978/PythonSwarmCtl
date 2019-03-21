# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
from prompt_toolkit import prompt
import curses

ESC_L=12  #Connect the left ESC in this GPIO pin
ESC_R=13  #Connect the right ESC in this GPIO pin

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC_L, 0)
pi.set_servo_pulsewidth(ESC_R, 0)



max_value = 2500 #change this if your ESC's max value is different or leave it be
min_value = 1400  #change this if your ESC's min value is different or leave it be
idle_value= 1000
turn_value= 2000
print ("For first time launch, select calibrate")
print ("Arm will arm motors and then start them")
print ("Type the exact word for the function you want")
print ("calibrate OR arm OR expo OR stop OR calibrate_expo")

def calibrate():   #This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC_L, 0)
    pi.set_servo_pulsewidth(ESC_R, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC_L, max_value)
        pi.set_servo_pulsewidth(ESC_R, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':
                time.sleep(2)
                pi.set_servo_pulsewidth(ESC_L, min_value)
                pi.set_servo_pulsewidth(ESC_R, min_value)
                time.sleep(7)
                print ("Motor is calibrated, now arming motor")
                pi.set_servo_pulsewidth(ESC_L, 0)
                pi.set_servo_pulsewidth(ESC_R, 0)
                arm()

def calibrate_expo():   #This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC_L, 0)
    pi.set_servo_pulsewidth(ESC_R, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC_L, max_value)
        pi.set_servo_pulsewidth(ESC_R, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':
            time.sleep(2)
            pi.set_servo_pulsewidth(ESC_L, min_value)
            pi.set_servo_pulsewidth(ESC_R, min_value)
            time.sleep(7)
            print ("Motor is calibrated, now arming motor")
            pi.set_servo_pulsewidth(ESC_L, 0)
            pi.set_servo_pulsewidth(ESC_R, 0)
            expo()

def arm(): #This is the arming procedure of an ESC
    pi.set_servo_pulsewidth(ESC_L, min_value)
    pi.set_servo_pulsewidth(ESC_R, min_value)
    print ("Disconnect battery if connected. Then, connect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        time.sleep(5)
        pi.set_servo_pulsewidth(ESC_L, idle_value)
        pi.set_servo_pulsewidth(ESC_R, idle_value)
        time.sleep(2)

        while True:
                inp = raw_input()
                if inp == "stop":
                        stop()
                        break
                else:
                        pi.set_servo_pulsewidth(ESC_L,inp)
                        pi.set_servo_pulsewidth(ESC_R,inp)

def expo(): #This is the arming procedure of an ESC
    pi.set_servo_pulsewidth(ESC_L, min_value)
    pi.set_servo_pulsewidth(ESC_R, min_value)
    print ("Disconnect battery if connected. Then, connect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        time.sleep(5)
        pi.set_servo_pulsewidth(ESC_L, min_value+100)
        pi.set_servo_pulsewidth(ESC_R, min_value+100)
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC_L, idle_value)
        pi.set_servo_pulsewidth(ESC_R, idle_value)
        time.sleep(2)
        print ("Start manual control, left, right, forward, and idle")

        # Curses Setup
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)

        while True:
                button = screen.getch()

                if button == ord('q'):
                        break
                elif button == curses.KEY_UP:
                        forward()
                elif button == curses.KEY_DOWN:
                        idle()
                elif button == curses.KEY_LEFT:
                        left_turn()
                elif button == curses.KEY_RIGHT:
                        right_turn()
                elif button == ord(' '):
                        stop()
                elif button == ord('w'):
                        w()
                elif button == ord('s'):
                        s()
                elif button == ord('x'):
                        x()
                elif button == ord('e'):
                        e()
                elif button == ord('d'):
                        d()
                elif button == ord('c'):
                        c()
                elif button == ord('r'):
                        w()
                elif button == ord('f'):
                        s()
                elif button == ord('v'):
                        x()
                elif button == ord('t'):
                        e()
                elif button == ord('g'):
                        d()
                elif button == ord('b'):
                        c()

def forward():
        print("Now moving straight forward")
        pi.set_servo_pulsewidth(ESC_L,max_value)
        pi.set_servo_pulsewidth(ESC_R,max_value)

def idle():
        print("Now idling")
        pi.set_servo_pulsewidth(ESC_L,idle_value)
        pi.set_servo_pulsewidth(ESC_R,idle_value)

def left_turn():
        print("Now turning left")
        pi.set_servo_pulsewidth(ESC_L,turn_value)
        pi.set_servo_pulsewidth(ESC_R,max_value)

def right_turn():
        print("Now turning right")
        pi.set_servo_pulsewidth(ESC_L,max_value)
        pi.set_servo_pulsewidth(ESC_R,turn_value)

def w():
        pi.set_servo_pulsewidth(ESC_L, 2400)
        pi.set_servo_pulsewidth(ESC_R, 2400)

def s():
        pi.set_servo_pulsewidth(ESC_L, 2200)
        pi.set_servo_pulsewidth(ESC_R, 2200)
def x():
        pi.set_servo_pulsewidth(ESC_L, 2000)
        pi.set_servo_pulsewidth(ESC_R, 2000)
def e():
        pi.set_servo_pulsewidth(ESC_L, 1800)
        pi.set_servo_pulsewidth(ESC_R, 1800)

def d():
        pi.set_servo_pulsewidth(ESC_L, 1600)
        pi.set_servo_pulsewidth(ESC_R, 1600)
def c():
        pi.set_servo_pulsewidth(ESC_L, 1450)
        pi.set_servo_pulsewidth(ESC_R, 1450)
def r():
        pi.set_servo_pulsewidth(ESC_L, 1200)
        pi.set_servo_pulsewidth(ESC_R, 1200)

def f():
        pi.set_servo_pulsewidth(ESC_L, 1000)
        pi.set_servo_pulsewidth(ESC_R, 1000)
def v():
        pi.set_servo_pulsewidth(ESC_L, 800)
        pi.set_servo_pulsewidth(ESC_R, 800)
def t():
        pi.set_servo_pulsewidth(ESC_L, 600)
        pi.set_servo_pulsewidth(ESC_R, 600)

def g():
        pi.set_servo_pulsewidth(ESC_L, 500)
        pi.set_servo_pulsewidth(ESC_R, 500)
def b():
        pi.set_servo_pulsewidth(ESC_L, 1500)
        pi.set_servo_pulsewidth(ESC_R, 1500)

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC_L, 0)
    pi.set_servo_pulsewidth(ESC_R, 0)
    pi.stop()
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()

#This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.
inp = raw_input()
if inp == "calibrate":
    calibrate()
elif inp == "arm":
    arm()
elif inp == "calibrate_expo":
    calibrate_expo()
elif inp == "expo":
    expo()
elif inp == "stop":
    stop()
else :
    print ("Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!")
