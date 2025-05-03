from django.shortcuts import render
from django.http import FileResponse
from .forms import UploadPDFForm, UploadWordForm, UploadPPTForm
from .utils import convert_pdf_to_word, convert_word_to_pdf, convert_pdf_to_ppt, convert_ppt_to_pdf, convert_pdf_to_excel
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadJPGForm
from .utils import convert_jpg_to_pdf
import os

def home(request):
    return render(request, 'home.html')

def upload_pdf(request):
    docx_filename = None
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            # Save the file using FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(pdf_file.name, pdf_file)
            uploaded_file_path = fs.path(filename)
            
            # Convert the uploaded file (PDF to Word)
            docx_filename = convert_pdf_to_word(pdf_file)
            
            return render(request, 'upload.html', {
                'form': form,
                'docx_filename': docx_filename,
                'media_url': settings.MEDIA_URL
            })
    else:
        form = UploadPDFForm()

    return render(request, 'upload.html', {
        'form': form,
        'docx_filename': docx_filename,
    })

def upload_word(request):
    pdf_filename = None
    if request.method == 'POST':
        form = UploadWordForm(request.POST, request.FILES)
        if form.is_valid():
            word_file = request.FILES['word_file']
            # Save the file using FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(word_file.name, word_file)
            uploaded_file_path = fs.path(filename)
            
            # Convert the uploaded file (Word to PDF)
            pdf_filename = convert_word_to_pdf(word_file)
            
            return render(request, 'upload_word.html', {
                'form': form,
                'pdf_filename': pdf_filename,
                'media_url': settings.MEDIA_URL
            })
    else:
        form = UploadWordForm()

    return render(request, 'upload_word.html', {
        'form': form,
        'pdf_filename': pdf_filename,
    })

def upload_pdf_to_ppt(request):
    pptx_filename = None
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            pptx_filename = convert_pdf_to_ppt(pdf_file)
    else:
        form = UploadPDFForm()
    
    return render(request, 'upload_pdf_to_ppt.html', {
        'form': form,
        'pptx_filename': pptx_filename,
        'media_url': settings.MEDIA_URL
    })

def upload_ppt_to_pdf(request):
    pdf_filename = None
    if request.method == 'POST':
        form = UploadPPTForm(request.POST, request.FILES)
        if form.is_valid():
            ppt_file = request.FILES['ppt_file']
            # Convert the uploaded PowerPoint to PDF
            pdf_filename = convert_ppt_to_pdf(ppt_file)
            
            return render(request, 'upload_ppt_to_pdf.html', {
                'form': form,
                'pdf_filename': pdf_filename,
                'media_url': settings.MEDIA_URL
            })
    else:
        form = UploadPPTForm()

    return render(request, 'upload_ppt_to_pdf.html', {
        'form': form,
        'pdf_filename': pdf_filename,
    })

def upload_pdf_to_excel(request):
    excel_filename = None
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            # Convert the uploaded PDF to Excel
            excel_filename = convert_pdf_to_excel(pdf_file)
            
            return render(request, 'upload_pdf_to_excel.html', {
                'form': form,
                'excel_filename': excel_filename,
                'media_url': settings.MEDIA_URL
            })
    else:
        form = UploadPDFForm()

    return render(request, 'upload_pdf_to_excel.html', {
        'form': form,
        'excel_filename': excel_filename,
    })

def upload_jpg_to_pdf(request):
    pdf_filename = None
    if request.method == 'POST':
        form = UploadJPGForm(request.POST, request.FILES)
        if form.is_valid():
            jpg_file = request.FILES['jpg_file']
            # Convert the uploaded file (JPG to PDF)
            pdf_filename = convert_jpg_to_pdf(jpg_file)
    else:
        form = UploadJPGForm()

    return render(request, 'upload_jpg_to_pdf.html', {
        'form': form,
        'pdf_filename': pdf_filename,
        'media_url': settings.MEDIA_URL
    })

