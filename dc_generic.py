import RPi.GPIO as GPIO
import curses
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
#Speed Varibles Pins
PWM1 = GPIO.PWM(12, 50)
PWM1.start(0)# This is the start value for the duty cycle
PWM2 = GPIO.PWM(13, 50)
PWM2.start(0)# This is the start value for the duty cycle
#Directional Varibles
D1 = 24
D2 = 26
#Setup for Curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(1)
#This is where the user input Starts
while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == ord('w'):
            GPIO.output(D1, True)
            GPIO.output(D2, True)
            print('Direction Set Forward')
        elif char == ord('x'):
            print('Direction Set Backward')
            GPIO.output(D1, False)
            GPIO.output(D2, False)
        elif  char == ord('q'):
            print('Speed Set High left')
            PWM1.ChangeDutyCycle(50)
        elif char == ord('e'):
            print('Speed set High Right')
            PWM2.ChangeDutyCycle(50)
        elif char == ord('a'):
            print('Speed set Medium Left')
            PWM1.ChangeDutyCycle(30)
        elif char == ord('d'):
            print('Speed Set Medium Right')
            PWM2.ChangeDutyCycle(30)
        elif char == ord('z'):
            print('Speed set Low Left')
            PWM1.ChangeDutyCycle(10)
        elif char == ord('c'):
            print('Speed set Low Right')
            PWM2.ChangeDutyCycle(10)
#Cleanup
GPIO.cleanup
curses.nobreak()
screen.keypad(0)
curses.echo()
curses.endwin()