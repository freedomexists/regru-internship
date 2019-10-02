import sys
import os
pth = sys.argv[1]
print(os.access(os.path.dirname(pth), os.X_OK))
