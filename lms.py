from asyncio import Task
import mysql.connector

con = mysql.connector.connect(host = "localhost", password ="winserver" , user = "root", port = 3306, database = "LMS")
print(con)
Cursor = con.cursor(buffered=True,dictionary=True)

def insert():
    task=input("enter book name ")
    sql=f"insert into book(book_Name) values('{(task)}')"
    print(sql)
    Cursor.execute(sql)
    con.commit()
    print("Done")
    book()




def read():
    sql="select * from book"
    Cursor.execute(sql)
    data=Cursor.fetchall()
    for x in data:
        print(*x)
    book()

def delete():
    tno=input("enter book number")
    sql=f"delete from book where book_id=({tno})"

    Cursor.execute(sql)
    con.commit()
    book()

def update():
    ab=input("enter id nub")
    sql=f"select * from book where book_id-({ab})"
    Cursor.execute(sql)
    data=Cursor.fetchall()
    for x in data:
        Task=x[1]
    
    bname=input("updated book")
    sql=f"UPDATE book SET book_name=('{bname}') WHERE ID = ({ab});"
    Cursor.execute(sql)
    con.commit()
    print("Done")
    book()


def book():
    print("select an operation")
    z=int(input(''))
    if(z==1):
        insert()
    elif(z==2):
        read()
    elif(z==3):
        delete()
    elif(z==4):
        update()
    else:
        print("Shai operation daliye ")
    main()

####################################################################################################################################



def insert_():
    task=input("enter user name ")
    sql=f"insert into user(user_Name) values('{(task)}')"
    print(sql)
    Cursor.execute(sql)
    con.commit()
    print("Done")
    user()




def read_():
    sql="select * from user"
    Cursor.execute(sql)
    data=Cursor.fetchall()
    for x in data:
        print(*x)
    user()


def delete_():
    tno=input("enter user number")
    sql=f"delete from user where user_id=({tno})"

    Cursor.execute(sql)
    con.commit()
    user()


def update_():
    ab=input("enter id nub")
    sql=f"select * from user where user_id-({ab})"
    Cursor.execute(sql)
    data=Cursor.fetchall()
    for x in data:
        Task=x[1]
    
    bname=input("updated user")
    sql=f"UPDATE book SET user_name=('{bname}') WHERE ID = ({ab});"
    Cursor.execute(sql)
    con.commit()
    print("Done")
    user()


def user():
    print("select an operation")
    z=int(input(''))
    if(z==1):
        insert_()
    elif(z==2):
        read_()
    elif(z==3):
        delete_()
    elif(z==4):
        update_()
    else:
        print("please enter  valid operation ")
    main()


##################################################################################################################################################


def issue():
    bookid=input("enter book id ")
    userid=input("enter user id ")
    issuedate=input("enter the date 'yyyy-mm-dd")
    sql=f"Select * from  book_user_relation where book_id={bookid}"
    
    Cursor.execute(sql)
    data=Cursor.fetchall()
    
    if(len(data)):
        print("Sorry book is not available")
    elif len(data)==0:
    # data=(bookid,userid)
        sql=f"insert into book_user_relation(book_id,user_id,issue_date) values({bookid},{userid},'{issuedate}')"
        # sql='insert into book_user_relation(%s,%s)'
        print(sql)

        Cursor.execute(sql)
        con.commit()
    else:
        print("Done")
    main()


def submit():
    i=input("enter book_id")
    sql=f"delete from book_user_relation where book_id=({i})"

    Cursor.execute(sql)
    con.commit()
    main()


def view():
    sql="select * from book_user_relation"
    Cursor.execute(sql)
    data=Cursor.fetchall()
    for x in data:
        print(*x)
    main()

def display():
    sql="select user.user_name, book_user_relation.user_id, book_user_relation.book_id, book_user_relation.issue_date from book_user_relation join user on user.user_id=book_user_relation.user_id;"
    Cursor.execute(sql)
    con.commit()
    data=Cursor.fetchall()
    for x in data:
        print(x)
    main()



    








##################################################################################################################################################

def main():
    print("press b for  book access & press u for user  access ") 
    print("press x for  issue book  & press z for submit book ") 
    print("view issue book list press v")
    q=input()
    if (q=='b'):
        book()
    elif(q=='u'):
        user()
    elif(q=='x'):
        issue()
    elif(q=='z'):
        submit()
    elif(q=='v'):

        view()
    elif(q=='f'):
        display()
    else:
        print("not valid ")

main()
