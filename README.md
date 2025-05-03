# File-Converter

A Django web application that supports file conversions between the following formats:

-> PDF to Word
-> Word to PDF
-> PDF to PowerPoint
-> PowerPoint to PDF
-> PDF to Excel
-> JPG to PDF

# Features

- Easy-to-use web interface
- Convert between multiple file formats (PDF, Word, PowerPoint, Excel, JPG)
- Simple file upload and download functionality

# Requirements

->  Python 3.x
->  Django
->  Django REST framework (for API functionality)
-> 'python-docx' (for Word to PDF, PDF to Word conversion)
-> `python-pptx' (for PowerPoint conversion)
-> `PyPDF2' (for PDF manipulation)
-> 'xlrd', `openpyxl' (for PDF to Excel conversion)
-> `Pillow' (for JPG to PDF conversion)



# set up the database
python3 manage.py migrate

# Run the Development Server
python3 manage.py runserver