from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import removessidForm
import os
from ast import literal_eval


def getssids(request):
    if request.user.is_authenticated:
        try:
            username = request.user.username
            os.system("SecureCRT.exe /Script C:\\webs\\mysite\\tempinfo\\" + username + "dir\\getSsid.py")
        except:
            pass
    return redirect('/removessid/')

@login_required(login_url='/login')
def removessidView(request):
    if request.user.is_authenticated:
        username = request.user.username
        f = open('C:\\webs\\mysite\\tempinfo\\'+ username +'dir\\ssidlist.txt', 'r')
        macs = f.readlines()
        f.close()
        for mac in macs:
            if "Last Updated:" in mac:
                time = mac
                break


        if request.method == 'POST':
            form = removessidForm(request.user,request.POST)

            if form.is_valid():
                ssids = form.cleaned_data["ssids"]
                f = open('C:\\webs\\mysite\\tempinfo\\'+ username +'dir\\removessid.txt', 'w+')
                f.write(ssids)
                f.close()
                if (ssids.split(',')) == ['']:
                    ssids = '0'
                else:
                    ssids = str(len(ssids.split(',')))


                # REMOVE SSID SCRIPT SPLASH PAGE
                try:
                    f = open('C:\\webs\\mysite\\tempinfo\\' + username + 'dir\\removessid.txt', 'r')
                    removessid = f.read()
                    f.close()
                    if len(removessid) > 0:
                        removessid = literal_eval(removessid)

                    f = open('C:\\webs\\mysite\\tempinfo\\' + username + 'dir\\ssidlist.txt', 'r')
                    ssidlist = f.readlines()
                    f.close()
                    rlist = []
                    for rssid in removessid:
                        for cssid in ssidlist:
                            if rssid in cssid[8:11]:
                                rlist.append(cssid[0:81])

                    if len(removessid) == len(rlist):
                        removessid = rlist
                    else:
                        rlist = []
                        for ssid in removessid:
                            rlist.append(ssid)
                        removessid = rlist
                except Exception as e:
                    print(e)

                open('C:\\webs\\mysite\\tempinfo\\' + username + 'dir\\removessidLIST.txt', 'w+').close()
                f = open('C:\\webs\\mysite\\tempinfo\\' + username + 'dir\\removessidLIST.txt', 'a+')

                for item in rlist:
                    f.write(str(item[8::].split('      ')[1])+'\n')
                f.close()


            else:
                pass
        else:
            form = removessidForm(request.user,request.GET)

        try:
            args = {'form':form, 'ssids':ssids, 'time' : time}
        except:
            try:
                args = {'form': form,'time': time}
            except:
                args = {'form': form}

        return render(request,'scripts/removessid.html',args)
