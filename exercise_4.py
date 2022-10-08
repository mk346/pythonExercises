mark = []
subject = []
grd = []
def Display():
    print("Enter Number of Subjects: ")
    subNo = int(input())
    for i in range(subNo): # looping until all the subjects are captured 
        subject.append(input("Enter Subject name: ")) # storing captured subject name to a list
        mid = int(input("Enter midterm marks: "))
        end = int(input("Enter endterm marks: "))
        tot = mid + end
        mark.append(tot) # storing total marks to a list
    calculate(tot) # invoking the calculate marks function
    gd = (grd[0]) # accessing the stored grade
    for i in range(subNo):
        output= subject[i] + " " + str(mark[i]) + " " + gd
        print (output)
Display()
# function to calculate the grade
def calculate(total):
    if total >= 70 and total <= 100:
        grade = 'A'
    if total >= 60 and total < 70:
        grade = 'B'

    if total >= 50 and total < 60:
        grade = 'C'

    if total >= 40 and total < 50:
        grade = 'D'

    if total >= 0 and total < 40:
        grade = 'E'
    grd.append (grade) # storing the returned grade to a list



