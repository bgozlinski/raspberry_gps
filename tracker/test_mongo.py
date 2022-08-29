from pihat import *
from config import *
from mpu import checkMPU
from mongoDB import mongoDB
from time import sleepping 


print(f"Sprawdzam polaczenie do bazy danych ...")
mongoDB(TASK_NAME, TEMPORARY_COORDINATES_FILE, DEVICE_ID)
print(f"Polaczenie zakonczono.")