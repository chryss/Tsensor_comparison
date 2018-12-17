# main.py -- put your code here!

[pyb.LED(i).off() for i in range(1, 5)]

interval = 1000
flashduration = 30
serial = pyb.USB_VCP()

def flashLED(num=1, duration=flashduration):
	pyb.LED(num).on()
	pyb.delay(duration)
	pyb.LED(num).off()

while True:
	serial.send("Hello!")
	flashLED(num=3)
	pyb.delay(interval-flashduration)
