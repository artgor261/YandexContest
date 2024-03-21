class Intern:
    def __init__(self, line):
        self.line = line
        self.__count = 0
        self.__birthday = 0
        self.__index = 0
        self.__sum = 0
        self.__result = 0

    def get_encrypt(self):
        self.__unique(self.line)
        self.__birthday_sum(self.line)
        self.__first_index(self.line)
        self.__set_sum()
        self.__convert_to_16(self.__sum)
        print(self.__result, end=' ')

    def __unique(self, line):
        s = set()
        for c in line:
            if c == '\n':
                pass
            elif c.isdigit():
                pass
            elif c == ',':
                pass
            else:
                s.add(c)
        self.__count = len(s)

    def __birthday_sum(self, line):
        nums = list()
        for c in line:
            if c.isdigit():
                nums.append(c)
        nums = list(map(int, nums))
        self.__birthday = sum(nums[::-1][4:]) * 64

    def __first_index(self, line):
        self.__index = (ord(line[0]) - 64) * 256

    def __set_sum(self):
        self.__sum = self.__count + self.__birthday + self.__index

    def __convert_to_16(self, number):
        num = list()
        while number > 0:
            mod = number % 16
            num.append(mod)
            number = number // 16
        for i, n in enumerate(num):
            if n == 10:
                num[i] = 'A'
            elif n == 11:
                num[i] = 'B'
            elif n == 12:
                num[i] = 'C'
            elif n == 13:
                num[i] = 'D'
            elif n == 14:
                num[i] = 'E'
            elif n == 15:
                num[i] = 'F'
        num = num[:3][::-1]
        if len(num) < 3:
            if len(num) == 2:
                num.append(0)
            elif len(num) == 1:
                num.append(0)
                num.append(0)
        self.__result = ''.join(map(str, num))


def main():
    file = open("input.txt", 'r')
    for line in file:
        intern = Intern(line)
        intern.get_encrypt()


main()
