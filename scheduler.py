import schedule
import time

def collect():
    # call collectors
    pass

schedule.every(5).minutes.do(collect)

while True:
    schedule.run_pending()
    time.sleep(1)
