from django import forms

class UploadPDFForm(forms.Form):
    pdf_file = forms.FileField(label='Upload PDF')


class UploadWordForm(forms.Form):
    word_file = forms.FileField(label='Upload Word Document')
