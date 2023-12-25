from  win10toast import ToastNotifier
import datetime

data=datetime.datetime.now()
data=str(data)
toast=ToastNotifier()
toast.show_toast("Date-time update",data,duration=15)