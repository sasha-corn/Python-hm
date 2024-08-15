user_time = int(input('Введіть час у секундах: '))

days = user_time // 86400
rest = user_time % 86400
hours = rest // 3600
rest = rest % 3600
minuts = rest // 60
seconds = rest % 60

if days % 10 == 1 and days != 11:
    name_day = 'день'
elif 2 <= days % 10 <= 4 and not 11 < days < 15:
    name_day = 'дні'
else:
    name_day = 'днів'

print(f"{days} {name_day} {(str(hours)).zfill(2)}:{(str(minuts)).zfill(2)}:{(str(seconds)).zfill(2)}")
