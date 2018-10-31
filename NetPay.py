name=input("What is your name? ")
hourlyPay=float(input("How much do you get paid by the hour? "))
overtimeHourlyPay=hourlyPay*1.5
weeklyHoursWorked=float(input("How many hours do you work each week? "))
if weeklyHoursWorked <= 40:
    weeklyOvertimeHoursWorked=0
else:
    weeklyOvertimeHoursWorked=weeklyHoursWorked-40
if weeklyHoursWorked <=40:
    weeklyHoursWorked=weeklyHoursWorked
else:
    weeklyHoursWorked=40
if weeklyHoursWorked+weeklyOvertimeHoursWorked <= 40:
   weeklySalary=weeklyHoursWorked*hourlyPay
else: 
    weeklySalary=weeklyHoursWorked*hourlyPay+weeklyOvertimeHoursWorked*overtimeHourlyPay
grossSalary=weeklySalary*52
taxes=grossSalary*.1
netPay=grossSalary-taxes
print ( name, "You earn", hourlyPay, " dollars an hour and work", weeklyHoursWorked+weeklyOvertimeHoursWorked, "hours a week. Your gross pay comes out to", grossSalary, "After paying", taxes, "dollars in taxes, your net pay comes out to", netPay)

