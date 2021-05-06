 do
    set bag=getobject("winmgmts:\\.\root\CIMV2")
    set pipe=bag.execquery("select * from win32_process where name='League of Legends.exe'") 
    '如果安的是64位的LOL，需要把win32_process改为win64_process
    on error resume next
    for Each i In pipe
        if err.number <> 0 then
            exit for
        else
            i.terminate()
        end if
    next
    wscript.sleep 1000
loop
