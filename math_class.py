# takes in a number(s) and does order of operation depending on call
    # the asterisk before nums, declares almost like an array of all other numbers listed after the first integer(4, [5, 6])
class MathClass:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        sum = num
        for n in nums:
            sum += n
        self.result = sum
        return self
    def subtract(self, num, *nums):
        sum = num
        for n in nums:
            sum -= n
        self.result = sum
        return self
mc = MathClass()
# x = mc.add(4,5,6).subtract(2,5,1).result
x = mc.add(4,5,6).result
print(x)