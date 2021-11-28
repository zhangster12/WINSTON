'''Provides time elements'''
from datetime import datetime

class Time:
    '''Provides current time elements'''

    now = datetime.now()
    month = now.strftime('%B')
    weekday = now.strftime('%A')

    def get_month(self):
        '''Gets current month'''

        return self.month

    def get_day_of_week(self):
        '''Gets current week of day'''

        return self.weekday
