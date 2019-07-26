from datetime import datetime

#pylog

mystring = "test program using cron! run at"
dt = mystring + str(datetime.now())

file = open(r"/home/sandw/twitter_sa/testlog.txt","w+")

file.write(dt)

file.close()

