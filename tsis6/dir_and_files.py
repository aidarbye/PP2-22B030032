import os
root_dir = os.getcwd()
# 1
# os.getcwd() - get current working directory
# os.walk(path) - traverse a directory
# root_dir = "/Users/aidarnurkin/Desktop/DigitalDesign"
# for dirpath, dirnames, filenames in os.walk(root_dir):
#     print("directory:", dirpath)
#     print("subdirectories:", dirnames)
#     print("files:", filenames)

# 2
# os.F_OK: Tests existence of the path.
# os.R_OK: Tests readability of the path.
# os.W_OK: Tests writability of the path.
# os.X_OK: Checks if path can be executed.

# print("Path doesnt exist" if not os.access(root_dir, os.F_OK) else "Path exist")
# print("Path is not readable" if not os.access(root_dir, os.R_OK) else "Path is readable")
# print("Path is not writable" if not os.access(root_dir, os.W_OK) else "Path is writable")
# print("Path is not executable" if not os.access(root_dir, os.X_OK) else "Path is executable")

# 3

# if os.path.exists(root_dir):
#     print("Directory portion:", os.path.dirname(root_dir))
#     print("Filename portion:", os.path.basename(root_dir))
# else:
#     print("Path does not exist")

# 4
# -File Handling-
# Read Only ('r’)
# Read and Write ('r+’)
# Write Only ('w’)
# Write and Read ('w+’)
# Append Only ('a’)
# Append and Read (‘a+’)
             
# filename = f"{root_dir}/text.txt"
# with open(filename, "r") as file:
#     lines = file.readlines()
#     print("The number of lines in the file is:", len(lines))

# 5
# arr = ["Nurkin","Aidar"]
# filename = f"{root_dir}/text.txt"
# with open(filename, "w") as file:
#     for i in arr:
#         file.write(i + ' ') 

# 6
# root_dir = f"{root_dir}/fromAtoZ"
# arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# for i in arr:
#     filename = root_dir+"/"+i+".txt"
#     with open(filename, "w") as file:
#         print("created")

# 7

# with open(f"{root_dir}/text.txt", "r") as file:
#     with open(f"{root_dir}/dest.txt", "w") as dest_file:
#         dest_file.write(file.read())

# 8
root_dir += "/needdeleted.txt"
with open(root_dir,"w") as file:
    print("created")
# if os.path.exists(root_dir):
#     if not os.access(root_dir, os.W_OK):
#         print("You do not have write access")
#     else:
#         os.remove(root_dir)
# else:
#     print("Path doesnt exist")

