import subprocess
import optparse
import re

def input_object():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac_adress",help="new mac adress")
    (user_inputs,arguments) = parse_object.parse_args()
    return user_inputs
def mac_terminal():
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_adress])
    subprocess.call(["ifconfig", interface, "up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        None

user_inputs = input_object()
interface = user_inputs.interface
mac_adress = user_inputs.mac_adress

mac_terminal()
finally_mac = control_new_mac(str(interface))

if finally_mac == mac_adress:
    print("Success")
else:
    print("Error!!")