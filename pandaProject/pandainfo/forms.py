from django import forms
from .models import Upload


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ("name","file")

        