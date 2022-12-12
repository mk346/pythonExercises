marks =[] # empty array for storing the marks
students = [1,2,3,4,5] # create a dummy array for looping the number of students you want to capture marks for
for i in students:
    marks.append(int(input("Enter student marks: "))) # append student marks to the array
    if len(marks) == len(students): # stop the loop if 5 students have been captured
        for x in marks: # loop through the marks captured and print them
            print(x)