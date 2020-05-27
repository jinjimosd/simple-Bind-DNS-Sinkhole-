import datetime

class util:


    def __init__(self):

        self.f = open("resources/date_update.txt","a+")

    def save_datetime_update(self):

        datetime_update = str(datetime.datetime.now()) + "\r\n"
        self.f.write(datetime_update)
        self.f.close()


        