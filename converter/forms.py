from django import forms

class UploadPDFForm(forms.Form):
    pdf_file = forms.FileField()

class UploadWordForm(forms.Form):
    word_file = forms.FileField()

class UploadPPTForm(forms.Form):
    ppt_file = forms.FileField()
    
class UploadJPGForm(forms.Form):
    jpg_file = forms.FileField()
