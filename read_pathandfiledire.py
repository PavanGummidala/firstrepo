import os
import sys

path=input("Enter your directory path: ")

if os.path.exists(path):
    df_l = os.listdir(path)
else:
    print("provide a valid path")
    sys.exit()


list_of_files_dir=os.listdir(path)
for each_file_dir in list_of_files_dir:
    f_d_p=os.path.join(path,each_file_dir)
    if os.path.isfile(f_d_p):
        print(f'{f_d_p} is a file')
    else:
        print(f'{f_d_p} is a directory')
