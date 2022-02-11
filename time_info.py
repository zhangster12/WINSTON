'''Provides time elements'''
from datetime import datetime
from phrase import *

class Time:
    '''Provides current time elements'''

    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    hour_mil = now.strftime('%H')
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
        
        elif 'hour' in phrase:
            return self.hour_mil

        elif 'date' in phrase:
            return self.date

        elif check_all_phrase(phrase, ['year', 'years']):

            if 'years ago' in phrase:
                
                list_phrase = phrase.split('years', 1)[0].split(' ')
                length = len(list_phrase)
                return int(self.year) - int(list_phrase[length - 2])

            elif check_all_phrase(phrase, ['years later', 'years from now']):
                
                list_phrase = phrase.split('years', 1)[0].split(' ')
                length = len(list_phrase)
                return int(self.year) + int(list_phrase[length - 2])

            elif check_all_phrase(phrase, ['last year', '1 year ago']):
                return int(self.year) - 1
            
            elif 'next year' in phrase:
                return int(self.year) + 1

            else:
                return self.year