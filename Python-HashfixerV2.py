def readAndFix(filename, outfilename):
	f = open(filename, "r")
	k = open(outfilename, "a+")
	for line in f:
		try:
			delimiterIndex = line.index(delimiter)
			print line.split(delimiter)
			data = line.split(delimiter)
			k.write(str(data))
			k.write("\n")
		except Exception as e:
			print "! ~ Error: " + str(e)
			print "(Common when end of file is reached.)"
	print "[~]Your hashes should be adjusted accordingly."        
	k.close()
	f.close()

print "Insert your delimiter here without quotes. Eg: :"
delimiter = str(raw_input("> "))       
readAndFix("test.txt", "pleasework.txt")
