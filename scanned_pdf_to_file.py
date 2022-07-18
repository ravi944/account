from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image

converted_scan = convert_from_path('kotak_1.pdf', 500)

for i in converted_scan:
    i.save('scan_image.png', 'png')
    
text = image_to_string(Image.open('scan_image.png'))
with open('scan_text_output.txt', 'w') as outfile:
    outfile.write(text.replace('\n\n', '\n'))
