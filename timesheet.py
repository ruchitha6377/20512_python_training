def Timesheet():
    def __init__(self, date, hours, activity, disc, status):
        self.date = date
        self.hours = hours
        self.activity = activity
        self.disc = disc
        self.status = status

    def displayTimesheet(self):
        print("date : ", self.date, ", activity: ", self.activity,",status:",self.status)



ts1=Timesheet(29,8,"project","todaysheet","submitted")
ts1.details()