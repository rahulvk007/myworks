from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as connector
global login_status
login_status = False
global admin_login
admin_login = False


page = tk.Tk()
page.geometry("10000x10000")
page.title("Verdure healthcare")
tk.Label(page, text="Verdure Healthcare",
         fg="Black", font="Gabriola 45 bold").pack()
tk.Label(page, text="'We Share to Care'",
         fg="Black", font="Gabriola 23").pack()


def open_reg():
    config = {
        "user": "root",
        "password": "passwd",  # Enter your sql password inside the quotes
        "host": "localhost",
        "port": 3306,
        "database": "hackathon"
    }
    try:
        c = connector.connect(**config)
    except:
        print('Connection error')
    new = Toplevel(page)
    new.geometry("10000x10000")
    new.title("User Registration")
    tk.Label(new, text="USER REGISTRATION", fg="Black",
             font="Gabriola 45 bold").pack()
    tk.Label(new, text="Email:", font="Constantia 20 ").place(x=400, y=150)
    tk.Label(new, text="UserName:", font="Constantia 20 ").place(x=400, y=210)
    tk.Label(new, text="login ID:", font="Constantia 20 ").place(x=400, y=270)
    email = tk.StringVar(new)
    name = tk.StringVar(new)
    ID = tk.StringVar(new)
    e0 = tk.Entry(new, textvariable=email).place(
        x=630, y=150, width=400, height=30)
    e1 = tk.Entry(new, textvariable=name).place(
        x=630, y=210, width=400, height=30)
    e2 = tk.Entry(new, textvariable=ID).place(
        x=630, y=270, width=400, height=30)

    def reg():
        e = email.get()
        a = name.get()
        b = ID.get()
        cur = c.cursor()
        query = 'select * from users where name = "{0}"'.format(a)
        cur.execute(query)
        res = cur.fetchall()
        if len(res) == 0:
            query = 'insert into users values ("{0}","{1}","{2}")'.format(
                a, e, b)
            cur.execute(query)
            c.commit()
            mb.showinfo("Info", "Registration Successful, Please login")
            open_login()
        else:
            mb.showerror("Error", "User already exists, Please login")
            open_login()

    tk.Button(new, text="Submit", command=reg).place(
        x=600, y=360, width=250, height=40)


def open_login():
    config = {
        "user": "root",
        "password": "passwd",
        "host": "localhost",
        "port": 3306,
        "database": "hackathon"
    }
    try:
        c = connector.connect(**config)
    except:
        print('Connection error')
    new = Toplevel(page)
    new.geometry("10000x10000")
    new.title("User Login")
    tk.Label(new, text="USER LOGIN", fg="Black",
             font="Gabriola 45 bold").pack()
    tk.Label(new, text="UserName:", font="Constantia 20 ").place(x=400, y=210)
    tk.Label(new, text="login ID:", font="Constantia 20 ").place(x=400, y=290)
    name = tk.StringVar(new)
    ID = tk.StringVar(new)
    e1 = tk.Entry(new, textvariable=name).place(
        x=630, y=210, width=400, height=30)
    e2 = tk.Entry(new, textvariable=ID).place(
        x=630, y=290, width=400, height=30)

    def login():
        a = name.get()
        b = ID.get()
        cur = c.cursor()
        query = 'select name,password from users where name = "{}"'.format(a)
        cur.execute(query)
        r = cur.fetchall()
        if len(r) != 0:
            if r[0][0] == a and r[0][1] == b:
                login_status = True
            else:
                #global login_status
                login_status = False
        else:
            #global login_status
            login_status = False

        new = Toplevel(page)

        if login_status is True:
            new.geometry("10000x10000")
            new.title("Departments")
            tk.Label(new, text="DEPARTMENTS", fg="Black",
                     font="Gabriola 45 bold").pack()
            mydb = {
                    "user": "root",
                    "password": "password",
                    "host": "localhost",
                    "port": 3306,
                    "database": "doctors"
                      }
            try:
                cdoc = connector.connect(**mydb)
            except:
               print('Connection error')

            def b1():
                new2 = Toplevel(page)
                new2.geometry("10000x10000")
                new2.title("Neurolgy department")
                tk.Label(new2, text="This is the Neurolgy department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new2, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Neurology"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)

            tk.Button(new, text="Neurology", command=b1).place(
                x=580, y=200, width=400, height=30)

            def b2():
                new3 = Toplevel(page)
                new3.geometry("10000x10000")
                new3.title("Dermatolgy")
                tk.Label(new3, text="This is the Dermatolgy department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new3, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Dermatology"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="Dermatolgy", command=b2).place(
                x=580, y=250, width=400, height=30)

            def b3():
                new4 = Toplevel(page)
                new4.geometry("10000x10000")
                new4.title("Cardiology")
                tk.Label(new4, text="This is the Cardiology department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new4, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Cardiology"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="Cardiology", command=b3).place(
                x=580, y=300, width=400, height=30)

            def b4():
                new5 = Toplevel(page)
                new5.geometry("10000x10000")
                new5.title("ENT")
                tk.Label(new5, text="This is the ENT department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new5, height=40, width=180)
                T.pack(expand=True)
                query = "select * from ENT"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="ENT", command=b4).place(
                x=580, y=350, width=400, height=30)

            def b5():
                new5 = Toplevel(page)
                new5.geometry("10000x10000")
                new5.title("Gastroentology")
                tk.Label(new5, text="This is the Gastroentology department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new5, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Gastroentology"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="Gastroentology", command=b5).place(
                x=580, y=400, width=400, height=30)

            def b6():
                new5 = Toplevel(page)
                new5.geometry("10000x10000")
                new5.title("Ophthalmology")
                tk.Label(new5, text="This is the Ophthalmology department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new5, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Ophthalmology"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="Ophthalmology", command=b6).place(
                x=580, y=450, width=400, height=30)

            def b7():
                new5 = Toplevel(page)
                new5.geometry("10000x10000")
                new5.title("Orthopaedics")
                tk.Label(new5, text="This is the Orthopaedics department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new5, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Orthopaedics"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="Orthopaedics", command=b7).place(
                x=580, y=500, width=400, height=30)

            def b8():
                new5 = Toplevel(page)
                new5.geometry("10000x10000")
                new5.title("Paediatrics")
                tk.Label(new5, text="This is the Paediatrics department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new5, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Paediatrics"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="Paediatrics", command=b8).place(
                x=580, y=550, width=400, height=30)

            def b9():
                new5 = Toplevel(page)
                new5.geometry("10000x10000")
                new5.title("Radiology")
                tk.Label(new5, text="This is the Radiology department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new5, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Radiology"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="Radiology", command=b9).place(
                x=580, y=600, width=400, height=30)

            def b10():
                new5 = Toplevel(page)
                new5.geometry("10000x10000")
                new5.title("Urology")
                tk.Label(new5, text="This is the Urology department",
                         font="Constantia 20 ").pack()
                mycursor = cdoc.cursor()
                T = Text(new5, height=40, width=180)
                T.pack(expand=True)
                query = "select * from Urology"
                mycursor.execute(query)
                result = mycursor.fetchall()
                doc = """ """
                for i in result:
                    sno = i[0]
                    dname = i[1]
                    hos = i[2]
                    default_rating = int(i[3])
                    q = 'select rating from reviews where name = "{0}"'.format(
                        dname)
                    cur = c.cursor()
                    cur.execute(q)
                    r = cur.fetchall()
                    rating = 0
                    if len(r) != 0:
                        for i in r:
                            rating = rating + i[0]
                        rating = ((rating+default_rating)/(len(r)+1))
                        rating = str(round(rating, 1))
                    else:
                        rating = str(default_rating)
                    doc = doc + '\n'+'Sno  :'+str(sno) + '\n' + 'Name:' + \
                        dname + '\nHospital :' + str(hos) + \
                        '\nRating :' + rating + '\n'
                T.insert('end', doc)
            tk.Button(new, text="Urology", command=b10).place(
                x=580, y=650, width=400, height=30)

            def reviews():
                new6 = Toplevel(page)
                new6.geometry("10000x10000")
                new6.title("User Reviews")
                tk.Label(new6, text="All reviews",
                         font="Constantia 20 ").pack()
                T = Text(new6, height=40, width=180)  # To declare text box
                T.pack(expand=True)  # same code
                query = "select * from reviews"
                cur.execute(query)
                result = cur.fetchall()
                s = """ """
                for i in result:
                    dname = i[0]
                    drev = i[1]
                    drating = i[2]
                    dept = i[3]
                    s = s + '\n' + 'Name:' + \
                        dname + '\nRating(Out of 5):' + str(drating) + \
                        '\n' + dept+'\n'+drev + '\n'
                T.insert('end', s)  # string s will be displayed

            tk.Button(new, text="reviews", command=reviews).place(
                x=580, y=700, width=400, height=30)

            if login_status is True:
                def admin():
                    new6 = Toplevel(page)
                    new6.geometry("10000x10000")
                    new6.title("Admin")
                    tk.Label(new6, text="Admin Dashboard",
                             font="Constantia 20 ").pack()
                    tk.Label(new6, text="ADMIN LOGIN", fg="Black",
                             font="Gabriola 45 bold").pack()
                    tk.Label(new6, text="UserName:",
                             font="Constantia 20 ").place(x=400, y=210)
                    tk.Label(new6, text="login ID:",
                             font="Constantia 20 ").place(x=400, y=290)
                    name = tk.StringVar(new6)
                    ID = tk.StringVar(new6)
                    e1 = tk.Entry(new6, textvariable=name).place(
                        x=630, y=210, width=400, height=30)
                    e2 = tk.Entry(new6, textvariable=ID).place(
                        x=630, y=290, width=400, height=30)

                    def submit_admin():
                        a = name.get()
                        b = ID.get()
                        cur = c.cursor()
                        query = 'select name,password from users where name = "{}"'.format(
                            a)
                        cur.execute(query)
                        r = cur.fetchall()
                        if len(r) != 0:
                            if r[0][0] == a and a == 'admin' and r[0][1] == b:
                                add_doctor()
                            else:
                                mb.showerror('Error!', 'Invalid credentials')

                    def add_doctor():
                        new7 = Toplevel(page)
                        new7.geometry("10000x10000")
                        new7.title("Admin")
                        tk.Label(new7, text="Add a doctor",
                                 font="Constantia 20 ").pack()
                        tk.Label(new7, text="HOSPITAL :",
                                 font="Constantia 20 ").place(x=400, y=210)
                        tk.Label(new7, text="DOCTOR NAME:",
                                 font="Constantia 20 ").place(x=400, y=290)
                        tk.Label(new7, text="DEPARTMENT:",
                                 font="Constantia 20 ").place(x=400, y=370)
                        tk.Label(new7, text="RATING: ",
                                 font="Constantia 20").place(x=400, y=450)
                        name = tk.StringVar(new7)
                        dept = tk.StringVar(new7)
                        rating = tk.StringVar(new7)
                        hospital = tk.StringVar(new7)
                        e1 = tk.Entry(new7, textvariable=hospital).place(
                            x=630, y=210, width=400, height=30)
                        e2 = tk.Entry(new7, textvariable=name).place(
                            x=630, y=290, width=400, height=30)
                        e3 = tk.Entry(new7, textvariable=dept).place(
                            x=630, y=370, width=400, height=30)
                        e4 = tk.Entry(new7, textvariable=rating).place(
                            x=630, y=450, width=400, height=30)

                        def submit_doc():
                            h = hospital.get()
                            a1 = name.get()
                            d1 = dept.get()
                            r1 = rating.get()
                            q = 'select * from {0}'.format(d1)
                            mycursor = cdoc.cursor()
                            mycursor.execute(q)
                            r = mycursor.fetchall()
                            sno = len(r) + 1
                            query = 'insert into {0} values({1},"{2}","{3}","{4}")'.format(
                                d1, sno, a1, h, r1)
                            mycursor.execute(query)
                            cdoc.commit()
                            mb.showinfo("Success", "Doctor added")
                        tk.Button(new7, text="Submit", command=submit_doc).place(
                            x=600, y=500, width=200, height=30)

                    tk.Button(new6, text="Add doctor", command=submit_admin).place(
                        x=580, y=350, width=400, height=30)

                tk.Button(new, text="Admin login", command=admin).place(
                    x=580, y=150, width=400, height=30)

            def post_review():
                new7 = Toplevel(page)
                new7.geometry("10000x10000")
                new7.title("Post Review")
                tk.Label(new7, text="Post a review",
                         font="Constantia 20 ").pack()
                tk.Label(new7, text="DOCTOR NAME:",
                         font="Constantia 20 ").place(x=400, y=290)
                tk.Label(new7, text="RATING:",
                         font="Constantia 20 ").place(x=400, y=370)
                tk.Label(new7, text="DEPARTMENT:",
                         font="Constantia 20 ").place(x=400, y=450)
                tk.Label(new7, text="REVIEW:",
                         font="Constantia 20 ").place(x=400, y=530)

                name = tk.StringVar(new7)
                rating = tk.StringVar(new7)
                dept = tk.StringVar(new7)
                review = tk.StringVar(new7)
                e2 = tk.Entry(new7, textvariable=name).place(
                    x=630, y=290, width=400, height=30)
                e3 = tk.Entry(new7, textvariable=rating).place(
                    x=630, y=370, width=400, height=30)
                e4 = tk.Entry(new7, textvariable=dept).place(
                    x=630, y=450, width=400, height=30)
                e5 = tk.Entry(new7, textvariable=review).place(
                    x=630, y=530, width=400, height=30)

                def submit_review():
                    b = name.get()
                    c1 = review.get()
                    d = int(rating.get())
                    e = dept.get()
                    query = 'insert into reviews values ("{0}","{1}",{2},"{3}")'.format(
                        b, c1, d, e)
                    cur.execute(query)
                    c.commit()
                    mb.showinfo('Success', 'Review successfully posted')

                tk.Button(new7, text="Submit", command=submit_review).place(
                    x=580, y=600, width=100, height=30)

            tk.Button(new, text="Post review", command=post_review).place(
                x=580, y=750, width=400, height=30)

        else:
            mb.showerror("Error", "Invalid login, try again")

    tk.Button(new, text="Submit", command=login).place(
        x=650, y=360, width=150, height=40)


tk.Button(page, text="New User", command=open_reg).place(
    x=650, y=300, width=250, height=40)
tk.Button(page, text="Login", command=open_login).place(
    x=650, y=360, width=250, height=40)
page.mainloop()
