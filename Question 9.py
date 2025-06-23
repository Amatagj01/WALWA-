"""Question 9
● Title: Student Records and Averages
● Question: Create a dictionary to store information about students in the AGE 219
course. Keys should be student registration numbers, and values should be
dictionaries containing their 'name' and a list of 'assignment_scores'. Write a
function to calculate the average score for a student, given their registration
number."""

#Title: Student Records and Averages
print("The Student Records and Averages")
student ={
  'AGE/D/9': {'name':'WALWA','assignment_scores': [89,98,95,60,78]},
  'AGE/D/5': {'name':'KUSEKWA','assignment_scores': [80,45,87,94,90]}
}

def calculate_average(reg_no):
  if reg_no in student :
      scores = student[reg_no]['assignment_scores']
      average = sum(scores) / len(scores)
      return f"{student[reg_no]['name']}'s average score is {average:}"
  else:
      return "Student not found."
     
    
reg_nom = input('Enter registration number of the student:'). upper() 
print(calculate_average(reg_nom))

 

