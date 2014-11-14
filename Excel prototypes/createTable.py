import xlwt
import codecs
import sys

from datetime import datetime

# you must program with 2 input files 
# wrap with try catch so if they fuck it, force a rerun

# check inputs (files correct)

 # while True:
 #        try:
 #            #file name of artists list
 #            inFileName = sys.argv[1]

 #            #cutoff value, inclusive
 #            cutOffValue = int(sys.argv[2])
 #            break
 #        except IndexError or TypeError:
 #            print ("Incorrect running of program. Must run as: 'python3 knewtonsolution.py Artist_lists_small.txt 50'")
 #            sys.exit()


def main():
	(typeFileName, valueFileName) = properInputFiles()
	wb = createWorkbook()
	ws = createWorksheet(wb, "abcdefghijklmnop")
	

	# parseFiles()
	
	return 

def properInputFiles():
	try:
		typeFileName = sys.argv[1]
		valueFileName = sys.argv[2]
		return (typeFileName, valueFileName)
	except IndexError or TypeError:
		print "Incorrect run of program. Must run as python2 createTable.py types.txt values.txt"
		sys.exit(0) 



def createWorkbook():
	return xlwt.Workbook()

def createWorksheet(workbook, sheetName):
	return workbook.add_sheet(sheetName);


def parseFiles():

	wb = xlwt.Workbook()
	style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
		num_format_str='#,##0.00')
	style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

	ws = wb.add_sheet('A Test Sheet')

	ouputFileName = sys.argv[1]

	# typeFileName = sys.argv[1]
	# valueFileName = sys.argv[2]

	typeFileName = "types.txt"
	valueFileName = "values.txt"

	types = inputTypes(typeFileName)

	values = inputValues(valueFileName)

	for typeIndex in range(len (types)):
		adjIndex = typeIndex +1
		ws.write(adjIndex, 0, types[typeIndex])

	for valueIndex in range(len (values)):
		adjIndex = valueIndex + 1
		ws.write(0, adjIndex, values[valueIndex])



	# ws.write(2, 2, xlwt.Formula("A3+B3"))

	wb.save(ouputFileName+".xls")




def setUpWorkBook():



	return 



# Takes a file name as a string
# Returns a list of strings of types
def inputTypes(filename):
	types = []
	try:
		file = codecs.open(filename)
	except IOError:
		print "You fucked up the file. I can't open it."
		sys.exit(0)

	for line in file:
		line = line.rstrip()
		types.append(line)
	file.close()
	return types

# Takes a file name as a string
# Returns a list of ints for values 
def inputValues(filename):
	values = []
	try:
		file = codecs.open(filename)
	except IOError:
		print "You fucked up the file. I can't open it."
		sys.exit(0)

	for line in file:
		line = line.rstrip()
		try:
			numValue = int(line)
		except ValueError:
			print "Badly formed input values."
			sys.exit(0)
		values.append(numValue)
	file.close()
	return values


#def populateExcelWithTable():





# automatically runs main method when script runs
if __name__ == "__main__":main()
