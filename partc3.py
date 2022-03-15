import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student2"
)

cursor=mydb.cursor()
cursor.execute("DROP TABLE IF EXISTS STUDENT")
sql="""CREATE TABLE student(
REGNO INT NOT NULL,
NAME CHAR(20),
MARK1 INT,
MARK2 INT,
MARK3 INT)"""
cursor.execute(sql)


def accept(rno,name, m1, m2, m3):
    cursor=mydb.cursor()
    qry="insert into student(RegNo, Name, Mark1, Mark2, Mark3) values('%d','%s','%d','%d','%d')"
    args=(rno,name, m1, m2, m3)
    try:
        cursor.execute(qry%args)
        mydb.commit()
        print("inserted 1 row")
    except:
        mydb.rollback()

def deleted(rno):
    sel= "delete from student where RegNo='%d'"%(rno)
    cursor.execute(sel)
    mydb.commit()
    print("deleted data rno")


def display():
    sel= "select * from student"
    cursor.execute(sel)
    Result= cursor.fetchall()
    if Result:
        print("Regno \t\t NAME \t\t Mark1 \t\t mark2 \t\t mark3 \t\t")
        for Rows in Result:
            print(Rows[0],"\t\t", Rows[1],"\t\t", Rows[2],"\t\t", Rows[3],"\t\t", Rows[4],"\n")
    else:
        print("no data exists")
    

i=0
while(i<=3):
    try:
        print("1=> insert data")
        print("2=> display")
        print("3=> delete")
        ch=int(input("enter choice"))
        if(ch==1):
            n=int(input("enter no of rows"))
            for i in range(n):
                rno= input("enter reg no")
                sel="select RegNo from student where RegNo='%d'"%(rno)
                cursor.execute(sel)
                result= cursor.fetchone()
                if result:
                    print("record already exists")
                    
                else:
                    
                    nm= input("enter name")
                    m1= input("enter mark1")
                    m2= input("enter 2")
                    m3= input("enter 3")
                    accept(rno,nm, m1, m2, m3)
        elif(ch==2):
            display()
        elif(ch==3):
            
            sel= "select * from student"
            cursor.execute(sel)
            result= cursor.fetchall()
            if result:
                rno= int(input("enter eno to deleted"))
                sel="select RegNo from student where RegNo='%d'"%(rno)
                cursor.execute(sel)
                result= cursor.fetchone()
                if result:
                    deleted(rno)
                    
                else:
                    print("student data not exists")
            else:
                print("empty recird")
        else:
            print("invalid choice")
            break
    except:
        print("enter valid entry")
mydb.close()
        
                
