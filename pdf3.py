import fitz
my_pdf=r"SamplePdf_477kb_1page.pdf"
doc = fitz.open(my_pdf)
def pdftype(doc):
    i=0
    for page in doc:
        if len(page.get_text())>0:
            i+=1
    if i>0:
        print("its partial pdf")
    else:
        print("its scanned pdf")
pdftype(doc)
