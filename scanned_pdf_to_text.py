import pytesseract
from pdf2image import convert_from_path
import glob

pdfs = glob.glob(r"bharat_co_bank-pdfdoctor_com.pdf")
for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500)
    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='eng')
        print(text)
