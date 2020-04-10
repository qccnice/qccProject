import os
import sys

print(os.uname())
print(os.environ)
print(os.environ.get('PATH','default'))
print(os.environ.get('PATHs','default'))
print(sys.path)
print(sys.path[0])
print(os.path.dirname(sys.path[0]))