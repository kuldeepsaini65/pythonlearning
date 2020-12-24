from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def secure_pdf(file, passward):
    paser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        paser.addPage(pdf.getPage(page))
    paser.encrypt(passward)

    with open(f"encrypted_{file}", 'wb') as f:
        paser.write(f)
        f.close()
    print(f"Your New File Name Is :- encrypted_{file} \nPassward Attached....")


if __name__ == '__main__':
    os.chdir("C://Users//Kuldeep saini//Downloads")
    file = 'statics.pdf'
    passward = input("Please Enter Your Password For Pdf ---->")
    secure_pdf(file, passward)
