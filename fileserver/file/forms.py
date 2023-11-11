from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'original_filename']  
        widgets = {'original_filename': forms.HiddenInput()}  

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            self.cleaned_data['original_filename'] = file.name  
        return file

