from machine import Pin, ADC
import utime
#defining the x and y axis as well as the button
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(17,Pin.IN, Pin.PULL_UP)
#defining Pins that the different wires were attached to
led_left = Pin(14, Pin.OUT)
led_middle = Pin(15, Pin.OUT)
led_right = Pin(12, Pin.OUT)
led_up = Pin(18, Pin.OUT)
led_down = Pin(13, Pin.OUT)

while True:
    #while the joystick is in the middle and the button is not pressed, only the middle LED is on
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
   
    led_left.value(0)
    led_down.value(0)
    led_up.value(0)
    led_right.value(0)
    led_middle.value(1)
   
# Check the x and y Value to determine the status of the joystick
    if buttonValue == 0:
        #if the button is pressed, the middle one is turned off while the outer LEDs light up
        buttonStatus = "pressed"
        led_middle.value(0)
        led_right.value(1)
        led_left.value(1)
        led_down.value(1)
        led_up.value(1)
       
       
    if xValue <= 600:
        #if the joystick is moved to the left, the left LED turns on
        xStatus = "left"
        led_left.value(1)
        led_middle.value(0)
       
    if xValue >= 60000:
        #if the joystick is moved to the right, the right LED is turned on
        xStatus = "right"
        led_right.value(1)
        led_middle.value(0)
       
    if yValue <= 600:
        #if the joystick is moved to the up, the top LED is turned on
        yStatus = "up"
        led_up.value(1)
        led_middle.value(0)
       
    if yValue >= 60000:
        #if the joystick is moved down, the bottom LED lights up
        yStatus = "down"
        led_down.value(1)
        led_middle.value(0)
       
   
    #printing the location and button status of the joystick
    print("X: " + xStatus + ", Y: " + yStatus + "  button status: " + buttonStatus)
    utime.sleep(0.2)
