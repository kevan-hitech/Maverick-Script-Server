from django.shortcuts import render, redirect
from .forms import addssidForm
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')

def addssidView(request):

    if request.method == 'POST':
        form = addssidForm(request.POST)

        if form.is_valid():
            show = form.cleaned_data["show"]
            name = form.cleaned_data["name"]
            passw = form.cleaned_data["passw"]
            vlan = form.cleaned_data["vlan"]
            wid = form.cleaned_data["wid"]
            frequency = form.cleaned_data["frequency"]
            apgroups1 = form.cleaned_data["apgroups1"]
            apgroups2 = form.cleaned_data["apgroups2"]
            apgroups3 = form.cleaned_data["apgroups3"]
            apgroups4 = form.cleaned_data["apgroups4"]
            apgroups = apgroups1+apgroups2+apgroups3+apgroups4
            apgroups = apgroups.replace('][',', ')
            data = [show,name,passw,vlan,wid]
            frequency = [frequency]

            f = open('C:\\webs\\mysite\\tempinfo\\'+request.user.username+'dir\\addssid.txt','w+')
            f.write(str(data) + '\n' + str(frequency) + '\n' + str(apgroups))
            f.close()

        else:
            pass
    else:
        form = addssidForm()

    try:
        args = {'form':form,'passw':passw}
    except:
        args = {'form': form}

    return render(request,'scripts/addssid.html',args)
