# -*- coding: utf-8 -*-
"""
Formulário padrão para a entrada de dados.
"""

from django import forms


class InputDataForm(forms.Form):
    """
    Formulário padrão para a entrada de dados.
    """
    Arquivo = forms.FileField(
    )
