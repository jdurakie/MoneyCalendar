import datetime

ONE_DAY = datetime.timedelta(days=1)
TODAY = datetime.datetime.date(datetime.datetime.now())
class MoneyCalendar(object):

    def __init__(self, startDate, numDays):
        self.calendar = []
        self.dates = {}
        self.startDate = startDate
        self.numDays = numDays
        self.lastDay = startDate + (numDays * ONE_DAY)

        for i in range(0, numDays):
            currentDate = startDate + (i * ONE_DAY)
            dayDict = {
                        "date": startDate + (i * ONE_DAY),
                        "transactions": {},
                        "total": 0 #day end total
                      }
            self.calendar.append(dayDict)
            self.dates[currentDate] = self.calendar[-1]

    def addTransaction(self, queryDate, label, amount):
        self.dates[queryDate]['transactions'][label] = amount

    def recalculateTotals(self):
        for i in range(0, self.numDays):
            prevDayTotal = 0
            if i > 0:
                prevDayTotal = self.calendar[i - 1]['total']
            todaysTransactions = self.calendar[i]['transactions']
            for _, amount in todaysTransactions.items():
                prevDayTotal += amount
            self.calendar[i]['total'] = prevDayTotal

    def printCalendar(self):
        for i in range(0, self.numDays):
            print(self.calendar[i])

    def addRecurringTransaction(self, daysBetween, startDay, label, amount):
        transactionDay = startDay
        while transactionDay < self.lastDay:
            self.addTransaction(transactionDay, label, amount)
            transactionDay += ONE_DAY * daysBetween

        self.recalculateTotals()

    def printDate(self, date):
        pass

    def import_existing(self):
        pass


mc = MoneyCalendar(TODAY, 20)
mc.addTransaction(TODAY, "starting", 100)
mc.addTransaction(TODAY + (ONE_DAY * 4), "soda", -1.2)
mc.recalculateTotals()
mc.addRecurringTransaction(daysBetween=7,
                           startDay=TODAY,
                           label="salary",
                           amount=10.0)
mc.addRecurringTransaction(daysBetween=7,
                           startDay=TODAY + ONE_DAY,
                           label="bill",
                           amount=-4.20)
mc.printCalendar()
