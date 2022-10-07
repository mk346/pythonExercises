# demonstrate a grading system 
# Subject1 -> end + mid /50
mark = []
subject = []
grd = []
student_name = []
def Display():
    print("Enter the Number of Students: ")
    stud_no= int(input())
    for i in range(stud_no):
        student = input("Enter Student Name: ")
        student_name.append(student)
        name = student_name[i]
        print("Enter Number of Subjects: ")
        subNo = int(input())
        for i in range(subNo):
            subject.append(input("Enter Subject name: "))
            mid = int(input("Enter midterm marks: "))
            end = int(input("Enter endterm marks: "))
            tot = mid + end
            mark.append(tot)

        for i in range(subNo):
            output= subject[i] + " " + str(mark[i])
    calculate(tot)
    gd = (grd[0])
    print(name)
    print (output + " " +gd)
Display()
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
    grd.append (grade)



