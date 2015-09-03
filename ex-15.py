from sys import argv

script, filename = argv   #Assign each element in list argv to the variable 'script' and 'filename'

txt = open(filename)          # open the file as a variable

print "%r.Here's your file %r:" % (script, filename)
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
