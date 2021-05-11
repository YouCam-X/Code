import keyboard
import time


bookinformation = []
bookinformation_number = 0

class Menu:
    #用于创建菜单界面
    def showmenu(self):
        while True:
            print('''欢迎来到图书管理系统,请按下对应的数字键选择功能：
                                 添加图书 —— 1
                                 查询图书 —— 2
                                 借阅\归还图书 —— 3
                                 删除图书 —— 4
                                 修改书籍信息 —— 5
                                 显示所有书籍 —— 6
                                 退出系统 —— 7''')
        
            while True:
                if keyboard.is_pressed('1'):
                    buffer = input('请忽略本条信息，按回车键继续')
                    # buffer 的作用是为了解决按下 数字键 1 后会将1这个字符代入到后面的input()当中的冲突
                    Bookmanager.addbooks(self)
                    break

                elif keyboard.is_pressed('2'):
                    buffer = input('请忽略本条信息，按回车键继续')
                    Bookmanager.searchbooks(self)
                    break
                
                elif keyboard.is_pressed('3'):
                    buffer = input('请忽略本条信息，按回车键继续')
                    Bookmanager.borrow_return_books(self)
                    break

                elif keyboard.is_pressed('4'):
                    buffer = input('请忽略本条信息，按回车键继续')
                    Bookmanager.deletebooks(self)
                    break

                elif keyboard.is_pressed('5'):
                    buffer = input('请忽略本条信息，按回车键继续')
                    Bookmanager.editbooks(self)
                    break

                elif keyboard.is_pressed('6'):
                    buffer = input('请忽略本条信息，按回车键继续')
                    Bookmanager.showallbooks(self)
                    break

                elif keyboard.is_pressed('7'):
                    return

                else:
                    continue

class Bookmanager:
    
    def save(self):
        file = open('Bookinformation.txt','a+') 
        #因为要添加图书，所以用 a+ 方式打开， 也可以用 r+，但是指针的位置不一样，可能会影响后面的代码
        # w+ 的话就直接覆盖了，所以不行

        for book in bookinformation:
            for i in book:
                file.write(i)
                file.write('\t')
            file.write('\n')
        file.close()

    #一开始的思路是，一次连续输入所有信息，用tab键分隔，但是觉得麻烦
    #def addbooks(self):
    #    global bookinformation_number 
    #    global bookinformation

    #    while true:

    #            information = input('请依次输入书的名字、作者、类型、添加日期，以及备注（请用tab分隔不同的信息）\n')
    #            information += '\t'
    #            information_mediator = []
    #            one_information = ''
    #            information_array = []
    #            whether_to_execute = 0

    #            for i in information:
    #                if i == '\t':
    #                    whether_to_execute += 1

    #            if whether_to_execute >= 5:
    #                for character in information:

    #                    if character.encode() == '\t'.encode():
    #                        for character in information_mediator:
    #                            one_information += character
    #                        if one_information != '':
    #                            information_array.append(one_information)
    #                        one_information = ''
    #                        information_mediator = []

    #                    else:
    #                        information_mediator.append(character)

    #                name = information_array[0]
    #                author = information_array[1]
    #                genre = information_array[2]
    #                add_date = information_array[3]
    #                marker = information_array[4]

    #                del information_array[5:]

    #                bookinformation.append(information_array)
    #                bookinformation_number += 1

    #                print('''成功添加图书
    #                            新书名字是 %s
    #                            作者是 %s
    #                            类型是 %s
    #                            添加日期是 %s
    #                            备注是 %s'''%(name,author,genre,add_date,marker))

    #                print('如添加有误，请按f键；正确请按j键') 
                    
    #                while true:
    #                    if keyboard.is_pressed('f'):
    #                        del bookinformation[bookinformation_number-1]
    #                        print('已删除此信息，开始重新添加')
    #                        bookinformation_number -= 1
    #                        break

    #                    elif keyboard.is_pressed('j'):
    #                        break

    #                    else:
    #                        continue

    #                time.sleep(0.2)

    #                print('继续添加图书信息请按f键，退出请按j键')         
    #                while true:
    #                    if keyboard.is_pressed('f'):
    #                        break

    #                    elif keyboard.is_pressed('j'):
    #                        bookmanager.save(self)
    #                        bookinformation = []
    #                        bookinformation_number = 0
    #                        return

    #                    else:
    #                        continue

    #            else:   
    #                print('您的输入不完全或者有误，请重新输入')
    
    #            buffer = input('请忽略本行内容，继续敲击回车键')


    def addbooks(self):

        global bookinformation
        global bookinformation_number

        bookinformation_number = 0
        bookinformation = []

        while True:
            bookinformation_mediator = []

            name = input('请输入书名：')
            author = input('请输入作者：')
            genre = input('请输入所属类型：')
            marker = input('请输入备注：')
            date = time.strftime("%Y-%m-%d",time.localtime())
            #自动获取当天的日期，并添加至列表内
            availability = '可借阅'
            #默认的可用性是 可借阅

            bookinformation_mediator.append(name)
            bookinformation_mediator.append(author)
            bookinformation_mediator.append(genre)
            bookinformation_mediator.append(date)
            bookinformation_mediator.append(marker)
            bookinformation_mediator.append(availability)
            bookinformation.append(bookinformation_mediator)
            bookinformation_number += 1
            #bookinformation_number 在后面的添加有误后，删除的时候用到

            print('''添加成功！
                     书名是：%s
                     作者是：%s
                     题材是：%s
                     备注是：%s
                     添加日期是：%s'''%(name,author,genre,marker,date))


            keyboard.wait('enter',True,True)
            #这里的wait()是为了抵消上一个input()输入完成后按的回车键，不然会连着执行下面的 is_pressed('enter')的命令

            print('如添加的信息有误，请按Esc键，确认添加请按Enter键')


            #用 While True 死循环监测键盘输入
            while True:
                if keyboard.is_pressed('esc'):
                    del bookinformation[bookinformation_number-1]
                    print('此书信息已删除，请重新添加')
                    bookinformation_number -= 1
                    #删除之后要记得值减一
                    keyboard.wait('esc',True,True)
                    #wait()同理
                    break
                
                elif keyboard.is_pressed('enter'):
                    buffer = input('')
                    keyboard.wait('enter',True,True)
                    break

                else:
                    continue


            print('继续添加请按Enter键，退出请按Esc键')


            while True:
                if keyboard.is_pressed('enter'):
                    buffer = input('')
                    break

                elif keyboard.is_pressed('esc'):
                    Bookmanager.save(self)
                    bookinformation = []
                    bookinformation_number = 0
                    #退出前面要记得初始化两个变量
                    return

                else:
                    continue


    def searchbooks(self):
        global bookinformation

        while True:
            #初始化变量以防上次循环的变量也被拉进来
            bookinformation = []
            search_number = 0

            information_mediator = []
            one_information_item = ''
            file = open('Bookinformation.txt', 'r')
            #因为只是搜素书籍信息，所以不需要改动txt文件，用 r 方式打开就好
            book_list = file.readlines()
            # readlines()函数可以一行一行地读，并返回列表

            for i in book_list:
                for each_character in i:
                    if each_character == '\t' or each_character == '\n':
                        #保存的时候是用了Tab键来分隔不同的信息，用换行符来区分不同的书籍
                        if one_information_item != '' and one_information_item != '\n':
                            #防止将空字符串添加进列表
                            information_mediator.append(one_information_item)
                            one_information_item = ''
                            #添加完后需要初始化变量
                    else:
                        one_information_item += each_character

                bookinformation.append(information_mediator)
                information_mediator = []


            keywords = input('请输入需要查找的书名或者关键字\n')

            #这里搜索功能只能搜索到完全一样的关键字，编程能力不行，真希望可以像百度、谷歌那样

            for book in bookinformation:
                for i in book:
                    if i == keywords:
                        search_number += 1

                        print('''第%s本符合结果的书：
                                 书名：%s
                                 作者：%s
                                 类型：%s
                                 添加日期：%s
                                 备注：%s
                                 可用性：%s'''%(str(search_number),book[0],book[1],book[2],book[3],book[4],book[5]))
                        break
            
            if search_number == 0:
                print("找遍了也找不到这本书")

            print('是否继续查找，继续请按Enter键，退出查找请按Esc键')

            keyboard.wait('enter',True,True)

            while True:
                if keyboard.is_pressed('enter'):
                    break

                elif keyboard.is_pressed('esc'):
                    bookinformation = []
                    return
                    
                else:
                    continue
            
            buffer = input('')
            keyboard.wait('enter',True,True)

    def editbooks(self):

        global bookinformation

        while True:
            locate_number_list = []
            search_number = 0
            bookinformation = Bookmanager.get_bookinformation(self)
            
            keywords = input('请输入需要修改的书的关键字')
            keyboard.wait('enter',True,True)

            for book in bookinformation:
                
                for i in book:

                    if i == keywords:

                        search_number += 1
                        locate_number_list.append(book[6])

                        print('''第%s本符合结果的书：
                                 书名：%s
                                 作者：%s
                                 类型：%s
                                 添加日期：%s
                                 备注：%s
                                 可用性：%s'''%(str(search_number),book[0],book[1],book[2],book[3],book[4],book[5]))
                    
            if search_number == 0:

                print('没有找到这本书，请按Enter重新搜索。或者按Esc键退出')

                while True:

                    if keyboard.is_pressed('esc'):
                        keyboard.wait('esc',True,True)
                        return
                    
                    elif keyboard.is_pressed('enter'):
                        keyboard.wait('enter',True,True)
                        break

                    else:
                        continue

                continue

            book_number = Bookmanager.if_integer_is_valid(self)

            try:
                locate_book_number = locate_number_list[int(book_number)-1]
                book_mediator = bookinformation[int(locate_book_number)]

                availability = book_mediator[5]

                print('''确定要修改这本书吗？确定请按Enter键，取消请按Esc键。
                         书名：%s
                         作者：%s
                         类型：%s
                         添加日期：%s
                         备注：%s
                         可用性：%s'''%(book_mediator[0],book_mediator[1],book_mediator[2],book_mediator[3],book_mediator[4],book_mediator[5]))
                 

                while True:

                    if keyboard.is_pressed('enter'):

                        print('请重新输入信息：')

                        buffer = input('')

                        name = input('请输入书名：')
                        author = input('请输入作者：')
                        genre = input('请输入所属类型：')
                        marker = input('请输入备注：')
                        date = time.strftime("%Y-%m-%d",time.localtime())
                        
                        keyboard.wait('enter',True,True)

                        book_mediator = []
                        book_mediator.append(name)
                        book_mediator.append(author)
                        book_mediator.append(genre)
                        book_mediator.append(date)
                        book_mediator.append(marker)
                        book_mediator.append(availability)
                        book_mediator.append(str(locate_book_number))

                        del bookinformation[int(locate_book_number)]
                        bookinformation.insert(int(locate_book_number),book_mediator)

                        print('''修改完毕：
                                 新书名：%s
                                 新作者：%s
                                 新类型：%s
                                 新添加/修改日期：%s
                                 新备注：%s
                                 可用性：%s'''%(bookinformation[int(locate_book_number)][0],bookinformation[int(locate_book_number)][1],bookinformation[int(locate_book_number)][2],bookinformation[int(locate_book_number)][3],bookinformation[int(locate_book_number)][4],bookinformation[int(locate_book_number)][5]))

                        #修改完毕后就立即保存文件，可以避免一些Bugs
                        file = open('Bookinformation.txt','w+')

                        for book in bookinformation:
                            for i in book[:6]:
                                file.write(i)
                                file.write('\t')
                            file.write('\n')

                        file.close()

                        boobookinformation = []

                        break

                    elif keyboard.is_pressed('esc'):
                        keyboard.wait('esc',True,True)
                        bookinformation = []
                        break

                    else:
                        continue

            except:
                print('出错了！请输入正确的数字')
            
            print('继续修改请按Enter键，返回到主菜单请按Esc键')

            while True:

                if keyboard.is_pressed('enter'):
                    buffer = input('')
                    break

                elif keyboard.is_pressed('esc'):
                    return

                else:
                    continue

    def deletebooks(self):
        global bookinformation

        while True:
            locate_number_list = []
            search_number = 0
            bookinformation = Bookmanager.get_bookinformation(self)
            keywords = input('请输入需要删除的书的关键字')
            keyboard.wait('enter',True,True)

            for book in bookinformation:
                
                for i in book:

                    if i == keywords:

                        search_number += 1
                        locate_number_list.append(book[6])

                        print('''第%s本符合结果的书：
                                 书名：%s
                                 作者：%s
                                 类型：%s
                                 添加日期：%s
                                 备注：%s
                                 可用性：%s'''%(str(search_number),book[0],book[1],book[2],book[3],book[4],book[5]))
                    
            if search_number == 0:

                print('没有找到这本书，请按Enter重新搜索。或者按Esc键退出')

                while True:

                    if keyboard.is_pressed('esc'):
                        keyboard.wait('esc',True,True)
                        return
                    
                    elif keyboard.is_pressed('enter'):
                        keyboard.wait('enter',True,True)
                        break

                    else:
                        continue

                continue

            book_number = Bookmanager.if_integer_is_valid(self)

            try:

                book = bookinformation[int(locate_number_list[int(book_number)-1])]

                print('''确定要删除这本书吗？确定请按Enter键，取消请按Esc键
                          书名：%s
                          作者：%s
                          类型：%s
                          添加日期：%s
                          备注：%s
                          可用性：%s'''%(book[0],book[1],book[2],book[3],book[4],book[5]))
               
                while True:

                    if keyboard.is_pressed('enter'):
                        del bookinformation[int(locate_number_list[int(book_number)-1])]
                        file = open('Bookinformation.txt','w+')

                        for book in bookinformation:
                            for i in book[:6]:
                                file.write(i)
                                file.write('\t')
                            file.write('\n')
                        
                        file.close()

                        #删除后就立即保存

                        print('已成功删除！')
                        keyboard.wait('enter',True,True)
                        break

                    elif keyboard.is_pressed('esc'):
                        keyboard.wait('esc',True,True)
                        break

                    else:
                        continue

            except:
                print('请输入正确的数字！')

            print('继续删除请按Enter键，返回主菜单请按Esc键')


            while True:

                if keyboard.is_pressed('enter'):
                    keyboard.wait('enter',True,True)
                    break

                elif keyboard.is_pressed('esc'):
                    return

                else:
                    continue

    def borrow_return_books(self):
        global bookinformation

        while True:

            #循环运行每一次都要在开头初始化变量，以防对本次运行造成影响

            bookinformation = Bookmanager.get_bookinformation(self)
            search_number = 0
            locate_number_list = []

            keywords = input('请输入需要借阅/归还的书的关键字')
            keyboard.wait('enter',True,True)

            for book in bookinformation:
                for i in book:

                    if i == keywords:
                        search_number += 1
                        locate_number_list.append(book[6])

                        print('''符合条件的第%s本书：
                                 书名：%s
                                 作者：%s
                                 类型：%s
                                 添加日期：%s
                                 备注：%s
                                 可用性：%s'''%(str(search_number),book[0],book[1],book[2],book[3],book[4],book[5]))
                        break

            if search_number == 0:
                        
                print('找遍了也没找到！请按Enter键重新搜素，或者按Esc返回主菜单')

                while True:

                    if keyboard.is_pressed('enter'):
                        keyboard.wait('enter',True,True)
                        break
                    
                    elif keyboard.is_pressed('esc'):
                        return

                    else:
                        continue

            else:
                book_number = Bookmanager.if_integer_is_valid(self)

                try:
                    book = bookinformation[int(locate_number_list[int(book_number)-1])]

                    print('借阅此书请按Enter键，归还请按Esc键')

                    while True:

                        if keyboard.is_pressed('enter'):
                            keyboard.wait('enter',True,True)

                            #用条件句解决借阅归还时可能会出现的bugs

                            if book[5] == '可借阅':
                                print('借阅成功！')
                                del bookinformation[int(locate_number_list[int(book_number)-1])][5]
                                bookinformation[int(locate_number_list[int(book_number)-1])].insert(5,'已借出')

                                #同样借出去后需要修改可用性为已借出，并写在文件里

                                file = open('Bookinformation.txt','w')

                                for book in bookinformation:
                                    for i in book[:6]:

                                        file.write(i)
                                        file.write('\t')
                                    file.write('\n')

                                file.close()
                                break

                            else:
                                print('此书已被借走，无法借阅')
                                break

                        elif keyboard.is_pressed('esc'):
                            keyboard.wait('esc',True,True)

                            if book[5] == '已借出':
                                print('归还成功！')
                                del bookinformation[int(locate_number_list[int(book_number)-1])][5]
                                bookinformation[int(locate_number_list[int(book_number)-1])].insert(5,'可借阅')

                                file = open('Bookinformation.txt','w')

                                for book in bookinformation:
                                    for i in book[:6]:

                                        file.write(i)
                                        file.write('\t')
                                    file.write('\n')

                                file.close()
                                break

                            else:
                                print('此书还在库中，无需归还')
                                break

                        else:
                            continue

                except:
                    print('请输入正确的数字！')

                print('重新搜素请按Enter键，返回主菜单请按Esc键')

                while True:

                    if keyboard.is_pressed('enter'):
                        keyboard.wait('enter',True,True)
                        break

                    elif keyboard.is_pressed('esc'):
                        return

                    else:
                        continue

    def showallbooks(self):
        global bookinformation

        bookinformation = []
        search_number = 0
        bookinformation = Bookmanager.get_bookinformation(self)

        print('\n以下是在数据库里的全部书籍：\n')

        for book in bookinformation:

            search_number += 1

            print('''第%s本书：
                        书名：%s
                        作者：%s
                        类型：%s
                        添加日期：%s
                        备注：%s
                        可用性：%s \n'''%(str(search_number),book[0],book[1],book[2],book[3],book[4],book[5]))
        
        return
    

    #写了一个函数用来执行经常用到的功能，就不用一遍一遍地重复写相同的代码了
    def get_bookinformation(self):
        global bookinformation

        bookinformation = []
        search_number = 0
        locate_number = 0
        information_mediator = []
        one_information_item = ''

        file = open('Bookinformation.txt', 'r')
        book_list = file.readlines()
        file.close()

        for i in book_list:

            for each_character in i:

                if each_character == '\t':

                    if one_information_item != '' and one_information_item != '\n':

                        information_mediator.append(one_information_item)
                        one_information_item = ''

                elif each_character == '\n':
                    one_information_item = ''
                    information_mediator.append(str(locate_number))
                    #这里会将每一行的行号写入列表中，后面会用得到
                    locate_number += 1
                    break

                else:
                    one_information_item += each_character
                
            bookinformation.append(information_mediator)
            information_mediator = []
        
        #程序只需要bookinformation这个数组就行，其他的变量作为局部变量就可以
        return bookinformation
    

    #这个函数用来判断输入的序号合不合法
    def if_integer_is_valid(self):

        book_number = input('请问需要对第几本书进行操作？输入数字即可')

        while not str.isdigit(book_number):
            print('请确保输入的是整数序号')
            book_number = input('请问需要对第几本书进行操作？输入数字即可')

        while int(book_number) != float(book_number):
            print('请确保输入的是整数序号')
            book_number = input('请问需要对第几本书进行操作？输入数字即可')

        keyboard.wait('enter',True,True)

        return book_number

main = Menu()
main.showmenu()