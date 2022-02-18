import time
import datetime
import pytz

def get_timestamp():
    return int(time.time())

def get_datetime():
    time_obj = datetime.datetime.now(pytz.timezone('Asia/Chongqing'))
    return datetime.datetime.strptime(time_obj.strftime("%Y%m%d%H%M%S"), "%Y%m%d%H%M%S")  

if __name__ == "__main__":
    print(get_datetime())