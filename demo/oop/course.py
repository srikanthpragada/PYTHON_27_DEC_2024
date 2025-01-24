
class Course:
    # constructor
    def __init__(self, title, fee, duration = 30):
        # Object Attributes
        self.title = title
        self.fee = fee
        self.duration = duration

    def show(self):
        print(self.title)
        print(self.fee)
        print(self.duration)

    def getnetfee(self):
        return self.fee + self.fee * 0.18



# create object of Course
c1 = Course('Data Science', 20000)
c1.show()
print(c1.getnetfee())


c2 = Course('AWS', 10000, 20)
c2.show()






