import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

print("Name |  Address")

for x in myresult:
  print(x[0] +" | " + x[1])
  print(type(x))
mydb.commit()

print(mycursor.rowcount, "record inserted.")




class docter:
  def __init__(self,id,name,specialization):
    self.id=id
    self.name=name
    self.specialization = specialization

  def add_doctor(self):
    mycursor = mydb.cursor()
    sql="insert into doctor(id,name,specialization) values (%d,%S,%S)"
    val=(20512,"ruchitha","radiologist")

    mycursor.execute("SELECT * FROM doctor")
    myresult = mycursor.fetchall()

    print(" id  |  Name |  specialization")

    for x in myresult:
      print(x[0] + " | " + x[1] + "|" + x[2])
      print(type(x))
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")