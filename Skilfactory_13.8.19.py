number_of_tickets = int(input())

age_of_visitors = [int(input()) for _ in range(number_of_tickets)]

sum_of_tickets = 0

for i in age_of_visitors:
    if 17 < i < 25:
        sum_of_tickets += 990
    elif i > 24:
        sum_of_tickets += 1390

if len(age_of_visitors) > 3:
    sum_of_tickets = sum_of_tickets * 0.9

print(sum_of_tickets)