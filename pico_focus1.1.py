from machine import PWM ,Pin , I2C
from ssd1306 import SSD1306_I2C
import time

# V 1.0     Sur 4 caracteres
titre ="Pico_focus v"
version ="1.1"
#  version avec oled

#Declarations

#PWM
#		slice/channel		GPIO1	GPIO2
#			2A				20		4
#			2B				21		5
#			1A				18		2
#			1B				19		3
STEP_motor1 = PWM(20, freq=15, duty_u16=32768)  # create a PWM object on a pin # set duty to 50%# and set freq and duty
DIR = machine.Pin(21, machine.Pin.OUT)
EN = machine.Pin(22, machine.Pin.OUT)


#  microstep
#				MS1		MS2		MS3
#	full step	0		0		0
#	1/2			1		0		0
# 	1/4			0		1		0
#	1/8			1		1		0
#	1/16		1		1		1
MS1= machine.Pin(26, machine.Pin.OUT)
MS2= machine.Pin(27, machine.Pin.OUT)
MS3= machine.Pin(28, machine.Pin.OUT)

#oled
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

rap = 100
lent = 100


led = machine.Pin('LED', machine.Pin.OUT)   #builin led

button_in =  Pin(13, Pin.IN, Pin.PULL_UP)
button_out =  Pin(14, Pin.IN, Pin.PULL_UP)
button_rapide =  Pin(15, Pin.IN, Pin.PULL_UP)

#init
led.value(0)
DIR.value(0)
print(DIR.value())
print(button_in())
STEP_motor1.deinit()
MS1.value(0)

oled.text("Pico_focus v"+version,0,0)  
oled.show()



while True:
    
    if button_in.value() == 0 :
        led.value(1)
        if button_rapide.value() == 0:
            MS1.value(0)
            MS2.value(0)
            MS3.value(0)
            STEP_motor1.init(freq=rap, duty_u16=32768)
            oled.fill(0)
            oled.text(titre+version,0,0)
            oled.text("IN   RAPIDE",0,16)  
            oled.show()
        else :
            MS1.value(1)
            MS2.value(1)
            MS3.value(0)
            STEP_motor1.init(freq=lent, duty_u16=32768)
            oled.fill(0)
            oled.text(titre+version,0,0)
            oled.text("IN   LENT",0,16)  
            oled.show()
            
    elif  button_out.value() == 0 :
        DIR.value(1)
        led.value(1)
        if button_rapide.value() == 0 :
            MS1.value(0)
            MS2.value(0)
            MS3.value(0)
            STEP_motor1.init(freq=rap, duty_u16=32768)
            oled.fill(0)
            oled.text(titre+version,0,0)
            oled.text("OUT  RAPIDE",0,16)  
            oled.show()
        else :
            MS1.value(1)
            MS2.value(1)
            MS3.value(0)
            STEP_motor1.init(freq=lent, duty_u16=32768)
            oled.fill(0)
            oled.text(titre+version,0,0)
            oled.text("OUT  LENT",0,16)  
            oled.show()
              
    else :
        DIR.value(0)
        EN.value(0)
        led.value(0)
        STEP_motor1.deinit()
        led.value(0)
        MS1.value(0)
        MS2.value(0)
        MS3.value(0)
    time.sleep(0.1)
    print(button_in())
    print(button_out())
    print(DIR.value())
    print(button_rapide.value())
    print("---" )
    print(MS1.value())
    print(MS2.value())
    print(MS3.value())
    print("***" )
    oled.fill(0)
    oled.text(titre+version,0,0)
    #oled.text("PRET",15,16) 
    oled.show()

#pwm.deinit()