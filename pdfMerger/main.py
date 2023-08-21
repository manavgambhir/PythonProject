import PyPDF2

pdfiles = ["1.pdf","2.pdf"]
merge = PyPDF2.PdfMerger()
for filename in pdfiles:
        pdfFile = open(filename, 'rb')                  #rb- Read Binary Mode
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merge.append(pdfReader)
pdfFile.close()
merge.write('merged.pdf')