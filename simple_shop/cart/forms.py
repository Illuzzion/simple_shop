from django import forms


# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int,
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  label='Количество', initial=1)

    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    # class Meta:
    #     widgets = {
    #         'quantity': forms.Select(attrs={'class': 'form-control'})
    #     }
