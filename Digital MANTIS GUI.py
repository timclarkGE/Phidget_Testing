#Known Bugs
#1  -   When using the pressure regulation at full pressure. The "pressure _reading.getSensorValue()" has a Phidget
#       Exception. This only happens during high pressure.

from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.CurrentInput import *
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.VoltageOutput import *
from Phidget22.Net import *
from tkinter import *
import time

#Hub Numbers for REL1000_0
HUB_ZOOM_ENABLE = 1
HUB_ZOOM_SELECT = 1
HUB_FOCUS_ENABLE = 2
HUB_FOCUS_SELECT = 1
HUB_MAN_SELECT = 2

#Channel Numbers for REL1000_0
CH_ZOOM_ENABLE = 1
CH_ZOOM_SELECT = 2
CH_FOCUS_ENABLE = 2
CH_FOCUS_SELECT = 0
CH_MAN_SELECT = 3

ACCEL = 2

MAXPR = 130.5
MINPR = 0.5

def focus(direction):
    if direction == "+":
        focus_enable.setState(True)
        focus_select.setState(False)
    elif direction == "-":
        focus_enable.setState(True)
        focus_select.setState(True)
    elif direction == "0":
        focus_enable.setState(False)

def zoom(direction):
    if direction == "+":
        zoom_enable.setState(True)
        zoom_select.setState(True)
    elif direction == "-":
        zoom_enable.setState(True)
        zoom_select.setState(False)
    elif direction == "0":
        zoom_enable.setState(False)

def set(state):
    if state == "ON":
        manual_select.setState(True)
    elif state == "OFF":
        manual_select.setState(False)

def update_left_intensity(val):
    left_light.setTargetVelocity(float(val)/100)

def update_right_intensity(val):
    right_light.setTargetVelocity(float(val) / 100)

def tilt_move(direction):
    if direction == "+":
        tilt.setTargetVelocity(float(tilt_speed.get())/100)
    elif direction == "-":
        tilt.setTargetVelocity(-1*float(tilt_speed.get())/100)
    elif direction == "0":
        tilt.setTargetVelocity(0)

def pan_move(direction):
    if direction == "R":
        pan.setTargetVelocity(float(pan_speed.get())/100)
    elif direction == "L":
        pan.setTargetVelocity(-1*float(pan_speed.get())/100)
    elif direction == "0":
        pan.setTargetVelocity(0)

def toggle_power():
    if power.getState() == True:
        power.setState(False)
    elif power.getState() == False:
        power.setState(True)


def set_pressure(val):
    #Pressure Range
    range = MAXPR - MINPR
    #Calculate volts/PSI
    ratio = 5 / range
    pressure_ctrl.setVoltage(float(val)*ratio)

def update_pressure():
    #val = float(pressure_reading.getSensorValue()) #range 0-1, if regulator is on it will be about 0.19
    #range = MAXPR - MINPR
    #pressure.set(round(range*val,2))
    val = float(pressure_reading.getSensorValue())
    PSI = val*160.5 -30.5
    pressure.set(round(PSI,2))
    root.after(100, update_pressure)

def actuate():
    if solenoid.getState() == True:
        solenoid.setState(False)
    elif solenoid.getState() == False:
        solenoid.setState(True)

def open_menu():
    wait = 0.15
    for x in range(3):
        set("ON")
        time.sleep(wait)
        set("OFF")
        time.sleep(wait)
    zoom("+")
    time.sleep(wait)
    zoom("0")

#Line required to look for Phidget devices on the network
Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)

#Setup Power Button
power = DigitalOutput()
power.setDeviceSerialNumber(540047)
power.setIsHubPortDevice(False)
power.setHubPort(1)
power.setChannel(3)
power.openWaitForAttachment(5000)

#Setup Focus, Zoom, and Manual Select:
focus_enable = DigitalOutput()
focus_enable.setDeviceSerialNumber(540047)
focus_enable.setIsHubPortDevice(False)
focus_enable.setHubPort(HUB_FOCUS_ENABLE)
focus_enable.setChannel(CH_FOCUS_ENABLE)
focus_enable.openWaitForAttachment(5000)

focus_select = DigitalOutput()
focus_select.setDeviceSerialNumber(540047)
focus_select.setIsHubPortDevice(False)
focus_select.setHubPort(HUB_FOCUS_SELECT)
focus_select.setChannel(CH_FOCUS_SELECT)
focus_select.openWaitForAttachment(5000)

zoom_enable = DigitalOutput()
zoom_enable.setDeviceSerialNumber(540047)
zoom_enable.setIsHubPortDevice(False)
zoom_enable.setHubPort(HUB_ZOOM_ENABLE)
zoom_enable.setChannel(CH_ZOOM_ENABLE)
zoom_enable.openWaitForAttachment(5000)

zoom_select = DigitalOutput()
zoom_select.setDeviceSerialNumber(540047)
zoom_select.setIsHubPortDevice(False)
zoom_select.setHubPort(HUB_ZOOM_SELECT)
zoom_select.setChannel(CH_ZOOM_SELECT)
zoom_select.openWaitForAttachment(5000)

manual_select = DigitalOutput()
manual_select.setDeviceSerialNumber(540047)
manual_select.setIsHubPortDevice(False)
manual_select.setHubPort(HUB_MAN_SELECT)
manual_select.setChannel(CH_MAN_SELECT)
manual_select.openWaitForAttachment(5000)

#Setup Lights
left_light = DCMotor()
left_light.setDeviceSerialNumber(540047)
left_light.setIsHubPortDevice(False)
left_light.setHubPort(0)
left_light.setChannel(0)
left_light.openWaitForAttachment(5000)
left_light.setAcceleration(20)

right_light = DCMotor()
right_light.setDeviceSerialNumber(540047)
right_light.setIsHubPortDevice(False)
right_light.setHubPort(5)
right_light.setChannel(0)
right_light.openWaitForAttachment(5000)
right_light.setAcceleration(20)

#Setup pan and tilt motors
tilt = DCMotor()
tilt.setDeviceSerialNumber(465371)
tilt.openWaitForAttachment(1000)
tilt.setAcceleration(ACCEL)

pan = DCMotor()
pan.setDeviceSerialNumber(469502)
pan.openWaitForAttachment(1000)
pan.setAcceleration(ACCEL)

#Setup Pnematics
pressure_ctrl = VoltageOutput()
pressure_ctrl.setDeviceSerialNumber(540047)
pressure_ctrl.setIsHubPortDevice(False)
pressure_ctrl.setHubPort(3)
pressure_ctrl.setChannel(0)
pressure_ctrl.openWaitForAttachment(5000)

pressure_reading = VoltageRatioInput()
pressure_reading.setDeviceSerialNumber(540047)
pressure_reading.setIsHubPortDevice(False)
pressure_reading.setHubPort(0)
pressure_reading.setChannel(0)
pressure_reading.openWaitForAttachment(5000)

solenoid = DigitalOutput()
solenoid.setDeviceSerialNumber(540047)
solenoid.setIsHubPortDevice(False)
solenoid.setHubPort(4)
solenoid.setChannel(3)
solenoid.openWaitForAttachment(5000)

root = Tk()

pressure = IntVar()

power_btn = Button(root, text="PWR", font="Courier, 12", command=toggle_power)
near = Button(root, text="NEAR", font="Courier, 12", width=7)
far = Button(root, text="FAR", font="Courier, 12", width=7)
wide = Button(root, text="WIDE", font="Courier, 12", width=7)
tele = Button(root, text="TELE", font="Courier, 12", width=7)
ms = Button(root, text="MS", font="Courier, 12", width=7)
left_light_scale = Scale(root, orient=VERTICAL, command=update_left_intensity)
right_light_scale = Scale(root, orient=VERTICAL, command=update_right_intensity)
label_lights = Label(root, text="Light Intensity")
tilt_up = Button(root, text="TILT UP", font="Courier, 12", width=10)
tilt_down = Button(root, text="TILT DOWN", font="Courier, 12", width=10)
pan_right = Button(root, text="PAN RIGHT", font="Courier, 12", width=10)
pan_left = Button(root, text="PAN LEFT", font="Courier, 12", width=10)
tilt_speed = Scale(root, orient=HORIZONTAL, from_=1, to=100)
pan_speed = Scale(root, orient=HORIZONTAL, from_=1, to=100)
pressure_input = Scale(root, orient=HORIZONTAL, from_=MINPR, to=MAXPR, label="Set Pressure (PSI)", command=set_pressure, resolution=0.5)
pressure_output = Entry(root, width=6, state="readonly", textvariable = pressure)
solenoid_btn = Button(root, text="AIR", font="Courier, 12", width=3, command=actuate)
menu = Button(root, text="CAMERA MENU", font="Courier, 12", width=16, command=open_menu)

tilt_speed.set(75)
pan_speed.set(75)

power_btn.grid(row=0, column=1)
ms.grid(row=1, column=1, padx=5, pady=5)
near.grid(row=0, column=2, padx=5, pady=5)
far.grid(row=1, column=2, padx=5, pady=5)
tele.grid(row=0,column=3, padx=5, pady=5)
wide.grid(row=1,column=3, padx=5, pady=5)
left_light_scale.grid(row=0, column=4,rowspan=2, padx=5,pady=5)
right_light_scale.grid(row=0, column=5,rowspan=2, padx=5,pady=5)
label_lights.grid(row=2, column = 4, columnspan=2)
tilt_up.grid(row=0,column=6, padx=5,pady=5)
tilt_down.grid(row=1,column=6, padx=5,pady=5)
pan_right.grid(row=0,column=7, padx=5,pady=5)
pan_left.grid(row=1,column=7, padx=5,pady=5)
tilt_speed.grid(row=2,column=6)
pan_speed.grid(row=2,column=7)
pressure_output.grid(row=0,column=8)
pressure_input.grid(row=1, column=8)
solenoid_btn.grid(row=0, column=9, rowspan=2, padx=5, pady=5)
menu.grid(row=2, column=0, columnspan=4)

near.bind('<ButtonPress-1>', lambda event: focus("+"))
near.bind('<ButtonRelease-1>', lambda event: focus("0"))
far.bind('<ButtonPress-1>', lambda event: focus("-"))
far.bind('<ButtonRelease-1>', lambda event: focus("0"))
wide.bind('<ButtonPress-1>', lambda event: zoom("-"))
wide.bind('<ButtonRelease-1>', lambda event: zoom("0"))
tele.bind('<ButtonPress-1>', lambda event: zoom("+"))
tele.bind('<ButtonRelease-1>', lambda event: zoom("0"))
ms.bind('<ButtonPress-1>', lambda event: set("ON"))
ms.bind('<ButtonRelease-1>', lambda event: set("OFF"))

tilt_up.bind('<ButtonPress-1>', lambda event: tilt_move("+"))
tilt_up.bind('<ButtonRelease-1>', lambda event: tilt_move("0"))
tilt_down.bind('<ButtonPress-1>', lambda event: tilt_move("-"))
tilt_down.bind('<ButtonRelease-1>', lambda event: tilt_move("0"))
pan_right.bind('<ButtonPress-1>', lambda event: pan_move("R"))
pan_right.bind('<ButtonRelease-1>', lambda event: pan_move("0"))
pan_left.bind('<ButtonPress-1>', lambda event: pan_move("L"))
pan_left.bind('<ButtonRelease-1>', lambda event: pan_move("0"))

update_pressure()
root.mainloop()

