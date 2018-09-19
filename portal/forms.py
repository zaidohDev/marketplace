from django import forms

from portal.models import Category


class ProductForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    slug = forms.SlugField(
        empty_value='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    category = forms.ModelMultipleChoiceField(label='Categorias', queryset=Category.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={
                                                      'class': 'form-control'
                                                  }
                                              )
                                              )

    quantity = forms.CharField(
        label='Quantidade',
        max_length=4,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    price = forms.CharField(
        label='Preço',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    short_description = forms.CharField(
        label='Descrição Curta',
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        label='Descrição',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )
