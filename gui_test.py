from guizero import App, Text, PushButton 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

def red_button():
    message.value = "Red"
    GPIO.output(23,GPIO.HIGH) ##switch LED button on
    GPIO.output(18,GPIO.LOW)##green LED off
    GPIO.output(24,GPIO.LOW)
    
def green_button():
    message.value = "Green"
    GPIO.output(18,GPIO.HIGH) ##green on
    GPIO.output(23,GPIO.LOW) ##red LED off
    GPIO.output(24,GPIO.LOW) ##blue off

    
def blue_button():
    message.value = "Blue"
    GPIO.output(18,GPIO.LOW) ##green off
    GPIO.output(24,GPIO.HIGH)##blue on
    GPIO.output(23,GPIO.LOW) ##red LED off

def exit_button():
    GPIO.output(18,GPIO.LOW)##green off
    GPIO.output(24,GPIO.LOW)##blue off
    GPIO.output(23,GPIO.LOW) #red off
    app.hide()

app = App(title="LED selector")
message = Text(app, text = "Please select 1 colour")
update_red = PushButton(app, command=red_button, text="Red")
update_green = PushButton(app, command=green_button, text="Green")
update_blue = PushButton(app, command=blue_button, text="Blue")
exit_button = PushButton(app, command=exit_button, text="Exit")
app.display()