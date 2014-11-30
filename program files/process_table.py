# Handles the input file and error checking for the generateSandbox.py file
import sys
import codecs


# Check to see if command line arguments are correct 
def properInputFiles():
	try:
		tableFileName = sys.argv[1]
		outputFileName = sys.argv[2]
		return (tableFileName, outputFileName)
	except IndexError or TypeError:
		print "Incorrect run of program. Must run as python generateSandbox.py \
		table.txt outputFileName"
		sys.exit(0) 

# Input for the table

def inputTable(filename):
	# Opening the file 
	try:
		file = codecs.open(filename)
	except IOError:
		print "Types file incorrectly formatting or does not exist."
		sys.exit(0)

	# Pulling types and values 
	types = file.readline().rstrip().split(",")
	values = file.readline().rstrip().split(",")

	# Converting values 
	values = checkValues(values)

	file.close()

	return (types, values)

def checkValues(values):
	valuesNum = []
	for v in values:
		try:
			v = float(v)
			valuesNum.append(v)
		except ValueError:
			print "Badly formed input values."
			sys.exit(0)

	return valuesNum

