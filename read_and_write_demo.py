## Reading from and writing to files
# We learned the basics of using context managers to read data
# from a file, make sure to have the data.txt file in the same
# directory as this file, otherwise you have to provide the full
# path to the file


file_name = 'data.txt'
with open(file_name) as f:
    for line in f:
        print(line.strip())




