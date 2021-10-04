from database import conect_mysql

class Schedule:
  def __init__(self,doc_id,pat_id,s_day,start_time,end_time,status):

    self.doc_id=doc_id
    self.pat_id = pat_id
    self.s_day=s_day
    self.start_time = start_time
    self.end_time = end_time
    self.status = status


  def add_schedule(self):
    mycon = conect_mysql()
    cur = mycon.cursor()
    sql="insert into schedule(doc_id,pat_id,s_day,start_time,end_time,status) values (%s,%s,%s,%s,%s,%s)"
    val=(self.doc_id,self.pat_id,self.s_day,self.start_time,self.end_time,self.status)
    cur.execute(sql, val)
    mycon.commit()

d=Schedule("1","2","2021-10-25","2:00 PM","3:00 PM","booked")
d.add_schedule()
print(d.name)