from PyPDF2 import PdfFileWriter, PdfFileReader 
out = PdfFileWriter() 

file = PdfFileReader("axis_no_ifsc_ CARE886121926.pdf")  
password = "CARE886121926"
if file.isEncrypted: 

    file.decrypt(password) 

    for idx in range(file.numPages):  
        page = file.getPage(idx)  
        out.addPage(page) 
        
    with open("myfile_decrypted.pdf", "wb") as f: 
        out.write(f) 
    print("File decrypted Successfully.") 
else:  
    print("File already decrypted.")
