import telnetlib
import time

HOST = "192.168.1.100"
#Connect us to the server
tn = telnetlib.Telnet(HOST, "2217")
text = "Hello World\n"
iter = 5
while iter:
    tn.write(text.encode('ascii'))
    time.sleep(1)
    iter -= 1
    print("here")
text2 = "DONE"
tn.write(text2.encode('ascii'))
tn.close()
print(tn.read_all())
