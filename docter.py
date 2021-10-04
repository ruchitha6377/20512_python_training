from database import conect_mysql

class Docter:
  def __init__(self,name,specialization):
    self.name=name
    self.specialization = specialization

  def add_docter(self):
    mycon = conect_mysql()
    cur = mycon.cursor()
    sql="insert into docter(name,specialization) values (%s,%s)"
    val=(self.name,self.specialization)
    cur.execute(sql, val)
    mycon.commit()
    mycon.close()

  def update_docter_spec(self,specialization):
    mycon = conect_mysql()
    cur = mycon.cursor()
    sql = "update docter set specialization = %s where id =%s"
    val = (self.name, self.specialization)
    cur.execute(sql, val)
    mycon.commit()

d=Docter("ruchitha","radiologist")
d.add_docter()
print(d.name)