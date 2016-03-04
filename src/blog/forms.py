from django import forms


from .models import Post

"""
user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
title = models.CharField(max_length=120)
slug = models.SlugField(unique=True)
image = models.FileField(upload_to=upload_location, 
        null=True, 
        blank=True, 
        # width_field="width_field", 
        # height_field="height_field"
        )
        
height_field = models.IntegerField(default=0)
width_field = models.IntegerField(default=0)
content = models.TextField()
draft = models.BooleanField(default=False)
publish = models.DateField(auto_now=False, auto_now_add=False)
updated = models.DateTimeField(auto_now=True, auto_now_add=False)
timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
"""

class PostModelForm(forms.ModelForm):
    #date_field = forms.DateField(initial="2010-11-20", widget=forms.SelectDateWidget(years=YEARS))
    class Meta:
        model = Post
        fields = [
            "user", 
            "title", 
            "slug", 
            "image"
            ]
        #exclude = ["height_field", "width_field"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        print title
        #raise forms.ValidationError("Nope!")
        return title





















SOME_CHOICES = [
        ('db-value', 'Display Value'),
        ('db-value2', 'Display Value2'),
        ('db-value3', 'Display Value3'),
    ]

INTS_CHOICES = [tuple([x,x]) for x in range(0, 102)]

YEARS = [x for x in range(1980, 2031)]

class TestForm(forms.Form):
    date_field = forms.DateField(initial="2010-11-20", widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label='Text', widget=forms.Textarea(attrs={"rows": 4, "cols": 10}))
    choices = forms.CharField(label='Text', widget=forms.Select(choices=SOME_CHOICES))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=101, widget=forms.Select(choices=INTS_CHOICES))
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
