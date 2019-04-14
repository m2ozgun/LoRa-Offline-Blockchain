# Put your imports here
import os
import serial
from web3 import Web3, HTTPProvider
from interface import ContractInterface


# Initialize your web3 object
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
ser = serial.Serial('/dev/ttyUSB1', 115200)
ser.flushInput()

print("from:", w3.eth.accounts[0])
# Create a path object to your Solidity source files
contract_dir = os.path.abspath('./contracts/')
greeter_interface = ContractInterface(w3, 'Greeter', contract_dir)

# Initialize your interface
greeter_interface.compile_source_files()
greeter_interface.deploy_contract()
instance = greeter_interface.get_instance()

def strToHex32(zBytes):
    
    len1 = len(zBytes)
    if len1 > 32:
        zBytes32 = zBytes[:32]
    else:
        zBytes32 = zBytes.ljust(32, '0')
    return bytes(zBytes32, 'utf-8')

while True:
    ser_bytes = ser.readline()
    ser_bytes = ser_bytes.strip().decode('utf-8').replace("\n", "")
    ser_new = ser_bytes.split("> ")

    tx = instance.functions.setGreeting(strToHex32(ser_new[1])).transact()

    receipt = w3.eth.waitForTransactionReceipt(tx)

    print()
    print(w3.toBytes(instance.functions.greet().call()))

    inp = input()
    ser.write((inp + "\r").encode())
    ser.reset_input_buffer()

