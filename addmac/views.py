from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import addmacForm


@login_required(login_url='/login')
def addmacView(request):

    if request.method == 'POST':
        form = addmacForm(request.POST)

        if form.is_valid():
            show = form.cleaned_data["show"]
            booth = form.cleaned_data["booth"]
            speed = form.cleaned_data["speed"]
            email = form.cleaned_data["email"]
            mac1 = form.cleaned_data["mac1"]
            mac2 = form.cleaned_data["mac2"]
            mac3 = form.cleaned_data["mac3"]
            mac4 = form.cleaned_data["mac4"]
            mac5 = form.cleaned_data["mac5"]
            mac6 = form.cleaned_data["mac6"]
            mac7 = form.cleaned_data["mac7"]
            mac8 = form.cleaned_data["mac8"]
            mac9 = form.cleaned_data["mac9"]
            mac10 = form.cleaned_data["mac10"]
            mac11 = form.cleaned_data["mac11"]
            mac12 = form.cleaned_data["mac12"]
            data = [show,booth,speed,email]
            macs = [mac1,mac2,mac3,mac4,mac5,mac6,mac7,mac8,mac9,mac10,mac11,mac12]
            print(data,"\n",macs)
            f = open('C:\\webs\\mysite\\tempinfo\\'+request.user.username+'dir\\addmac.txt','w+')
            f.write(str(data)+'\n'+str(macs).replace('-',':'))
            f.close()


        else:
            pass
    else:
        form = addmacForm()

    try:
        args = {'form': form, 'email': email}
    except:
        args = {'form': form,}

    return render(request,'scripts/addmac.html',args)

