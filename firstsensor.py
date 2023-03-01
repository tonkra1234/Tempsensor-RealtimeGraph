import glob
import time
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def init():

    base_dir = '/sys/bus/w1/devices/'
    while True:
        try:
            device_folder = glob.glob(base_dir + '28*')[0]
            break
        except IndexError:
            sleep(0.5)
            continue
    device_file = device_folder + '/w1_slave'

    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    
    return lines


def read_temp1(x):

    global lines
    lines = x
    
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = x
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        
        return temp_c
    