from datetime import datetime


class Time:
    now = datetime.now()
    month = now.strftime('%B')
    weekday = now.strftime('%A')

    def get_month(self):
        return self.month

    def get_weekday(self):
        return self.weekday
