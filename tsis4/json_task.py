import json

print(
"""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

def decode_json(name) -> dict():
    with open(name, 'r') as json_clear:
        json_str = json_clear.read()

    data = json.loads(json_str)
    return data

def giga_print(arr):
    print("{:35}\t{:23}\t{:10}".format(arr[0], arr[1], arr[2]),arr[3])

def solve(data):
    for i in range(len(data["imdata"])):
        dn = data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
        descr = data["imdata"][i]["l1PhysIf"]["attributes"]["descr"]
        speed = data["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
        mtu = data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
        arr = [dn,descr,speed,mtu]
        giga_print(arr)       

data = decode_json("simple_data.json")
solve(data)
