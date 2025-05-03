from django.shortcuts import render
from .forms import UploadPDFForm, UploadWordForm
from .utils import convert_pdf_to_word, convert_word_to_pdf
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .utils import convert_pdf_to_ppt

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
    