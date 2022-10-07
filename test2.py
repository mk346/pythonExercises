gender = input("Enter Debtor's Gender: ").capitalize()
if gender == 'Male':
    salutation = "Sir"
    initials = "his"
elif gender == 'Female':
    salutation = "Madam"
    initials = "her"
#print(salutation + " " +initials)
#f = open("template.txt", "x")
fd = open("template.txt","w")
#input = input("user input")
fd.write("Gender captured is "+gender +"\n" +"Correct salutation according to gender is "+salutation+"\n"+"Correct initials according to the gender captured is "+initials)
# fd.write("\n")
# fd.write(salutation)
# fd.write("\n")
# fd.write(initials)