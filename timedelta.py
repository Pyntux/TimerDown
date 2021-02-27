
# Timedelta function demonstration
import datetime
from datetime import timedelta


# Using current time
time = datetime.datetime.now()


# Trenutno vreme koje vuče odozgo
day = time.day
mounth = time.month
hour = time.hour
minute = time.minute

# spinbox vrednost, za koliko minuta da ga ugasi
spinbox = 10
# vrednost u sekundama, to čita timedelta
min_sec = spinbox * 60
hour_sec = spinbox * 3600


# Sadašnje vreme + spinbox vrednost u sekundama da je buduće vreme
future = time + datetime.timedelta(seconds=min_sec)
future2 = time + datetime.timedelta(seconds=hour_sec)

print(f"Vreme kada nameštam gašenje: {day}.{mounth}. u {hour}:{minute}h")
print(
    f"Vreme kada će se ugasiti ako je spiner za minute: {future.day}.{future.month}. u {future.hour}:{future.minute}h")
print(
    f"Vreme kada će se ugasiti ako je spiner za sate: {future2.day}.{future2.month}. u {future2.hour}:{future2.minute}h")
