from database import conect_mysql

class Patient:
  def __init__(self,name,gender,age):

    self.name=name
    self.gender = gender
    self.age=age


  def add_patient(self):
    mycon = conect_mysql()
    cur = mycon.cursor()
    sql="insert into patient(name,gender,age) values (%s,%s,%s)"
    val=(self.name,self.gender,self.age)
    cur.execute(sql, val)
    mycon.commit()

d=Patient("john","male",25)
d.add_patient()
print(d.name)