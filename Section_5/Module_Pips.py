# internal / build in modules...

import math
import mymodule

print(math.sqrt(16)) # squareroot..
mymodule.hello() # import from mymodule.py ..


# external mod ..

import requests

r=requests.get("https://www.google.com")
print(r.text) # give me whole html code for google ..


