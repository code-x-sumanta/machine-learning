#.......Java Script Object Notasion

import json

data='{"var1":"soom","var2":67}'
parsed=json.loads(data)
print(parsed)


data1={
    "name":"SumantaDey",
    "subjects":["math","physics","chemistry"]
}
jscomp=json.dumps(data1)
print(jscomp)