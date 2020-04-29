from django import forms

class QuerySmiles(forms.Form):
    smiles_str = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'smiles-input'}))
    thresh_hold = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'radio-inline', 'checked': ''}),
                                    choices=[('0.7', '0.7'), ('0.5', '0.5'), ('0.3', '0.3')])