from django import forms



class SearchForm(forms.Form):
    q = forms.CharField()
    q2 = forms.CharField()
    q3 = forms.CharField()
    q4 = forms.CharField()
    q5 = forms.CharField()


