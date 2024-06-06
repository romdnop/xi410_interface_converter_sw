#from math import abs

TIMER_CLK_SOURCE = 48e6
TIMER_CLK = 48e6

OUTPUT_PWM_FREQ = 10e3  
TIMER_ARR_VALUE = TIMER_CLK/OUTPUT_PWM_FREQ #value to be written to ARR register, sets PWM freq to OUTPUT_PWM_FREQ

TEMP_LOW = -20
TEMP_HIGH = 45

PWM_TEMP_LOW = TIMER_ARR_VALUE*0.4
PWM_TEMP_HIGH = TIMER_ARR_VALUE*0.65

PWM_TEMP_RESOLUTION = ((TEMP_HIGH+abs(TEMP_LOW))/(PWM_TEMP_HIGH - PWM_TEMP_LOW))


current_temp = 23.3125
#current_temp = 0.0
current_voltage = 4.9106

VOLTAGE_TEMP_LOW = 3.47
VOLTAGE_TEMP_HIGH = 7.69
VOLTAGE_TEMP_RESOLUTION = (VOLTAGE_TEMP_HIGH - VOLTAGE_TEMP_LOW) / (PWM_TEMP_HIGH - PWM_TEMP_LOW)
VOLTAGE_TEMP_ZERO = VOLTAGE_TEMP_RESOLUTION * (abs(TEMP_LOW)/PWM_TEMP_RESOLUTION) + VOLTAGE_TEMP_LOW


def voltsToTemp(volts):
    if(volts <= VOLTAGE_TEMP_ZERO):
        return 0.0
    if(volts > 0):
        #volts to counts: (volts - VOLTAGE_TEMP_ZERO) * (65.0 / VOLTAGE_TEMP_RESOLUTION )
        return (volts - VOLTAGE_TEMP_ZERO) * (65.0 / VOLTAGE_TEMP_RESOLUTION ) 
    return 0

def countsToTemp(counts):
    if(counts <= )
    return 0

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
print(f'Counts range (PWM_TEMP_HIGH - PWM_TEMP_LOW): {PWM_TEMP_HIGH - PWM_TEMP_LOW}')
print(f'Current temp: {current_temp}')
print(f'Counts: {tempToCounts(current_temp)}')
print(f'Voltage temp RESOLUTION: {VOLTAGE_TEMP_RESOLUTION}')
print(f'Voltage temp low {TEMP_LOW}: {VOLTAGE_TEMP_LOW}')
print(f'Voltage temp high {TEMP_HIGH}: {VOLTAGE_TEMP_HIGH}')
print(f'Voltage temp ZERO: {VOLTAGE_TEMP_ZERO}')


print(f'voltsToTemp({current_voltage}) => {voltsToTemp(current_voltage)}')


