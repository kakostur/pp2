import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
with open ("sample-data.json" , "r") as file:
    data = json.load(file)

output = {
    "totalCount": str(len(data['imdata'])),
    "imdata":[]
}

for item in data['imdata']:
    l1PhysIf = item ['l1PhysIf']['attributes']

format_interface = "{:<60} {:<10} {:<9} {:<10}".format (
    l1PhysIf ['dn'] ,
    l1PhysIf ['descr'],
    l1PhysIf ['speed'] ,
    l1PhysIf ['mtu']
)


print (format_interface)
print ("="*80)