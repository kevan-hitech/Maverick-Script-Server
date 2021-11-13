from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import smtplib
import os, shutil
from django.contrib.auth import authenticate

class HomeForm(forms.Form):

    fname = forms.CharField(required=True,
                           error_messages={'required': 'Required Field'},
                           widget=forms.TextInput(),
    )
    lname = forms.CharField(required=True,
                           error_messages={'required': 'Required Field'},
                           widget=forms.TextInput(),
    )

    usern = forms.CharField(required=True,
                           error_messages={'required': 'Required Field'},
                           widget=forms.TextInput(),
    )
    passw = forms.CharField(required=True,
                           error_messages={'required': 'Required Field'},
                           widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super(HomeForm, self).clean()
        usern = cleaned_data.get('usern')
        passw = cleaned_data.get('passw')
        fname = cleaned_data.get('fname')
        lname = cleaned_data.get('lname')

        user = usern + '@javitscenter.com'
        password = passw
        smtpsrv = "smtp.office365.com"
        try:
            smtpserver = smtplib.SMTP(smtpsrv, 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(user, password)
            path = os.getcwd()
            print(path)
            smtpserver.close()
            os.mkdir(path+'\\tempinfo\\'+usern+'dir', 777)
            f = open(path+'\\tempinfo\\'+usern+'dir\\info.txt', 'w+')
            if usern == "kbasnayake":
                User.objects.create_superuser(usern, user, passw, first_name=fname, last_name=lname)
            else:
                User.objects.create_user(usern, user, passw, first_name=fname, last_name=lname)

            info = (usern+'\n'+'\n'+fname+'\n'+lname)
            f.write(info)
            f.close()
            f = open(path+'\\tempinfo\\'+usern+'dir\\maclist.txt', 'w+')
            f.write("Last Updated: 2001-01-01 12:00:00.000000")
            f.close()
            f = open(path + '\\tempinfo\\'+usern+'dir\\ssidlist.txt', 'w+')
            f.write("Last Updated: 2001-01-01 12:00:00.000000")
            f.close()

            scripts = ['addMac.py','addSsid.py','getMac.py','getSsid.py','removeMac.py','removeSsid.py']
            for script in scripts:
                source = 'C:\\webs\\mysite\\tempinfo\\admindir\\'+script
                destination = 'C:\\webs\\mysite\\tempinfo\\'+usern+'dir\\'+script
                shutil.copyfile(source, destination)

        except Exception as e:
            smtpserver.close()
            print('Reg error',e)
            raise ValidationError(e)

class LoginsForm(forms.Form):

    username = forms.CharField(required=True,
                           widget=forms.TextInput(),
    )
    password = forms.CharField(required=True,
                           widget=forms.PasswordInput()
    )

    def __init__(self, user, data=None):
        self.user = user
        super(LoginsForm, self).__init__(data=data)

    def clean(self):
        cleaned_data = super(LoginsForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            try:
                user = username + '@javitscenter.com'
                smtpsrv = "smtp.office365.com"
                smtpserver = smtplib.SMTP(smtpsrv, 587)
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo()
                smtpserver.login(user, password)
                path = os.getcwd()
                smtpserver.close()
                u = User.objects.get(username=username)
                u.set_password(password)
                u.save()
            except Exception as e:
                try: smtpserver.close()
                except: pass
                print('Reg error',e)
                raise ValidationError(e)
            try: smtpserver.close()
            except: pass
