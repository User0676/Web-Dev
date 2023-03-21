def alarm_clock(day, vacation):
  if day==0:
    day=7
  if day<=5:
    if vacation==True:
      return '10:00'
    else:
      return '7:00'
  else:
    if vacation==False:
      return '10:00'
    else:
      return "off"