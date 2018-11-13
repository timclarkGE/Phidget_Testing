from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.CurrentInput import *
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Net import *
from tkinter import *
import time

#Equipment Serial Numbers
SN_TILT = 465371
SN_PAN = 469502

ACCEL = 2

#Line required to look for Phidget devices on the network
Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)

relay = DigitalOutput()
relay.setDeviceSerialNumber(540047)
relay.openWaitForAttachment(1000)
relay.setHubPort(2)
relay.setIsHubPortDevice(False)
relay.setIsLocal(True)
relay.setChannel(0)


print(relay.getDeviceSerialNumber())
relay.setState(True)
time.sleep(1)
print(relay.getDeviceClass())
relay.setState(False)
print("here")

#root = Tk()

#root.mainloop()

