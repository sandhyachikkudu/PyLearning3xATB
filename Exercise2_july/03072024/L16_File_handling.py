# File handling
# how to read a file and write in to a file by using the python

# function
# variable = open('file_name','mode')

# 'mode'--different modes
# r --- for reading the file--default
# w----for writing(cereates the new file or append teh exising file)
# a---- for appending
# b---for binary mode(zoom.exe---binary)
# +--- for updating ---reading the writing



# For Read and Write the content
# read A FILE
# Reading the entire content: content =file_object.read()
# line =file_object.readline() for single line
# lines=file.object.readlines() for all lines

# file.close--close the file


file = open('testdata.txt','r')
content = file.read()
print(content)


















