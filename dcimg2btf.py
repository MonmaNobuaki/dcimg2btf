import numpy as np
import tifffile
import tkinter as tk
from tkinter import filedialog, messagebox
import datetime
import os

# Please provide information about the video file you want to convert. width, height : number of pixels.
width,height = [576,576]

root = tk.Tk()
root.withdraw()


ready_1 = messagebox.showinfo('showinfo','Select directory for reading files')
target_dir = filedialog.askdirectory(initialdir = dir) 

ready_2 = messagebox.showinfo('showinfo','Select directory for saving files')
save_dir = filedialog.askdirectory(initialdir = dir) 
os.chdir(target_dir)

print("===============================================================")

time = datetime.datetime.now()

files = os.listdir(target_dir)
reading_file = []
for file in files:
    if str(file[-5:]) == 'dcimg':
        reading_file.append(file)
print('start in ' + str(time)[:-7])

for filename in reading_file:
    os.chdir(target_dir)

    print('Reading... ' + str(filename))
    MM = np.memmap(filename, mode='r', dtype='uint16')
    index = np.array(np.where(MM[0:len(MM)] == [65535]))

    Idx = []
    i = 0
    while i < len(index[0])-1:
        if index[0][i+1]  - index[0][i] == 2:
            Idx.append(index[0][i]-1)
            i+=1
        i+=1
    os.chdir(save_dir)
    flag = 0
    outFileName = str(filename)[:-6] + '_conv.btf'
    with tifffile.TiffWriter(outFileName,bigtiff=True,append = True) as tif:
        for ID in Idx:
            target = MM[ID:ID+int(width)*int(height)]
            tif.save(target.reshape(width,height))
            flag +=1
