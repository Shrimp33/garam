from main import *

p = PathManager('test', save=False)
p["test"] = "test"
print(p["test"])
p["test1"]["test2"] = "test2"
print(p["test1"]["test2"])
p["test1"]["test2"] = "test3"
print(p["test1"]["test2"])
