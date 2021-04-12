from django import forms
from .models import Puzzle, Category, Manufacturer
from django.forms.widgets import ClearableFileInput
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
"""
Definition of forms.
"""

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class MyClearableFileInput(ClearableFileInput):
    initial_text = 'Выбрано'
    input_text = 'Изменить'
    clear_checkbox_label = 'Удалить'

class PuzzleForm(forms.ModelForm):

    name = forms.CharField(label="Название")
    name.widget.attrs.update({'class' : 'form-control'})
        
    manufacturer = forms.IntegerField(label="Производитель")
    manufacturer.widget.attrs.update({'class' : 'form-control'})

    category = forms.IntegerField(label="Категория")
    category.widget.attrs.update({'class' : 'form-control'})

    number_of_details = forms.IntegerField(label="Количество деталей")
    number_of_details.widget.attrs.update({'class' : 'form-control'})

    age = forms.IntegerField(label="Рекомендуемый возраст")
    age.widget.attrs.update({'class' : 'form-control'})

    ifalldetails = forms.BooleanField(label="Все ли детали?", required=False, widget=forms.NullBooleanSelect)
    ifalldetails.widget.attrs.update({'class' : 'form-control'})

    imagepath = forms.ImageField(label = "Изображение", required=False, widget=MyClearableFileInput)
    imagepath.widget.attrs.update({'class' : 'form-control'})

    description = forms.CharField(label="Описание", widget=forms.Textarea, required=False)
    description.widget.attrs.update({'class' : 'form-control'})

    class Meta:
        model = Puzzle
        fields = ['manufacturer', 'name', 'category','number_of_details', 'age', 'ifalldetails', 'imagepath', 'description']
