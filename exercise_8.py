ovr = []
pay = []
def Overtime_cal(hrs):
    if hrs <= 50:
        overtime = 300 * hrs
    elif hrs > 50:
        overtime = 300 * (50 - hrs)
    ovr.append(overtime)
def payeCalc(sal):
    if sal >= 50000:
        rate = 0.14
        paye = sal * rate
    elif sal >= 40000 and sal < 50000:
        rate = 0.12
        paye = sal * rate
    elif sal >= 35000 and sal < 40000:
        rate = 0.11
        paye = sal * rate
    elif sal >= 25000 and sal < 35000:
        rate = 0.08
        paye = sal * rate
    elif sal >= 16000 and sal < 25000:
        rate = 0.05
        paye = sal * rate
    elif sal >= 9500 and sal < 16000:
        rate = 0.03
        paye = sal * rate
    elif sal < 9500:
        rate = 0.0
        paye = sal * rate
    pay.append(paye)
def Display():
    # capturing employee salary and overtime hours
    salary = int(input("Enter Employee Basic Salary: "))
    hours = int(input("Enter Employee Overtime Hours: "))

    #constants
    nssf = 80.00
    nhif = 200.00
    service = 100.00


    payeCalc(salary)
    Overtime_cal(hours)
    print(pay[0])
    print(ovr[0])

    gross_pay = salary + ovr[0]
    net_pay = gross_pay - (pay[0] + nssf + nhif +service)
    print("Employee Gross Pay is: "+str(gross_pay))
    print("Employee Net Pay is: "+str(net_pay))

Display()
