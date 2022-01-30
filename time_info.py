'''Provides time elements'''
from datetime import datetime

class Time:
    '''Provides current time elements'''

    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    date = now.strftime('%B %d, %Y')
    year = now.strftime('%Y')
    month = now.strftime('%B')
    weekday = now.strftime('%A')

    def check_phrase_time(self, phrase):
        if 'month' in phrase:
            return self.month

        elif 'day of week' in phrase:
            return self.weekday

        elif 'what time is it' in phrase:
            return self.current_time

        elif 'date' in phrase:
            return self.date

        elif 'last year' in phrase:
            return int(self.year) - 1
        
        elif 'next year' in phrase:
            return int(self.year) + 1

        elif 'year' in phrase:
            return self.year