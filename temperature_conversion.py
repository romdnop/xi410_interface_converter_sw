#from math import abs
import numpy
from itertools import count, takewhile

TIMER_CLK_SOURCE = 48e6
TIMER_CLK = 48e6

OUTPUT_PWM_FREQ = 10e3  
TIMER_ARR_VALUE = TIMER_CLK/OUTPUT_PWM_FREQ #value to be written to ARR register, sets PWM freq to OUTPUT_PWM_FREQ

TEMP_LOW = -20
TEMP_HIGH = 45

PWM_TEMP_LOW = TIMER_ARR_VALUE*0.3 #0.4
PWM_TEMP_HIGH = TIMER_ARR_VALUE*0.55 #0.65
PWM_TEMP_RESOLUTION = ((TEMP_HIGH+abs(TEMP_LOW))/(PWM_TEMP_HIGH - PWM_TEMP_LOW))
PWM_TEMP_ZERO = PWM_TEMP_LOW + abs(TEMP_LOW) / PWM_TEMP_RESOLUTION

current_temp = 23.3125
#current_temp = 0.0
current_voltage = 4.9106

VOLTAGE_TEMP_LOW = 1.78
VOLTAGE_TEMP_HIGH = 5.97
VOLTAGE_TEMP_RESOLUTION = (VOLTAGE_TEMP_HIGH - VOLTAGE_TEMP_LOW) / (PWM_TEMP_HIGH - PWM_TEMP_LOW)
VOLTAGE_TEMP_ZERO = VOLTAGE_TEMP_RESOLUTION * (abs(TEMP_LOW)/PWM_TEMP_RESOLUTION) + VOLTAGE_TEMP_LOW


def voltsToTemp(volts):
    #1) get counts first
    #2) get voltage from counts
    
    if(volts <= VOLTAGE_TEMP_ZERO):
        counts = PWM_TEMP_LOW + ((volts - VOLTAGE_TEMP_LOW)) / VOLTAGE_TEMP_RESOLUTION
        return countsToTemp(counts)
    if(volts > 0):
        counts = (volts - VOLTAGE_TEMP_ZERO) / VOLTAGE_TEMP_RESOLUTION + PWM_TEMP_ZERO
        return countsToTemp(counts)


def voltsToCounts(volts):
    if(volts <= VOLTAGE_TEMP_ZERO):
        return PWM_TEMP_LOW + ((volts - VOLTAGE_TEMP_LOW)) / VOLTAGE_TEMP_RESOLUTION
    if(volts > 0):
        #volts to counts: (volts - VOLTAGE_TEMP_ZERO) * (65.0 / VOLTAGE_TEMP_RESOLUTION )
        return (volts - VOLTAGE_TEMP_ZERO) / VOLTAGE_TEMP_RESOLUTION + PWM_TEMP_ZERO
    return 0

def countsToTemp(counts):
    if counts <= PWM_TEMP_LOW:
        return TEMP_LOW
    if counts >= PWM_TEMP_HIGH:
        return TEMP_HIGH
    if counts <= PWM_TEMP_ZERO:
        return -((PWM_TEMP_ZERO - counts) * PWM_TEMP_RESOLUTION)
    if counts > PWM_TEMP_ZERO:
        return (counts - PWM_TEMP_ZERO) * PWM_TEMP_RESOLUTION
    #return 0

def tempToCounts(temp):
    if temp <= TEMP_LOW:
        return PWM_TEMP_LOW
    if temp >= TEMP_HIGH:
        return PWM_TEMP_HIGH
    if temp >= 0:
        counts = temp/PWM_TEMP_RESOLUTION + abs(TEMP_LOW)/PWM_TEMP_RESOLUTION + PWM_TEMP_LOW
    if temp < 0:
        counts = abs(temp)/PWM_TEMP_RESOLUTION + PWM_TEMP_LOW
    return counts


print(f'Temp low limit: {TEMP_LOW}')
print(f'Temp high limit: {TEMP_HIGH}')
print(f'PWM_TEMP_LOW: {PWM_TEMP_LOW}')
print(f'PWM_TEMP_HIGH: {PWM_TEMP_HIGH}')
print(f'PWM_TEMP_ZERO: {PWM_TEMP_ZERO}')
print(f'Counts range (PWM_TEMP_HIGH - PWM_TEMP_LOW): {PWM_TEMP_HIGH - PWM_TEMP_LOW}')
print(f'PWM_TEMP_RESOLUTION: {PWM_TEMP_RESOLUTION} deg/count')
print(f'Current temp: {current_temp}')
print(f'Counts: {tempToCounts(current_temp)}')

print(f'Voltage temp low {TEMP_LOW}: {VOLTAGE_TEMP_LOW}')
print(f'Voltage temp high {TEMP_HIGH}: {VOLTAGE_TEMP_HIGH}')
print(f'Voltage temp ZERO: {VOLTAGE_TEMP_ZERO}')
print(f'Voltage temp RESOLUTION: {VOLTAGE_TEMP_RESOLUTION} V/count')

#print(f'voltsToCounts({current_voltage}) => {voltsToCounts(current_voltage)}')
#print(f'countsToTemp({voltsToCounts(current_voltage)}) => {countsToTemp(voltsToCounts(current_voltage))}')

def frange(start, stop, step):
    return takewhile(lambda x: x< stop, count(start, step))

for volts in list(frange(VOLTAGE_TEMP_LOW, VOLTAGE_TEMP_HIGH, 0.01)):
    #temperature = i
    #voltsToCounts()
    counts = voltsToCounts(volts)
    temp = countsToTemp(counts)

    tempV = voltsToTemp(volts)

    #voltsToCounts - countsToTemp
    print(f'voltsToTemp({volts:.2f}) => {tempV:.2f}')
    print(f'voltsToCounts({volts:.2f}) => {voltsToCounts(volts):.2f} ---- countsToTemp({counts:.2f}) => {temp:.2f}')
    #print(f'voltsToCounts(i) => ---- tempToCounts({i}) => {countsT:.2f} ----- countsToTemp({countsT:.2f}) => {countsToTemp(countsT):.2f}')
    #print(f'voltsToCounts({current_voltage}) => {voltsToCounts(current_voltage)}')
    #print(f'')


