from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class userregistration(UserCreationForm):
    #password1=forms.CharField(widget=forms.PasswordInput,label='Password')
    #password2=forms.CharField(widget=forms.PasswordInput,label='Re-Enter-Password')
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i,j in self.fields.items():
            j.help_text=None
class change_password(forms.Form):
    new_password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
class question_form(forms.Form):
    question=forms.CharField(label='question',max_length=255)
    option1=forms.CharField(label='option1',max_length=255)
    option2=forms.CharField(label='option2',max_length=255)
    option3=forms.CharField(label='option3',max_length=255)
    option4=forms.CharField(label='option4',max_length=255)
    correct_option=forms.ChoiceField(label='correct_option',choices=[(1,'option1'),(2,'option2'),(3,'option3'),(4,'option4')],widget=forms.RadioSelect)


        

