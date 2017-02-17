#import module
import os

# Create empty function
def rename_files():
    #1. Get all files names
    file_list = os.listdir(r"/Users/lmann/Desktop/udacity-python/prank/")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"/Users/lmann/Desktop/udacity-python/prank/")

    #2. Rename all files
    for file_name in file_list:
        os.rename(file_name, file_name.strip("1234567890"))
    os.chdir(saved_path)


rename_files()
