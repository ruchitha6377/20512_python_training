import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="case_study"
)

mycursor = mydb.cursor()

class docter:
  def __init__(self,id,name,specialization):
    self.id=id
    self.name=name
    self.specialization = specialization

  def add_docter(self):
    mycursor = mydb.cursor()
    sql="insert into docter(id,name,specialization) values (%d,%s,%s)"
    val=(20512,"rupiah","radiologist")
    mycursor.execute(sql, val)

    mycursor.execute("SELECT * FROM docter")
    myresult = mycursor.fetchall()

    print("id | Name |  specialization")

    for x in myresult:
      print(x[0] + " | " + x[1] + "|" + x[2] )
      print(type(x))
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")







