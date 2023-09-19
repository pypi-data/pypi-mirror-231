import json
import datetime
import urllib.request
from typing import List
from dateutil.relativedelta import relativedelta


class QueueChecker:

    loc = {
        "KAPA": "189",
        "KAPO": "198",
        "KOOL": "207",
        "WADL": "217",
        "WAIA": "226"
    }


    def __init__(self, location: str, target_month: int, target_day: int, target_year: int, scope: int = 3) -> None:
        self.location = location
        self.scope = scope
        self.target_month = target_month
        self.target_day = target_day
        self.target_year = target_year
        

    @property
    def get_available_dates(self) -> List[str]:
        available_dates = []
        target_date = datetime.date.today().replace(month=self.target_month, day=self.target_day, year=self.target_year)
        with urllib.request.urlopen(self.date_url) as response:
            dates = json.loads(response.read().decode("utf-8"))["data"]
        for date in dates: 
            date = datetime.datetime.strptime(date, '%m/%d/%Y').date()
            if date <= target_date:
                available_dates.append(date.strftime("%Y-%m-%d"))
        return available_dates

    
    @property
    def date_url(self) -> str:
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        last_date = (datetime.date.today() + relativedelta(months=self.scope)).strftime("%Y-%m-%d")
        return f"https://alohaq.honolulu.gov/wrk_availability.php?l={self.location}&s={self.loc[self.location]}&d={current_date}&m={last_date}&t=all"
    

    def time_url(self, date) -> str:
        return f"https://alohaq.honolulu.gov/wrk_get_availability.php?l={self.location}&s={self.loc[self.location]}&d={date}"


    def get_available_time(self, date) -> List[str]:
        with urllib.request.urlopen(self.time_url(date)) as response:
            times = json.loads(response.read().decode("utf-8"))
        return times