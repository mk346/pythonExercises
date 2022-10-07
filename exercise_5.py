from distutils.command.install_egg_info import safe_name

# collecting the required information
amount = int(input("Enter Debt Amount: "))
debtor_name = input("Enter Debtor's Name: ").capitalize()
gender = input("Enter Debtor's Gender: ").capitalize()
phone = input("Enter Debtor's Phone Number: ")
email = input("Enter Debtor's Email: ")

# Determing salutation and gender initials
if gender == 'Male':
    salutation = 'Sir'
    initials = 'his'
elif gender == 'Female':
    salutation = 'Madam'
    initials = 'her'

# creating the letter template
#fd = open("template.txt", "x")
# writing into the template
fd = open("template.txt","w")
fd.write("Name: "+debtor_name)
fd.write("\n")
fd.write("\n")
fd.write("Email: "+email)
fd.write("\n")
fd.write("\n")
fd.write("Phone Number: "+phone)
fd.write("\n")
fd.write("\n")
fd.write("Dear "+salutation)
fd.write("\n")
fd.write("\n")
fd.write("RE: Demand Notice ")
fd.write("\n")
fd.write("\n")
fd.write("We are writing on behalf of our client to ask that you settle "+ initials+ " debt amounting to Ksh: " +str(amount)+ " by end of next week."+ "\n"+ "Failure to settle the amount or communicate about the same will attract recovery measures. ")
fd.write("\n")
fd.write("\n")
fd.write("Yours Faithfully")
fd.write("\n")
fd.write("Nexus Debt Collectors")
fd.close()




