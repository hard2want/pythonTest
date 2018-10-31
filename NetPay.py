# promt user for their name
name = input("What is your name? ")

# prompt user for their hourly rate, remember to make it a float
hourlyPay = float(input("How much do you get paid by the hour? "))

# promt user for the number of hours they worked, remember to make it a float
weeklyHoursWorked=float(input("How many hours do you work each week? "))

# calculate the rate per hour for overtime hours
overtimeHourlyPay = hourlyPay * 1.5


if weeklyHoursWorked <= 40:
    weeklyOvertimeHoursWorked=0
else:
    weeklyOvertimeHoursWorked=weeklyHoursWorked-40

if weeklyHoursWorked+weeklyOvertimeHoursWorked <= 40:
   weeklySalary=weeklyHoursWorked*hourlyPay
else: 
    weeklySalary=weeklyHoursWorked*hourlyPay+weeklyOvertimeHoursWorked*overtimeHourlyPay
grossSalary=weeklySalary*52
taxes=grossSalary*.1
netPay=grossSalary-taxes
print ( name, "You earn", hourlyPay, " dollars an hour and work", weeklyHoursWorked+weeklyOvertimeHoursWorked, "hours a week. Your gross pay comes out to", grossSalary, "After paying", taxes, "dollars in taxes, your net pay comes out to", netPay)


#if weeklyHoursWorked <=40:
#    weeklyHoursWorked=weeklyHoursWorked
#else:
#    weeklyHoursWorked=40
