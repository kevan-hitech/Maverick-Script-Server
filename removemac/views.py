from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import removemacForm
import os


def getmacs(request):
    if request.user.is_authenticated:
        try:
            username = request.user.username
            os.system("SecureCRT.exe /Script C:\\webs\\mysite\\tempinfo\\" + username + "dir\\getMac.py")
        except:
            pass
    return redirect('removemac/')



@login_required(login_url='/login')

def removemacView(request):
    username = request.user.username
    f = open('C:\\webs\\mysite\\tempinfo\\'+username+'dir\\maclist.txt', 'r')
    macs = f.readlines()
    f.close()
    for mac in macs:
        if "Last Updated:" in mac:
            time = mac
            break

    if request.method == 'POST':
        form = removemacForm(request.user,request.POST)
        if form.is_valid():
            macs = form.cleaned_data["macs"]

            f = open('C:\\webs\\mysite\\tempinfo\\'+username+'dir\\removemac.txt', 'w+')
            f.write(macs.replace('-',':'))
            f.close()

            if (macs.split(',')) == ['']:
                macs = '0'
            else:
                macs = str(len(macs.split(',')))
        else:
            pass
    else:
        form = removemacForm(request.user)
    try:
        args = {'form':form,'macs':macs, 'time':time}
    except:
        try:
            args = {'form': form, 'time': time}
        except:
            args = {'form': form}

    return render(request,'scripts/removemac.html',args)
