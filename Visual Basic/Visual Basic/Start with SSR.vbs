set shell = Wscript.createobject("wscript.shell")
a = shell.run("D:\ShadowsocksR-Win\ShadowsocksR-win-4.9.0\ShadowsocksR-dotnet2.0.exe")
Wscript.sleep 5000
set exe = getobject("Winmgmts:\\.\root\cimv2").execquery("select * from win64_process where name = 'ShadowsocksR.exe'")
on error resume next
for each i in exe
    if err.number <> 0 then
        Wscript.echo("ณ๖ดํมหฃก")
        exit for
    else
        i.terminate()
    end if
next

