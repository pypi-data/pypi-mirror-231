from faker import Faker

fake = Faker()
# print(fake.time_object())
# date1 = fake.date_object()
# print(date1)
# print(type(date1))
from datetime import date

from datetime import datetime, timedelta


# 生成过去两天的日期


def gendate():
    """
    生成一个最近两天的日期
    :return:
    """
    today = datetime.now().date()
    date1 = fake.date_between(start_date="-2d", end_date=today)
    return date1


def date2str(mydate, template="%Y-%m-%d"):
    """
    将一个日期对象转换成字符串
    :param mydate: 日期类型
    :param template: 日期格式
    :return: str
    """

    # 将日期对象转换为字符串
    date_string = mydate.strftime(template)
    return date_string

def time2str(mytime,template="%H:%M:%S"):
    """

    :param mytime: 时间类型
    :param template: 时间的格式
    :return: 时间的字符串形式
    """
    time_string = mytime.strftime(template)
    return time_string

from datetime import datetime, time
import random


def gentime(starthour=6, endhour=18):
    """
    生成白天的时间
    :param starthour: 白天开始的时间
    :param endhour: 白天结束的时间
    :return:
    """

    # 生成白天时间
    start_time = time(starthour, 0)  # 设置白天开始时间为6:00 AM
    end_time = time(endhour, 0)  # 设置白天结束时间为6:00 PM

    # 获取当前日期
    current_date = datetime.now().date()

    # 生成随机白天时间
    random_hour = random.randint(start_time.hour, end_time.hour)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    daytime = datetime.combine(current_date, time(random_hour, random_minute, random_second))

    # 打印生成的时间
    # print(daytime.time())
    return daytime.time()
