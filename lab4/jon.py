import json
with open("sample-data.json", "r") as file:
    data = json.load(file)

output = {
    "totalCount": str (len (data ['imdata'])),
    "imdata" :[]
}

for item in data['imdata']:
    l1_phys_if = item ['l1PhysIf']['attributes']

format_interface = "{:<50} {:<80} {:<30}".format (
    l1_phys_if ['adminSt'],
    l1_phys_if ['autoNeg'],
    l1_phys_if ['brkoutMap']
)

print (format_interface)
print ("="*80)