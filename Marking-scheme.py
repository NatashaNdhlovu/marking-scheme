student_mark=57
# I am checking the range thats above 75 and awarding : Dist
if student_mark>75 and student_mark<=100:
 print("Distinction")
# checking the range thats above 60 awarding :Pass 
elif student_mark>60 and student_mark<=75:
 print("Pass")
# checking the range thats above 50 awarding :Credit
elif student_mark>50 and student_mark<=60:
 print("Credit")
# checking the range thats above 35 awading :Almost
elif student_mark>35 and student_mark<=50:
 print("Almost")
# checking the range thats above 20 awading :Fail 
elif student_mark>20 and student_mark<=35:
 print("Fail")
elif student_mark>0 and student_mark<=20:
 print("ungraded")
# checking the range thats above 20 and below awading :Ungraded 
else:
 print("error")
   
