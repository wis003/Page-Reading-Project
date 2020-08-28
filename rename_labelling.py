import os

paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk('C:\\Users\\18587\\Desktop\\Output')
        for filename in filenames)

for path in paths:
    newname = path.replace('Label', 'seg')
    if newname != path:
        os.rename(path, newname)