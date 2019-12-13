import os

pdf_document = "input/9m-2019_IFRS_RUS.pdf"  

def print_pdf():
  print("123")
  from PyPDF2 import PdfFileReader
  
  with open(pdf_document, "rb") as filehandle:  
   pdf = PdfFileReader(filehandle)
   info = pdf.getDocumentInfo()
   pages = pdf.getNumPages()   
   print (info)
   print ("number of pages: %i" % pages)   
   page1 = pdf.getPage(5)
   print(page1)
   print(page1.extractText())

if __name__ == "__main__":
  print_pdf()