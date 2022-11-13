# AUTOMATIC-FARE-GENERATION
Automatic fare generation system in python will take the image of a car and detect it's license plate number and even calculate the fare automatically by the in time and out time of the car 
<br>
When run in Raspberry pi the python code 'plate.py' gives an output like this :- <br>
![image](https://user-images.githubusercontent.com/109916723/201528746-ca100923-7655-4f0b-be20-7127f5516848.png)
As you can see above the license plate number is detected through plate.py and shown in output .The same plate number along with some other added details about the car 
is stored simultaneously by that same code in a 'dup.csv' file which looks like this :-<br>
![image](https://user-images.githubusercontent.com/109916723/201528895-388cfca7-ba69-421b-8e2d-1324a6956af7.png)
<br>Now finally after running plate.py when we run the program 'fare.py' then the realtime is noted as exit time and the entry time is taken from the dup.csv file
and the fare for this time is calculated and shown on the screen with an updated balance of the user as shown :-<br>
![image](https://user-images.githubusercontent.com/109916723/201529062-d6917941-77e7-46ae-88a2-e49abe9054b5.png)
Note- Fare will only come more than 20 when actually the second file will be compiled after a certain time such that the fare is increased or else you can 
simply change the entry time manually in the dup.csv file and see the fare accordingly.
