

import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
python_file=open("q2,m.json","w")
json.dump(a,python_file,indent=6)
python_file.close()






