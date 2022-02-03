from datetime import timedelta, datetime

from timing import Conference_Mgmt


class Track_Time(Conference_Mgmt):
    id = 0

    def __init__(self):
        super(Track_Time, self).__init__()
        Track_Time.id += 1
        self.talks = {}
        self.talk_list = Track_Time.extract_input()

    @staticmethod
    def extract_input():
        """
        This function extracts the data from the given input file 
        """
        talks = {}
        lines = []
        try:
            lines = [line.strip() for line in open('input-test-two-talks.txt')]
        except FileNotFoundError as e:
            print('File Not Found', e)
        if len(lines) != 0:
            for line in lines:
                title, minutes = line.rsplit(maxsplit=1)
                try:
                    minutes = int(minutes[:-3])
                # negative indexing raises error, so it means it's lightning
                except ValueError:
                    minutes = 5
                talks[line] = minutes
            return talks

        else:
            print("File Empty")


    def get_talks(self, start_talk, end_talk):
        """
        This function assigns the start and end times for the talks
        """
        start = timedelta(hours=start_talk)
        for key, value in list(self.talk_list.items()):
            prev = start + timedelta(minutes=int(value))
            if prev <= timedelta(hours=end_talk):
                self.talks[(datetime.min + start).strftime('%I:%M %p')] = key
                self.talk_list.popitem()
                start += timedelta(minutes=int(value))
        return self.talks


    def show_output(self):
        """
        This function gives the result according the start and end times for the talks
        """
        while self.talk_list:
            print('Track_Time %s' % Track_Time.id)
            self.__prepare_output(9, 12)
            print('%s - %s' % (self.lunch, 'Lunch'))
            self.__prepare_output(13, 17)
            print('%s - %s' % (self.day_end, 'Networking Event'))
            Track_Time.id += 1
        

    def __prepare_output(self, start, end):
        for time, title in sorted(self.get_talks(start, end).items()):
            print(time, '-', title)
        # clear previous entries
        self.talks.clear()


if __name__ == '__main__':
    """
        This is main function creating the object for the Track_Time class
    """
    a = Track_Time()
    a.show_output()