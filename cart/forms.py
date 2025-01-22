from django import forms 
PROD=[(i,str(i)) for i in range(15)]
class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(coerce=int,choices=PROD)
    override=forms.BooleanField(required=False,
                                initial=False,widget=forms.HiddenInput)