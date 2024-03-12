import json


jsonvlue = {
    'best':'nikhil',
    'love':'kusomi'
}
f= open("nik.json",'w')
json.dump(jsonvlue,f,indent=10)


f.close()