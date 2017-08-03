# class MathDojo(object):
#     total = 0

#     def add(self, *y):
#         for i in y:
#             self.total += i
#         # print self.total
#         return self

#     def subtract(self, *y):
#         for i in y:
#             self.total -= i
#         # print self.total
#         return self



# md = MathDojo()
# print md.add(2,4,5,3,32).subtract(3,2,1).total

#part 2

class MathDojo(object):
    total = 0

    def add(self, *y):
        for i in y:
            if type(i) == int:
                self.total += i
            else:
                for z in i:
                    self.total += z
        # print self.total
        return self

    def subtract(self, *y):
        for i in y:
            if type(i) == int:
                self.total -= i
            else:
                for z in i:
                    self.total -= z
        # print self.total
        return self




md = MathDojo()
print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).total

