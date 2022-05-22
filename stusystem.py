

import os
filename = 'student.txt'
def main():
    while True:
        menm()
        choice = int(input('请选择:'))
        if choice in range(8):
            if choice==0:
                answer=input('您确定要退出系统吗？y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()


def menm():
    print('=====================学生信息管理系统==========================')
    print('--------------------------功能菜单----------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('------------------------------------------------------------')

def insert():
    student_list = []
    while True:
        id = (input('请输入ID(如1001):'))
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩'))
            java = int(input('请输入java成绩'))
        except:
            print("输入无效，不是整数类型，请重新输入")
            continue

        #将学生信息保存到字典中
        student={'id':id, 'name':name, 'english':english, 'python':python, 'java':java}
        student_list.append(student)
        ans = input('是否继续添加？y/n')
        if ans=='y' or ans=='Y':
            continue
        else:
            break

    #保存学生信息
    save(student_list)
    print('学生信息录入完毕！！！')

def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
       # print(item)
        stu_txt.write(str(item)+'\n')
    stu_txt.close()


def search():
    stu_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生ID：')
            elif mode =='2':
                name = input('请输入学生姓名：')
            else:
                print("您的输入有误，请重新输入")
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            stu_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            stu_query.append(d)

            #显示查询结果
            show_student(stu_query)

            #清空列表
            stu_query.clear()
            ans = input('是否要继续查询？y/n：')
            if ans == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return




def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示！！！')
        return

    #定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'java成绩', '总成绩'))

    #定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        # print(item)
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java')),

        ))


def delete():
    while True:
        stu_id = input('请输入要删除的学生的ID:')
        if stu_id!='':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    stu_old = file.readlines()
                    # print(f'读文件:{stu_old}')
            else:
                stu_old = []
            flag = False
            if stu_old:
                # print(f'if读文件:{stu_old}')
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in stu_old:
                        # print(f"遍历读取出来的文件{item}")
                        d = dict(eval(item))
                        # print(d)
                        if d['id']!=stu_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id:{stu_id}的学生信息已被删除')
                    else:
                        print(f'id:{stu_id}的学生信息找不到')
            else:
                print('磁盘上无学生信息文件')
                break   #？多余的？
            # show()
            ans = input('是否继续删除y/n:')
            if ans == 'y':
                continue
            else:
                break;

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            stu_old = rfile.readlines()
    else:
        print('无学生信息文件，无法修改')
        return

    stu_id = input('请输入要修改学员的ID:')
    with open(filename,'w', encoding='utf-8') as wfile:
        for item in stu_old:
            d = dict(eval(item))
            if d['id'] == stu_id:
                print('找到学生信息，可以修改他的相关信息了!')
                while True:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['english'] = input('请输入英语成绩:')
                        d['python'] = input('请输入python成绩:')
                        d['java'] = input('请输入java成绩:')
                    except:
                        print('您输入信息有误，请重新输入！！！')
                    else:
                        break

                wfile.write(str(d) + '\n')
                print('修改成功！！！')
            else:
                wfile.write(str(d) + '\n')

        ans = input('是否继续修改其他学生的信息y/n:')
        if ans == 'y':
            modify()
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
        stu_new=[]
        for item in students:
            d = dict(eval(item))
            stu_new.append(d)
    else:
        return

    asc_or_desc = input('请选择(0.升序  1.降序):')
    if asc_or_desc=='0':
        asc_or_desc_bool = False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()

    mode=input('请选择排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序):')
    if mode == '1':
        stu_new.sort(key=lambda x :int(x['english']),reverse=asc_or_desc_bool)
    elif mode == '2':
        stu_new.sort(key=lambda x :int(x['python']),reverse=asc_or_desc_bool)
    elif mode == '3':
        stu_new.sort(key=lambda x :int(x['java']),reverse=asc_or_desc_bool)
    elif mode == '0':
        stu_new.sort(key=lambda x : int(x['english']) + int(x['python']) + int(x['java']),reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(stu_new)

def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')

    else:
        print('暂未保存学生信息！！！')
def show():
    stu_lst=[]
    print('show')
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                # print(item)
                stu_lst.append(eval(item))
            if stu_lst:
                show_student(stu_lst)
    else:
        print('暂未保存过数据！！！')

if __name__=='__main__':
    main()