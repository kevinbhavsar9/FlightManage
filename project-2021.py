import mysql.connector as sql
import random
import pandas as pd


db=sql.connect(host="localhost",user="root",passwd="whatever",database="project")
cursor=db.cursor()


#cursor.execute("drop table flyair_flight")
#cursor.execute("drop table flyair_flight")
#cursor.execute('drop table user')
#cursor.execute('create table flyair_flight(pass_no int primary key,seat_no varchar(5), to_destination varchar(20),from_destination varchar(20),departure_date date, arrival_time varchar(10),departure_time varchar(20), price int(10), meal varchar(10), meal_amt float null)')
#cursor.execute("insert into flyair_flight values(101,'A1', 'Dubai','Ahmedabad','2020-01-21','03:00 PM','12:00 PM',50000, 'yes',100)")
#cursor.execute("insert into flyair_flight values(102,'A2', 'Sydney','Mumbai','2020-02-11','06:00 PM','01:00 PM',75000, 'yes',210)")
#cursor.execute("insert into flyair_flight values(103,'A3', 'New York','Delhi','2020-03-10','10:00 PM','01:00 PM',100000, 'yes',932)")
#cursor.execute("insert into flyair_flight values(104,'B1', 'London','Pune','2020-04-11','09:00 PM','12:00 PM',90000, 'yes',333)")
#cursor.execute("insert into flyair_flight values(105,'B2', 'Moscow','Kolkata','2020-05-02','06:00 PM','2:00 PM',85000, 'yes',388)")

#cursor.execute("create table flyair_cust(pass_no int references flyair_flight(pass_no),name varchar(20),mob_no int(15), email varchar(50))")
#cursor.execute("insert into flyair_cust values(101,'manushi bhavsar','1234567891','manushi@gmail.com')")
#cursor.execute("insert into flyair_cust values(102,'hetal dudhrejiya','1244567891','hetal@gmail.com')")
#cursor.execute("insert into flyair_cust values(103,'devam raval','1232567891','devam@gmail.com')")
#cursor.execute("insert into flyair_cust values(104,'purav shah','1214567891','purav@gmail.com')")




def view():
    print('1.View passenger details \n2.View flight details')
    print()
    ch=int(input('Enter your choice:'))
    print()
    if ch==1:
        q=input('Enter your full name:')
        cursor.execute('select * from flyair_cust where name like '%q%'')
        a=cursor.fetchall()
        for i in a:
            print(a)
            break
    elif ch==2:
        q=input('Enter your full name:')
        cursor.execute('select * from flyair_cust where name like '%q%'')
        a=cursor.fetchall()
        for i in a:
            print(a)
            break
    else:
        print('Invalid Choice')
    print()


def enter():
    print('Step 1:Enter Flight Data  \nStep 2:Enter passenger details')
    print()
    print('STEP 1')
    pass_no=int(input('Enter passenger ID:'))
    seat_no=random.choice(['A1','C1','C2','C3','D1','D2','D3','A2','A3','B1','B2','B3'])
    to_destination=(input('Enter your visit destination:'))
    from_destination=input('Enter your departing destination:')
    departure_date=input('Enter your departing date (only in YYYY-MM-DD format):')
    arrival_time=random.choice(['10:00 AM','11:00 AM','12:00 PM','02:00 AM','3:00 AM','04:00 PM'])
    departure_time=random.choice(['2:00 AM','01:00 AM','01:00 PM','02:00 PM','3:00 PM','04:00 AM'])
    price=random.randint(10000,100000)
    meal=input('Do you want an in-flight meal? (yes/no)')
    if meal=='yes' or meal=='YES':
        srno=[1,2,3,4,5,6,7,8,9,10]
        items=['Cappacino', 'Hot Chocolate','Frappacino','Ice Cream Sundae','French Vanilla Bean','Ice Tea','Espresso','Choco Chip Frappe','Java Chip','Milkshake']
        price=[230,100,500,75,100,100,200,100,150,120]
        d={'Sr. No.':srno, 'Item Name':items, 'Price':price}
        print(pd.DataFrame(d))
        bill=0
        food=" "
        c=input("Do you want an in-flight meal?(yes/no)")
        while c=='yes' or "YES":
            ch=int(input('Enter your choice(int only):'))
            if ch==1:
                food="Cappacino"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*230
            elif ch==2:
                food="Hot Chocolate"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*100
            elif ch==3:
                food="Frappacino"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*500
            elif ch==4:
                food="Ice Cream Sundae"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*75
            elif ch==5:
                food="French Vanilla Bean"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*100
            elif ch==6:
                food="Ice Tea"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*100
            elif ch==7:
                food="Espresso"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*200
            elif ch==8:
                food="Choco Chip Frappe"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*100
            elif ch==9:
                food="Java Chip"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*150
            elif ch==10:
                food="Milkshake"
                qty=int(input('Enter Quantity:'))
                bill=bill+qty*120
            else:
                print('INVALID')
            break
        print("Food item:",food)
        tax=(9/100)*bill
        nbill=bill+tax 
        print('Tax amount:',tax)
        print('Total bill amount:', nbill)
        if c=='no' or c=='NO':
            print('Thank you!')
        
    
    cursor.execute('insert into flyair_flight(pass_no,seat_no,to_destination,from_destination,departure_date,arrival_time,departure_time,price,meal,meal_amt) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(pass_no,seat_no,to_destination,from_destination,departure_date,arrival_time,departure_time,price,meal,nbill))
        
    print()
    
    print('STEP 2')
    name=input('Enter your name:')
    mob_no=int(input('Enter your mobile number:'))
    email=input('Enter your email address:')
    cursor.execute('insert into flyair_cust(pass_no,name, mob_no, email) values(%s,%s,%s,%s)',(pass_no,name,mob_no,email))
    cursor.execute('select * from flyair_cust')
    b=cursor.fetchall()
    '''for i in b:
        print(b)
        continue'''
    df1=pd.DataFrame(b)
    print(df1)
    print()
    cursor.execute('select * from flyair_flight')
    a=cursor.fetchall()
    '''for i in a:
        print(a)
        continue'''
    df2=pd.DataFrame(a)
    print(df2)


def update():
    print('Update Information:')
    print('Update Passenger Details:')
    print('What do you want to update: \n1. Name \n2.Mobile Number \n3.Email ID')
    u=int(input('Enter your choice(in number):'))
    if u==1:
        n=input('Enter your full name:')
        cursor.execute("update table flyair_cust set name=%s",(n,))
    elif u==2:
        n=int(input('Enter your mobile number:'))
        cursor.execute("update table flyair_cust set mob_no=%s",(n,))
    elif u==3:
        n=(input('Enter your email id:'))
        cursor.execute("update table flyair_cust set email=%s",(n,))
    else:
        print('INVALID OPTION')
    

def delete():
    print('Delete information')
    print('Delete Passenger details:')
    print('What do you want to delete: \n1. Name \n2.Mobile Number \n3.Email ID')
    u=int(input('Enter your choice(in number):'))
    if u==1:
        n=input('Enter your full name:')
        cursor.execute("delete from flyair_cust where name=%s",(n,))
    elif u==2:
        n=int(input('Enter your mobile number:'))
        cursor.execute("delete from flyair_cust where mob_no=%s",(n,))
    elif u==3:
        n=input('Enter your email id:')
        cursor.execute("delete from flyair_cust where email=%s",(n,))


def user_login():
    #cursor.execute('drop table user')
    #cursor.execute('create table user(user_id int, username varchar(20),password varchar(20))')
    user_id=int(input('Enter your user ID:'))
    username=input('Enter your username:')
    password=input('Enter your password:')
    cursor.execute('insert into user values(%s,%s,%s)',(user_id, username, password))
    cursor.execute('select * from user;')
    print()
    a=cursor.fetchall()
    d=pd.DataFrame(a,columns=['User ID','Username','Password'])
    print(d)
    print()
    '''
    for i in a:
        print(a)
        break
    '''
    print('What would you like to do:')
    print("1. Enter details \n2. View details \n3. Update details \n4. Delete details")
    print()
    ch=int(input('Enter your choice:'))
    if ch==1:
        enter()
    elif ch==2:
        view()
    elif ch==3:
        update()
    elif ch==4:
        delete()

user_login()
db.commit()
db.close()
