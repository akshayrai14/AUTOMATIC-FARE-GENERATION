import pandas as pd
from datetime import datetime
import time
data=pd.read_csv("dup.csv");
veh=data['Vehicle Type'];
number = data['License Plate No.'];
bal=data['Balance']
exit_time=int(time.time())
Tim1=data['Entry Time']
i=0
fare=0
for x in veh:
  tt=Tim1[i]
  print('Entry time : '+str(tt))
  print('Exit time : '+str(datetime.now()))
  print('License Plate Number : '+str(number[i]))
  print('Previous Balance : '+str(bal[i]))
  obj2 = time.strptime(tt,"%Y-%m-%d %H:%M:%S.%f")
  entry_time =int(time.mktime(obj2))
  duration=(exit_time-entry_time)/60
  if x=='Car':
      fare=20    
      if (duration-60)>0:
          fare+=(duration-60)*0.4
  else:
      fare=10
      if (duration-60)>0:
          fare+=(duration-60)*0.2
  print('Current Fare : '+str(fare))
  print('Updated balance : '+str(bal[i]-fare))
  i+=1
  
