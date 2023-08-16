from PyPDF2 import PdfWriter

merge = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merge.append(pdf)

merge.write("merged-pdf.pdf")
merge.close()