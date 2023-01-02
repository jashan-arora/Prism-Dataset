import os
path = r"/Users/jashanarora/Downloads/Prism-Dataset/LEDTV"
x = "IMG_4"
y = "LEDTV"
for count, filename in enumerate(os.listdir(path)):
    dst = f"{os.path.splitext(filename)[0].replace(x,y)}{os.path.splitext(filename)[1]}"
    # foldername/filename, if .py file is outside folder
    src = f"{path}/{filename}"
    dst = f"{path}/{dst}"
    # rename() function will
    # rename all the files
    os.rename(src, dst)
