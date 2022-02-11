import json

dict={"anisha":12,"annu":13,"nishu":14,"rani":15}
my_file=open("q4,m.json","w")
json.dump(dict,my_file,indent=6)
my_file.close()


