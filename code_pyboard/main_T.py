# main.py -- put your code here!

import pyb
import dht
import machine
import sht31

[pyb.LED(i).off() for i in range(1, 5)]

interval = 4000
flashduration = 50
P36pin = 'Y11'
DHT11pin = 'X7'
SCLpin = 'X9'
SDApin = 'X10'

serial = pyb.USB_VCP()
p36 = pyb.ADC(pyb.Pin(P36pin))
d = dht.DHT11(machine.Pin(DHT11pin))
i2c = machine.I2C(sda=machine.Pin(SDApin), scl=machine.Pin(SCLpin), freq=400000)
sht31sensor = sht31.SHT31(i2c)

def flashLED(num=1, duration=flashduration):
	pyb.LED(num).on()
	pyb.delay(duration)
	pyb.LED(num).off()

def adc2mV(adcval):
	return adcval * 3300 / 4095

def p36_mV2C(mv):
	return (mv - 500)/10

serial.send('DHT11_T\tDHT11_T\tP36_T\tSHT31_T\tSHT31_H')

# while True:
# 	d.measure()
# 	p36val = p36.read()
# 	newtemp = p36_mV2C(adc2mV(p36val))
# 	sht31_t, sht31_h = sht31sensor.get_temp_humi()
# 	msg = "{}\t{}\t{:.2f}\t{:.2f}\t{:.2f}".format(
# 			d.temperature(), d.humidity(), 
# 			newtemp, sht31_t, sht31_h)
# 	serial.send(msg)
# 	flashLED(num=3)
# 	pyb.delay(interval-flashduration)
