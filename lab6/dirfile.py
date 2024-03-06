#1
import os
path = os.getcwd()
print('Directories: ')
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
print('\nFiles: ')
for j in os.listdir(path):
    if os.path.isfile(os.path.join(path, j)):
        print(j)
print('\nAll Directories and Files: ')

for index, folder,file in os.walk(path):
    for i in folder:
        print(os.path.join(index, i))
    for j in file:
        print(os.path.join(index, j))




#2
import os
def check_path_access(path):
    access_info = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
    return access_info

access_info = check_path_access('/path/to/your/directory')
print(access_info)






#3
import os
def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist.")

test_path('/path/to/your/file.txt')





#4
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return -1

line_count = count_lines('/path/to/your/file.txt')
print("Number of lines:", line_count)




#5
def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print("Data written to", filename)
    except Exception as e:
        print("Error:", e)
data = ['apple', 'banana', 'orange']
write_list_to_file(data)





#6
import string
def generate_text_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")
generate_text_files()







#7
def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            with open(destination, 'w') as dest_file:
                dest_file.write(src_file.read())
        print("Contents copied from", source, "to", destination)
    except Exception as e:
        print("Error:", e)
copy_file('source.txt', 'destination.txt')







#8
import os
def delete_file(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print("File", path, "deleted successfully.")
        except Exception as e:
            print("Error:", e)
    else:
        print("File", path, "does not exist.")
delete_file('file_to_delete.txt')
