from django import forms

class QueryForm(forms.Form):
    q = forms.CharField(label='Une Idée?', max_length=100)