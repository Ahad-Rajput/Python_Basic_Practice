# Find out whether a student is passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take the marks as an input from the User


marks1 = int(input("Enter subject 1 marks: "))
marks2 = int(input("Enter subject 2 marks: "))
marks3 = int(input("Enter subject 3 marks: "))

total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print(f"Congratulation! You are passed. Your total percentage is {total_percentage}")
else:
    print(f"You are failed. Your total percentage is {total_percentage}")