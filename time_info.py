'''Provides time elements'''
from datetime import datetime

class Time:
    '''Provides current time elements'''

    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    date = now.strftime('%B %d, %Y')
    month = now.strftime('%B')
    weekday = now.strftime('%A')

    def get_date(self):
        '''Gets current date'''

        return self.date

    def get_current_time(self):
        '''Gets current time'''

        return self.current_time

    def get_month(self):
        '''Gets current month'''

        return self.month

    def get_day_of_week(self):
        '''Gets current week of day'''

        return self.weekday
