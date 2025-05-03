import os
import subprocess
from pdf2docx import Converter
from pdf2image import convert_from_path
from pptx import Presentation
from pptx.util import Inches
from django.conf import settings

# Convert PDF to Word
def convert_pdf_to_word(pdf_file):
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_file.name)

    # Save the uploaded PDF file to disk
    with open(pdf_path, 'wb+') as destination:
        for chunk in pdf_file.chunks():
            destination.write(chunk)

    # Define the output path for the .docx file
    docx_path = pdf_path.replace('.pdf', '.docx')

    # Convert the PDF to Word
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

    return os.path.basename(docx_path)

# Convert Word to PDF (Linux-compatible using LibreOffice)
def convert_word_to_pdf(word_file):
    word_path = os.path.join(settings.MEDIA_ROOT, word_file.name)

    # Save the uploaded Word file to disk
    with open(word_path, 'wb+') as destination:
        for chunk in word_file.chunks():
            destination.write(chunk)

    # Use LibreOffice to convert Word to PDF
    try:
        subprocess.run([
            "libreoffice",
            "--headless",
            "--convert-to", "pdf",
            word_path,
            "--outdir", settings.MEDIA_ROOT
        ], check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("Conversion failed: " + str(e))

    # Get the output filename
    pdf_filename = word_file.name.replace('.docx', '.pdf')
    return pdf_filename



def convert_pdf_to_ppt(pdf_file):
    # Save PDF to disk
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_file.name)
    with open(pdf_path, 'wb+') as destination:
        for chunk in pdf_file.chunks():
            destination.write(chunk)

    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Create PowerPoint
    prs = Presentation()
    blank_slide_layout = prs.slide_layouts[6]  # Blank layout

    for image in images:
        slide = prs.slides.add_slide(blank_slide_layout)
        img_path = pdf_path.replace('.pdf', '_temp.jpg')
        image.save(img_path, 'JPEG')
        slide.shapes.add_picture(img_path, Inches(0), Inches(0),
                                 width=prs.slide_width,
                                 height=prs.slide_height)

    pptx_filename = pdf_file.name.replace('.pdf', '.pptx')
    pptx_path = os.path.join(settings.MEDIA_ROOT, pptx_filename)
    prs.save(pptx_path)

    return os.path.basename(pptx_path)
