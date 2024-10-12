# A first Python script
import sys
from importlib import reload
import script2
print(sys.platform)
print(2**100)
x = 'Spam!!'
print(x*8)
reload(script2)
