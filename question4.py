
import json

a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
file=open("q3,m.json","w")
file.write((json.dumps(a,sort_keys=True,indent=4)))
file.close()