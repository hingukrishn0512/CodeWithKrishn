from typing import Dict

dict1 : dict = {"a":1 , "b": 2}
dict2: dict = {"c":3 , "d":4}

merged = dict1 | dict2

print((merged , type(merged)))

 #we can merged the dictinaery also