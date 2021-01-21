import pywhatkit as wt
import datetime as dt
import pandas as pd
import time

# ? Read the data from excel
data = pd.read_excel("Whatsapp-Bot\data.xlsx", engine="openpyxl")
phone_number = [f"+91{number.Contact}" for (index, number) in data.iterrows()]
# ? Get the Current Time
value = dt.datetime.now()
counter = 2

msg = "Hello,this messege is from pybot! Don't reply"

# ? Sending Message
for each in phone_number:
    hour = value.hour
    minute = value.minute
    wt.sendwhatmsg(each, msg, hour, minute + counter
                   er, wait_time=30)
    counter += 1
time.sleep(20)
