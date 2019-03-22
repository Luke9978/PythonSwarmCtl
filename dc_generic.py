import time
import pigpio
import curses
import os
from prompt_toolkit import prompt
#set up of PIGPIO daemeaon
os.system("sudo pigpiod")
time.sleep(1)
pi = pigpio.pi()

#Speed Varibles Pins
PWM1 = 12
PWM2 = 13
#Speed Varibles with PWM
Max_Val = 2500  #Also True Values for Directional Varibles
Min_Val = 0     #Also False Value for Directional Varibles
#Directional Varibles
D1 = 24
D2 = 26
#Setup for Curses
screen =  curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(1)
#This is where the user input Starts
while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == ord('w'):
            print('Direction Set Forward')
        elif char == ord('x'):
            print('Direction Set Backward')
        elif  char == ord('q'):
            print('Speed Set High left')
        elif char == ord('e'):
            print('Speed set High Right')
        elif char == ord('a'):
            print('Speed set Medium Left')
        elif char == ord ('d'):
            print('Speed Set Medium Right')
        elif char == ord('z'):
            print('Speed set Low Left')
        elif char == ord('c'):
            print('Speed set Low Right')

#Cleanup
pi.stop()
curses.nobreak()
screen.keypad(0)
curses.echo()
curses.endwin()