file_name="file.txt"
file=open(file_name, "r")
a=file.read().split("\n")
print(a)
