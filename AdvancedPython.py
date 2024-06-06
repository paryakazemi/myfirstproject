class student:
    def __init__(self,firstname,lastname,codemelli,fathername,magtatahsili,moadelemsal,age):
        self.firstname=firstname
        self.lastname=lastname
        self.codemelli=codemelli
        self.fathername=fathername
        self.magtatahsili=magtatahsili
        self.moadelemsal=moadelemsal
        self.age=age
    def showstudent(self):
        for counter in range(0,2):
            print(self.liststudent[counter].firstname)
            print(self. liststudent[counter].lastname)
            print(self.liststudent[counter].codemelli)
            print(self.liststudent[counter].fathername)
            print(self.liststudent[counter].magtatahsili)
            print(self.liststudent[counter].moadelemsal)
            print(self.liststudent[counter].age)
    def searchStudent(self,codemelli):
        for counter in range(0,2):
            if self.liststudent[counter].codemelli==codemelli:
                print(self.liststudent[counter].moadelemsal)
            else:
                print("khata vujud darad")
    def registerStudent(self,firstname,lastname,codemelli,fathername,magtatahsili,moadelemsal,age):
        std=student(firstname,lastname,codemelli,fathername,magtatahsili,moadelemsal,age)
        self.liststudent.append(std)
        print("sabt nam shodid")
class teacher:
    def __init__(self,name,famili,payetahsili,codemelli2,codepersenel,age2):
        self.name=name
        self.famili=famili
        self.payetahsili=payetahsili
        self.codemelli2=codemelli2
        self.codepersenel=codepersenel
        self.age2=age2
    def showteacher(self):
        for counter in range(0,2):
            print(self.listteacher[counter].name)
            print(self.listteacher[counter].famili)
            print(self.listteacher[counter].payetahsili)
            print(self.listteacher[counter].codemelli2)
            print(self.listteacher[counter].codepersenel)
            print(self.listteacher[counter].age2)
    def searchTeacher(self,codemelli2):
        for counter in range(0,2):
            if self.listteacher[counter].codemelli2==codemelli2:
               print(self.listteacher[counter].name)
            else:
                print("khata vujud darad")
    def registerTeacher(self,name,famili,payetahsili,codemelli2,codepersenel,age2):
        tchr=teacher(name,famili,payetahsili,codemelli2,codepersenel,age2)
        self.listteacher.append(tchr)
        print("shoma estekhdam shodid")
class school:
    def __init__(self,namemadrase,saltasis,liststudent,listteacher):
        self.namemadrase=namemadrase
        self.saltasis=saltasis
        self.liststudent=liststudent
        self.listteacher=listteacher
    def showAll(self):
        print(self.namemadrase)
        print(self.saltasis)
        for counter in range(0,2):
            print(self.liststudent[counter].firstname)
            print(self.liststudent[counter].lastname)
            print(self.liststudent[counter].codemelli)
            print(self.liststudent[counter].fathername)
            print(self.liststudent[counter].magtatahsili)
            print(self.liststudent[counter].moadelemsal)
            print(self.liststudent[counter].age)
        for counter in range(0,2):
            print(self.listteacher[counter].name)
            print(self.listteacher[counter].famili)
            print(self.listteacher[counter].payetahsili)
            print(self.listteacher[counter].codemelli2)
            print(self.listteacher[counter].codepersenel)
            print(self.listteacher[counter].age2)

firstname=input("lotfan esme khod ra vared konid?")
lastname=input("lotfan famili khod ra vared konid?")
codemelli=int(input("lotfan codemelli khod ra vared konid?"))
if codemelli<100000 or codemelli>10000000:
    print("sabtnam anjam nashod")
fathername=input("lotfan esme pedare khod ra vared konid?")
magtatahsili=int(input("lotfan magtatahsili khod ra vared konid?"))
moadelemsal=float(input("lotfan moadele emsal khod ra vared konid?"))
age=int(input("lotfan sene khod ra vared konid?"))
if age<6 or age>12:
    print("sabtnam anjam nashod")
std=student(firstname,lastname,codemelli,fathername,magtatahsili,moadelemsal,age)
firstname1=input("lotfan esme khod ra vared konid?")
lastname1=input("lotfan famili khod ra vared konid?")
codemelli1=int(input("lotfan codemelli khod ra vared konid?"))
if codemelli1<100000 or codemelli1>10000000:
    print("sabtnam anjam nashod")
fathername1=input("lotfan esme pedare khod ra vared konid?")
magtatahsili1=int(input("lotfan magtatahsili khod ra vared konid?"))
moadelemsal1=float(input("lotfan moadele emsal khod ra vared konid?"))
age1=int(input("lotfan sene khod ra vared konid?"))
if age1<6 or age1>12:
    print("sabtnam anjam nashod")
std1=student(firstname1,lastname1,codemelli1,fathername1,magtatahsili1,moadelemsal1,age1)
liststudent=[]
liststudent.append(std)
liststudent.append(std1)
print(liststudent[0].showstudent())
print(liststudent[1].showstudent())
print(liststudent[0].searchStudent(codemelli))
print(liststudent[1].searchStudent(codemelli))
print(liststudent[0].registerStudent(firstname,liststudent,codemelli,fathername,magtatahsili,moadelemsal,age))
print(liststudent[1].registerStudent(firstname,liststudent,codemelli,fathername,magtatahsili,moadelemsal,age))

name=input("lotfan esme moalem ra vared konid?")
famili=input("lotfan famili moalem ra vared konid?")
payetahsili=input("lotfan payetahsili moalem ra vared konid?")
codemelli2=int(input("lotfan codemelli moalem ra vared konid?"))
if codemelli2<100000 or codemelli2>10000000:
    print("estekhdam anjam nashod")
codepersenel=int(input("lotfan codepersenel ra vared konid?"))
age2=int(input("lotfan sene moalam ra vared konid?"))
if age2<24 or age2>54:
    print("estekhdam anjam nashod")
tchr=teacher(name,famili,payetahsili,codemelli2,codepersenel,age2)
name1=input("lotfan esme moalem ra vared konid?")
famili1=input("lotfan famili moalem ra vared konid?")
payetahsili1=input("lotfan payetahsili moalem ra vared konid?")
codemelli3=int(input("lotfan codemelli moalem ra vared konid?"))
if codemelli3<100000 or codemelli3>10000000:
    print("estekhdam anjam nashod")

codepersenel1=int(input("lotfan codepersenel ra vared konid?"))
age3=int(input("lotfan sene moalam ra vared konid?"))
if age3<24 or age3>54:
    print("estekhdam anjam nashod")
tchr1=teacher(name1,famili1,payetahsili1,codemelli3,codepersenel1,age3)
listteacher=[]
listteacher.append(tchr)
listteacher.append(tchr1)
print(listteacher[0].showteacher())
print(listteacher[1].showteacher())
print(listteacher[0].searchTeacher(codemelli2))
print(listteacher[1].searchTeacher(codemelli2))
print(listteacher[0].registerTeacher(name,famili,payetahsili,codemelli2,codepersenel,age2))
print(listteacher[1].registerTeacher(name,famili,payetahsili,codemelli2,codepersenel,age2))
namemadrase=input("lotfan name madrase ra vared konid?")
saltasis=int(input("lotfan saltasis madrase ra vared konid?"))
scl=school(namemadrase,saltasis,liststudent,listteacher)
listschool=[]
listschool.append(scl)
scl.showAll()