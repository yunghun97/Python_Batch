import requests
import mysql.connector
import schedule
import time
from scheduleEvent.eventAction import expireCheck

schedule.every().day.at("16:53").do(expireCheck)

while True:
    schedule.run_pending()
    time.sleep(10)