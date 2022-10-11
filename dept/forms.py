from cProfile import label
from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Emf, Faculty, cn, emfdisplay, iot, ml, ws,cndisplay,iotdisplay,wsdisplay,mldisplay

class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ('Username','FirstName','LastName','Email','Password','header_image')
        labels = {
            'Username':'',
            'FirstName': '',
            'LastName':'',
            'Email':'',
            'Password':'',
        }
        widgets = {
            'Username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User name'}),
            'FirstName' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'}),
            'LastName' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last name'}),
            'Email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}),
            'Password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }


# class committeeForm(ModelForm):
#     class Meta:
#         model = committee
#         fields=('Username','Password')
#         widets = {
#             'Username': forms.TextInput(attrs={'class':'form-control'}),
#             'Password': forms.PasswordInput(attrs={'class':'form-control'}),
#         }

class EmfForm(ModelForm):
    class Meta:
        model = Emf
        fields = ('title','cie_image')


class emfdisplayForm(ModelForm):
    class Meta:
        model = emfdisplay
        fields = ('name', 'comments')

class cnForm(ModelForm):
    class Meta:
        model = cn
        fields = ('cn_title','cn_cie_image')

class cndisplayForm(ModelForm):
    class Meta:
        model = cndisplay
        fields = ('name', 'comments_cn')
        
class mlForm(ModelForm):
    class Meta:
        model = ml
        fields = ('ml_title','ml_cie_image')

class mldisplayForm(ModelForm):
    class Meta:
        model = mldisplay
        fields = ('name', 'comments_ml')

class wsForm(ModelForm):
    class Meta:
        model = ws
        fields = ('ws_title','ws_cie_image')

class wsdisplayForm(ModelForm):
    class Meta:
        model = wsdisplay
        fields = ('name', 'comments_ws')

class iotForm(ModelForm):
    class Meta:
        model = iot
        fields = ('iot_title','iot_cie_image')

class iotdisplayForm(ModelForm):
    class Meta:
        model = iotdisplay
        fields = ('name', 'comments_iot')