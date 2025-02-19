import requests
import csv
from datetime import datetime
import os


API_KEY = os.getenv("OPENWEATHER_APL_KEY")
CITY = "Seoul"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
print(data)
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
# main -> temp
# main -> humidity
# weather -> description
timezone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(temp, humidity, description, timezone)

# 위의 4개의 데이터를 가지는 csv파일 생성성
csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "description"]

# csv 가 존재하면-> True
# csv 가 존재하지 않으면 -> False
file_exist = os.path.isfile(csv_filename)


# mode ="a"-> if not file -> create
# if is file -> write 모드 
with open(csv_filename, "a", newline="") as file:
    writer = csv.writer(file)


    # 파일이 존재하지 않는다 -> 헤더가 없다. 
    if not file_exist:
        writer.writerow(header)

    writer.writerow(["timezone", "temp", "humidity", "description"])

    print("csv 저장완료")
