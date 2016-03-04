from django import forms



class TestForm(forms.Form):
    some_text = forms.CharField()
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=101)
    email = forms.EmailField(min_length=10)

    def __init__(self, user=None, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        print(user)
        if user:
            self.fields["some_text"].initial = user.username

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer

    def clean_some_text(self, *args, **kwargs):
        some_text = self.cleaned_data.get("some_text")
        if len(some_text) < 5:
            raise forms.ValidationError("Ensure the text is greater than 5 characters")
        return some_text
