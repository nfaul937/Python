from PyPDF2 import PdfFileReader, PdfFileWriter
import xlrd

infile = PdfFileReader(open("BillingForms.pdf", "rb"))

#Number of pages in input PDF file
pageCount = infile.numPages
print ('\nPage Count: ' + str(pageCount))

#Minimum run count(assuming number of pages is even)
runCount = pageCount / 2
print ('Run Count:  ' + str(runCount) + '\n')

#Initilize page numbers
pnum1 = 0
pnum2 = 1

workbook = xlrd.open_workbook('Spreadsheet.xlsx')
worksheet = workbook.sheet_by_name('Billing')

for i in range(0,int(runCount)):
	#Getting Server Name for file naming purposes
	value = worksheet.cell(i + 1,1).value
	print ('Run ' + str(i + 1) + ' out of ' + str(runCount))
	
	print ('Page '+ str(pnum1))
	print ('Page '+ str(pnum2))

	print ('Getting pages...\n')
	page1 = infile.getPage(pnum1)
	page2 = infile.getPage(pnum2)
	
	#Increment page numbers
	pnum1 = pnum1 + 2
	pnum2 = pnum2 + 2
	
	#Create PDF writer object
	outfile = PdfFileWriter()
	
	print ('Adding pages...\n')
	outfile.addPage(page1)
	outfile.addPage(page2)
	
	outputStream = open(r"vm-" + str(value) + ".pdf", "wb")
	outfile.write(outputStream)
	print(str(value))
	
	
#Close output stream
outputStream.close
