import time
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Net import *
from Phidget22.ErrorCode import *
from tkinter import *

ACCEL = 2

#Line required to look for Phidget devices on the network
Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)

mtrA = DCMotor()
mtrA.setDeviceSerialNumber(469502)
mtrA.openWaitForAttachment(5000)
mtrA.setAcceleration(ACCEL)

mtrB = DCMotor()
mtrB.setDeviceSerialNumber(465371)
mtrB.openWaitForAttachment(5000)
mtrB.setAcceleration(ACCEL)

mtrC = DCMotor()
mtrC.setDeviceSerialNumber(474333)
mtrC.openWaitForAttachment(5000)
mtrC.setAcceleration(ACCEL)

#channelInfo = ChannelInfo()
#channelInfo.netInfo.serverDiscovery = discovery
#channelInfo.deviceSerialNumber = deviceSerialNumber
#channelInfo.channel = channel
#channelInfo.netInfo.isRemote = isRemote

root = Tk()

title = Label(root, text="3 Axis Open Loop Controller", font="Courier, 14")

def start_motor(direction):
    move(direction)

def stop_motor():
    mtrA.setTargetVelocity(0)
    mtrB.setTargetVelocity(0)
    mtrC.setTargetVelocity(0)

def move(direction):
    if direction == "A+":
        mtrA.setTargetVelocity(aVel.get())
    elif direction == "A-":
        mtrA.setTargetVelocity(-1*aVel.get())
    if direction == "B+":
        mtrB.setTargetVelocity(bVel.get())
    elif direction == "B-":
        mtrB.setTargetVelocity(-1*bVel.get())
    if direction == "C+":
        mtrC.setTargetVelocity(cVel.get())
    elif direction == "C-":
        mtrC.setTargetVelocity(-1*cVel.get())

b1 = Button(root, text="A+", font="Courier, 12")
b2 = Button(root, text="A-", font="Courier, 12")
b3 = Button(root, text="B+", font="Courier, 12")
b4 = Button(root, text="B-", font="Courier, 12")
b5 = Button(root, text="C+", font="Courier, 12")
b6 = Button(root, text="C-", font="Courier, 12")

aVel = Scale(root, from_=0, to=1, orient=HORIZONTAL, length=100, label="Motor A Velocity", resolution=.01)
bVel = Scale(root, from_=0, to=1, orient=HORIZONTAL, length=100, label="Motor B Velocity", resolution=.01)
cVel = Scale(root, from_=0, to=1, orient=HORIZONTAL, length=100, label="Motor C Velocity", resolution=.01)

title.grid(row=0, columnspan = 10, pady=10, sticky=N)
b1.grid(row=1,column=0, padx=5)
b2.grid(row=1,column=1, padx=5)
b3.grid(row=1,column=2, padx=5)
b4.grid(row=1,column=3, padx=5)
b5.grid(row=1,column=4, padx=5)
b6.grid(row=1,column=5, padx=5)
aVel.grid(row=2,column=0, columnspan=2, pady=10)
bVel.grid(row=2,column=2, columnspan=2, pady=10)
cVel.grid(row=2,column=4, columnspan=2, pady=10)


b1.bind('<ButtonPress-1>', lambda event: start_motor("A+"))
b1.bind('<ButtonRelease-1>', lambda event: stop_motor())

b2.bind('<ButtonPress-1>', lambda event: start_motor("A-"))
b2.bind('<ButtonRelease-1>', lambda event: stop_motor())

b3.bind('<ButtonPress-1>', lambda event: start_motor("B+"))
b3.bind('<ButtonRelease-1>', lambda event: stop_motor())

b4.bind('<ButtonPress-1>', lambda event: start_motor("B-"))
b4.bind('<ButtonRelease-1>', lambda event: stop_motor())

b5.bind('<ButtonPress-1>', lambda event: start_motor("C+"))
b5.bind('<ButtonRelease-1>', lambda event: stop_motor())

b6.bind('<ButtonPress-1>', lambda event: start_motor("C-"))
b6.bind('<ButtonRelease-1>', lambda event: stop_motor())



root.mainloop()
