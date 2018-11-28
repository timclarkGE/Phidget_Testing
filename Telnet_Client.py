import telnetlib

HOST = "localhost"
#Connect us to the server
tn = telnetlib.Telnet(HOST, "2217")

tn.write("Hello World")
print(tn.read_all())
