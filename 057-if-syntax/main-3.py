'''Napisz program, który:
zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia
bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else ustali co dzisiaj powinieneś robić
Przepisz powyższy program stosując składnie uproszczona polecenia if'''

import datetime as dt

today_weekday = dt.date.today().strftime("%A")
today_weekday = dt.datetime.now().strftime('%A')

if today_weekday == 'Monday':
    print("I'm helping my mum")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You are doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print("I have two meetings")
elif today_weekday == 'Saturday':
    print("You have lessons")
else:
    print("SUNDAY WILL BE FOR US")


print("I'm helping my mum" if today_weekday == 'Monday' else
      "You are doing laundry" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "I'm on duty" if today_weekday == 'Thursday' else
      "I have two meetings" if today_weekday == 'Friday' else
      "You have lessons" if today_weekday == 'Saturday' else
      "SUNDAY WILL BE FOR US")