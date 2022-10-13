
import json

f = open("\\data\\data_1.json", "r")
data = json.load(f)

out_file = open("\\schema\\schema_1.json", "w")

del data["attributes"]

json.dump(data, out_file, indent = 6)
  
out_file.close()
