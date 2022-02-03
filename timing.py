from datetime import timedelta, datetime

class Conference_Mgmt:
    def __init__(self):
        """
        This function creates specified start times and end times 
        """
    
        self.morning_start = (datetime.min+ timedelta(hours=9)).strftime('%I:%M %p')
        self.lunch = (datetime.min+ timedelta(hours=12)).strftime('%I:%M %p')
        self.afternoon_start = (datetime.min+ timedelta(hours=13)).strftime('%I:%M %p')
        self.day_end = (datetime.min+ timedelta(hours=17)).strftime('%I:%M %p')

if __name__ == '__main__':
    a = Conference_Mgmt()
    print(a.afternoon_start)