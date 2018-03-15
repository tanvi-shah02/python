#open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print ("Read string is: ", str)
fo.close()

