# This program will let you test your ESC and brushless motor.
# Make sure your battery is not connected if you are going to calibrate it at first.
# Since you are testing your motor, I hope you don't have your propeller attached to it otherwise you are in trouble my friend...?
# This program is made by AGT @instructable.com. DO NOT REPUBLISH THIS PROGRAM... actually the program itself is harmful                                             pssst Its not, its safe.
import pigpio  # importing GPIO library
import curses
import os  # importing os library so as to communicate with the system
import time  # importing time library to make Rpi wait because its too impatient
import serial
os.system("sudo pigpiod")  # Launching GPIO library
# As i said it is too impatient and so if this delay is removed you will get an error
time.sleep(1)

ESC_L = 12  # Connect the left ESC in this GPIO pin
ESC_R = 13  # Connect the right ESC in this GPIO pin
pi = pigpio.pi()
max_value = 2500  # change this if your ESC's max value is different or leave it be
min_value = 1400  # change this if your ESC's min value is different or leave it be
idle_value = 1000
turn_value = 2000

ser = serial.Serial("/dev/serial0",9600)

def arm():  # This is the arming procedure of an ESC
    set_servo_pulsewidth(0)
    print("Disconnect the battery and press Enter")
    #inp = input()
    if '' == '':
        set_servo_pulsewidth(max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if '' == '':
            time.sleep(2)
            set_servo_pulsewidth(min_value)
            time.sleep(7)
            print("Motor is calibrated, now arming motor")
            set_servo_pulsewidth(0)
    set_servo_pulsewidth(min_value)
    time.sleep(5)
    set_servo_pulsewidth(min_value + 100)
    time.sleep(1)
    set_servo_pulsewidth(idle_value)
    time.sleep(2)
    print("Start manual control, left, right, forward, and idle")

    # Curses Setup
    #screen = curses.initscr()
    #curses.noecho()
    #curses.cbreak()
    #screen.keypad(True)

    while True:
        if ser.inWaiting() !=0:
            rec = str(ser.readline())
            print(rec)
        if button == ord('q'):
            break
        #elif button == curses.KEY_UP:
            #print("Now moving straight forward")
            #set_servo_pulsewidth(max_value)
        #elif button == curses.KEY_DOWN:
            #print("Now idling")
            #set_servo_pulsewidth(idle_value)
        #elif button == curses.KEY_LEFT:
            #print("Now turning left")
            #set_servo_pulsewidth(turn_value, max_value)
        #elif button == curses.KEY_RIGHT:
            #print("Now turning right")
            #set_servo_pulsewidth(max_value, turn_value)
        elif ' ' in rec:
            stop()
        elif 'w' in rec:
            set_servo_pulsewidth(2200)
        elif 's' in rec:
            set_servo_pulsewidth(1800)
        elif 'x' in rec:
            set_servo_pulsewidth(1450)
        elif button == ord('e'):
            set_servo_pulsewidth(1800)
        elif button == ord('d'):
            set_servo_pulsewidth(1600)
        elif button == ord('c'):
            set_servo_pulsewidth(1600)
        elif button == ord('r'):
            set_servo_pulsewidth(2400)
        elif button == ord('f'):
            set_servo_pulsewidth(2200)
        elif button == ord('v'):
            set_servo_pulsewidth(2000)
        elif button == ord('t'):
            set_servo_pulsewidth(1800)
        elif button == ord('g'):
            set_servo_pulsewidth(1600)
        elif button == ord('b'):
            set_servo_pulsewidth(1450)

def set_servo_pulsewidth(*speeds): # can feed this function one or two speeds to set L R respoectively
    if len(speeds) == 2:
        pi.set_servo_pulsewidth(ESC_L,speeds[0])
        pi.set_servo_pulsewidth(ESC_R,speeds[1])

    elif len(speeds) == 1:
        pi.set_servo_pulsewidth(ESC_L,speeds[0])
        pi.set_servo_pulsewidth(ESC_R,speeds[0])

def stop():  # This will stop every action your Pi is performing for ESC ofcourse.
    set_servo_pulsewidth(0)
    pi.stop()
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()



###############################################################################
#                                   START OF PROGRAM
###############################################################################

set_servo_pulsewidth(0)
print("Arm will arm motors and then start them")
print("Type the exact word for the function you want")
print("arm OR stop")

inp = input()
if inp == "arm":
    arm()
elif inp == "stop":
    stop()
else:
    print("Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!")
