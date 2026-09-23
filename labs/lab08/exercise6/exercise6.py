position = input()
overtime_hours = int(input())
is_weekend = input()


if position == "Manager":
    rate = 30
elif position == "Supervisor":
    rate = 20
elif position == "Staff":
    rate = 15
else:
    rate = 8

if overtime_hours <= 8:
    overtime_pay = overtime_hours * rate * 1.5
else:
    overtime_pay = 8 * rate * 1.5 + (overtime_hours - 8) * rate * 2

if is_weekend == "yes":
    overtime_pay = overtime_pay + overtime_hours * 5



print(overtime_pay)
