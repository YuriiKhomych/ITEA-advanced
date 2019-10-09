# example 1


class ImproveEnglish:
    def get_schedule(self, your_level):
        if your_level in ['A1', 'A2']:
            return self.schedule_a()

        if your_level in ['B1', 'B2']:
            return self.schedule_b()

        if your_level in ['C1', 'C2']:
            return self.schedule_c()

    def schedule_a(self):
        print('We have lessons in the morning, at 8:30 a.m')
        return self

    def schedule_b(self):
        print("Unfortunately now we don't have groups align to your level")
        return self

    def schedule_c(self):
        print('We have lessons in the evening, at 7:00 p.m')
        return self


you = ImproveEnglish()
you.get_schedule('C1')

# example 2


class Profit:
    def your_profit(self, salary, charges):
        if charges == salary:
            return self.find_job()
        if charges > salary:
            return self.spend_less()
        if charges < salary:
            return self.calc_profit(salary, charges)

    def find_job(self):
        print('You need to find a better job')
        return self

    def spend_less(self):
        print('You should try to spend less')
        return self

    def calc_profit(self,  salary, charges):
        profit = salary - charges
        print('Your profit is:', profit)
        return self


p = Profit()
p.your_profit(1000, 900)






