from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import scriptlogForm
import pyodbc

@login_required(login_url='login')
# Create your views here.


def scriptlogView(request):

    sqlconn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=nyccoc-sql-02;DATABASE=ShowDB;UID=ShowDBuser;PWD=zQ+GZ*[z!EtCXv5)')
    cur = sqlconn.cursor()

    sql = """select g.datetime
            , g.username
            , g.show
            , g.script
            , g.action
            , s.controllers
            , s.mac
            , s.speed
            , s.booth
            from dbo.global g
            inner join dbo.add_mac s on(g.action = s.action)
            join dbo.shows sh on g.show = cast(sh.name as varchar(50))
            where GETDATE() between dateadd(day, -999, sh.move_in) and dateadd(day, 999, sh.move_out) ORDER BY g.datetime"""

    cur.execute(sql)
    item = cur.fetchone()

    log_array = []
    while item is not None:
        item = (item[0],item[3],item[2],item[1],item[6].replace(',',', '),item[5],item[7],item[8])
        #print(item) #Add MAC
        log_array.append(item)
        item = cur.fetchone()

    sql = """select g.datetime
            , g.username
            , g.show
            , g.script
            , g.action
            , s.controllers
            , s.ap_groups
            , s.ssid
            , s.password
            , s.vlan
            from dbo.global g
            inner join dbo.add_ssid s on(g.action = s.action)
            join dbo.shows sh on g.show = cast(sh.name as varchar(50))
            where GETDATE() between dateadd(day, -999, sh.move_in) and dateadd(day, 999, sh.move_out) ORDER BY g.datetime"""
    cur.execute(sql)
    item = cur.fetchone()

    while item is not None:
        item = (item[0],item[3],item[2],item[1],item[6].replace(',',', '),item[5],item[9],item[7],item[8])
        #print(item) #Add SSID
        log_array.append(item)
        item = cur.fetchone()

    sql = """select g.datetime
            , g.username
            , g.show
            , g.script
            , g.action
            , s.mac
            from dbo.global g
            inner join dbo.remove_mac s on(g.action = s.action)"""
    cur.execute(sql)
    item = cur.fetchone()

    while item is not None:
        item = (item[0],item[3],item[2],item[1],item[5].replace(',',', '))
        #print(item) #Remove MAC
        log_array.append(item)
        item = cur.fetchone()

    sql = """select g.datetime
                , g.username
                , g.show
                , g.script
                , g.action
                , s.ssid
                from dbo.global g
                inner join dbo.remove_ssid s on(g.action = s.action)"""
    cur.execute(sql)
    item = cur.fetchone()

    while item is not None:
        item = (item[0],item[3],item[2],item[1],item[5].replace(',',', '))
        #print(item) #Remove SSID
        log_array.append(item)
        item = cur.fetchone()
    sqlconn.close()
    log_array = sorted(log_array, key=lambda dat: dat[0], reverse=True)

    cfile = log_array

# ----------------------------------------------------------------------------------------
# REQUEST.METHOD == "POST"
# ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------

    if request.method == 'POST':
        form = scriptlogForm(request.POST)
        if form.is_valid():
            show = form.cleaned_data["show"]
            date = form.cleaned_data["date"]
            script = form.cleaned_data["script"]
            user = form.cleaned_data["user"]

            sqlconn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=nyccoc-sql-02;DATABASE=ShowDB;UID=ShowDBuser;PWD=zQ+GZ*[z!EtCXv5)')
            cur = sqlconn.cursor()

            sql = """select g.datetime
                    , g.username
                    , g.show
                    , g.script
                    , g.action
                    , s.controllers
                    , s.mac
                    , s.speed
                    , s.booth
                    from dbo.global g
                    inner join dbo.add_mac s on(g.action = s.action)
                    join dbo.shows sh on g.show = cast(sh.name as varchar(50))
                    where GETDATE() between dateadd(day, -999, sh.move_in) and dateadd(day, 999, sh.move_out) ORDER BY g.datetime"""

            cur.execute(sql)
            item = cur.fetchone()

            log_array = []
            while item is not None:
                if script.lower() in str(item[3]).lower() and show.lower() in str(item[2]).lower() and user.lower() in str(item[1].lower()):
                    item = (item[0], item[3], item[2], item[1], item[6].replace(',',', '), item[5], item[7], item[8])
                    # print(item) #Add MAC
                    log_array.append(item)
                item = cur.fetchone()

            sql = """select g.datetime
                    , g.username
                    , g.show
                    , g.script
                    , g.action
                    , s.controllers
                    , s.ap_groups
                    , s.ssid
                    , s.password
                    , s.vlan
                    from dbo.global g
                    inner join dbo.add_ssid s on(g.action = s.action)
                    join dbo.shows sh on g.show = cast(sh.name as varchar(50))
                    where GETDATE() between dateadd(day, -999, sh.move_in) and dateadd(day, 999, sh.move_out) ORDER BY g.datetime"""
            cur.execute(sql)
            item = cur.fetchone()

            while item is not None:
                if script.lower() in str(item[3]).lower() and show.lower() in str(item[2]).lower() and user.lower() in str(item[1].lower()):
                    item = (item[0],item[3],item[2],item[1],item[6].replace(',',', '),item[5],item[9],item[7],item[8])
                    # print(item) #Add SSID
                    log_array.append(item)
                item = cur.fetchone()

            sql = """select g.datetime
                    , g.username
                    , g.show
                    , g.script
                    , g.action
                    , s.mac
                    from dbo.global g
                    inner join dbo.remove_mac s on(g.action = s.action)"""
            cur.execute(sql)
            item = cur.fetchone()

            while item is not None:
                if script.lower() in str(item[3]).lower() and show.lower() in str(item[2]).lower() and user.lower() in str(item[1].lower()):
                    item = (item[0], item[3], item[2], item[1], item[5].replace(',',', '))
                    # print(item) #Remove MAC
                    log_array.append(item)
                item = cur.fetchone()

            sql = """select g.datetime
                        , g.username
                        , g.show
                        , g.script
                        , g.action
                        , s.ssid
                        from dbo.global g
                        inner join dbo.remove_ssid s on(g.action = s.action)"""
            cur.execute(sql)
            item = cur.fetchone()

            while item is not None:
                if script.lower() in str(item[3]).lower() and show.lower() in str(item[2]).lower() and user.lower() in str(item[1].lower()):
                    item = (item[0], item[3], item[2], item[1], item[5].replace(',',', '))
                    # print(item) #Remove SSID
                    log_array.append(item)
                item = cur.fetchone()

            sqlconn.close()
            log_array = sorted(log_array, key=lambda dat: dat[0], reverse=True)

            cfile = log_array
        else:
            pass


    else:
        form = scriptlogForm()

    try:
        args = {'form':form,'cfile':cfile,'script':script}
    except:
        args = {'form': form, 'cfile': cfile}

    return render(request,'scripts/scriptlog.html',args)
