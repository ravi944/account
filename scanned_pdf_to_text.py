from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
converted_scan = convert_from_path('bank-statement-template-11-converted.pdf', 500)
for i in converted_scan:
    i.save('scan_image.png', 'png')
text = image_to_string(Image.open('scan_image.png'))
print(text)
