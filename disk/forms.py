# -*- coding: utf-8 -*-
from django import forms


class FolderForm(forms.Form):
    """ Upload form """
    foldername = forms.CharField(max_length=100)
