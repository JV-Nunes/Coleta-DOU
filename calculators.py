import datetime

class Calculator:
    def __init__(self):
        pass
    
    def get_dates(self):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        day_before_yesterday = yesterday - datetime.timedelta(days=1)

        return self.to_str(today), self.to_str(yesterday), self.to_str(day_before_yesterday)

    def to_str(self, date):
        return date.strftime("%Y-%m-%d")





if __name__=='__main__':
    calc = Calculator()
    print(calc.to_str(calc.get_yesterday()))
