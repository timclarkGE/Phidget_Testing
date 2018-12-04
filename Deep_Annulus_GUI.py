from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.CurrentInput import *
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.Net import *
from tkinter import *

def updateCurrent():
    if A:
        aCur_reading.set(aCur.getCurrent())
    if B:
        bCur_reading.set(bCur.getCurrent())
    if C:
        cCur_reading.set(cCur.getCurrent())
    root.after(100,updateCurrent)

def joystick_movement(self, ratio):
    #default ratio 0.48
    mtrC.setTargetVelocity(round(2*(ratio-0.48),1))
    print(round(2*(ratio-0.48),1))

def holding_voltage(value):
    print(value)
    mtrA.setTargetVelocity(-1*float(value))


#Set which controllers are connected
A = 1
B = 0
C = 0

ACCEL = 2

#Line required to look for Phidget devices on the network
Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)

if A:
    # Motor A: Setup Motor Control and Motor Current
    mtrA = DCMotor()
    mtrA.setDeviceSerialNumber(534830)
    mtrA.openWaitForAttachment(1000)
    mtrA.setAcceleration(ACCEL)

    aCur = CurrentInput()
    aCur.setDeviceSerialNumber(534830)
    aCur.openWaitForAttachment(1000)

if B:
    # Motor B: Setup Motor Control and Motor Current
    mtrB = DCMotor()
    mtrB.setDeviceSerialNumber(465371)
    mtrB.openWaitForAttachment(1000)
    mtrB.setAcceleration(ACCEL)

    bCur = CurrentInput()
    bCur.setDeviceSerialNumber(465371)
    bCur.openWaitForAttachment(1000)

if C:
    # Motor C: Setup Motor Control and Motor Current
    mtrC = DCMotor()
    mtrC.setDeviceSerialNumber(474333)
    mtrC.openWaitForAttachment(1000)
    mtrC.setAcceleration(ACCEL)

    cCur = CurrentInput()
    cCur.setDeviceSerialNumber(474333)
    cCur.openWaitForAttachment(1000)

    pot = VoltageRatioInput()
    pot.setDeviceSerialNumber(474333)
    pot.openWaitForAttachment(1000)
    pot.setOnVoltageRatioChangeHandler(joystick_movement)
    pot.setVoltageRatioChangeTrigger(0.05)



root = Tk()

if A:
    aCur_reading = StringVar()
if B:
    bCur_reading = StringVar()
if C:
    cCur_reading = StringVar()

title = Label(root, text="3 Axis Open Loop Controller", font="Courier, 14")
if A:
    l1 = Label(root, text="Cur(A)")
if B:
    l2 = Label(root, text="Cur(A)")
if C:
    l3 = Label(root, text="Cur(A)")

def start_motor(direction):
    move(direction)

def stop_motor():
    if A:
        mtrA.setTargetVelocity(0)
        mtrA.setTargetVelocity(-1*float(aHold.get()))
    if B:
        mtrB.setTargetVelocity(0)
    if C:
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
if A:
    b1 = Button(root, text="A+", font="Courier, 12")
    b2 = Button(root, text="A-", font="Courier, 12")
if B:
    b3 = Button(root, text="B+", font="Courier, 12")
    b4 = Button(root, text="B-", font="Courier, 12")
if C:
    b5 = Button(root, text="C+", font="Courier, 12")
    b6 = Button(root, text="C-", font="Courier, 12")

#Create the velocity scales
if A:
    aVel = Scale(root, from_=0, to=1, orient=HORIZONTAL, length=100, label="Motor A Velocity", resolution=.01)
    aHold = Scale(root, from_=0, to=.12, orient=HORIZONTAL, length=100, label="Holding Voltage", resolution=.005, command=holding_voltage)
if B:
    bVel = Scale(root, from_=0, to=1, orient=HORIZONTAL, length=100, label="Motor B Velocity", resolution=.01)
if C:
    cVel = Scale(root, from_=0, to=1, orient=HORIZONTAL, length=100, label="Motor C Velocity", resolution=.01)

#Create the boxes for displaying the current
if A:
    e1 = Entry(root, width=5, state="readonly", textvariable = aCur_reading)
if B:
    e2 = Entry(root, width=5, state="readonly", textvariable = bCur_reading)
if C:
    e3 = Entry(root, width=5, state="readonly", textvariable = cCur_reading)

title.grid(row=0, columnspan = 10, pady=10, sticky=N)
if A:
    b1.grid(row=1,column=0, padx=5)
    b2.grid(row=1,column=1, padx=5)
    aVel.grid(row=2,column=0, columnspan=2, pady=10)
    l1.grid(row=3,column=0)
    e1.grid(row=3,column=1)
    aHold.grid(row=4,column=0, columnspan=2, pady=10)

    b1.bind('<ButtonPress-1>', lambda event: start_motor("A+"))
    b1.bind('<ButtonRelease-1>', lambda event: stop_motor())

    b2.bind('<ButtonPress-1>', lambda event: start_motor("A-"))
    b2.bind('<ButtonRelease-1>', lambda event: stop_motor())

if B:
    b3.grid(row=1,column=2, padx=5)
    b4.grid(row=1,column=3, padx=5)
    bVel.grid(row=2,column=2, columnspan=2, pady=10)
    l2.grid(row=3,column=2)
    e2.grid(row=3,column=3)

    b3.bind('<ButtonPress-1>', lambda event: start_motor("B+"))
    b3.bind('<ButtonRelease-1>', lambda event: stop_motor())

    b4.bind('<ButtonPress-1>', lambda event: start_motor("B-"))
    b4.bind('<ButtonRelease-1>', lambda event: stop_motor())

if C:
    b5.grid(row=1,column=4, padx=5)
    b6.grid(row=1,column=5, padx=5)
    cVel.grid(row=2,column=4, columnspan=2, pady=10)
    l3.grid(row=3,column=4)
    e3.grid(row=3,column=5)

    b5.bind('<ButtonPress-1>', lambda event: start_motor("C+"))
    b5.bind('<ButtonRelease-1>', lambda event: stop_motor())

    b6.bind('<ButtonPress-1>', lambda event: start_motor("C-"))
    b6.bind('<ButtonRelease-1>', lambda event: stop_motor())

updateCurrent()
root.mainloop()

