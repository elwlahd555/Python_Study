import datetime
import random
import time

before = datetime.datetime.now()


# 201
def print_coin():
    print("비트코인")


# 202
print_coin()

# 203
for i in range(100):
    print_coin()


# 204
def print_coins():
    for j in range(100):
        print("비트코인")


# 205
def hello():
    print("Hi")


hello()


# 206
def message():
    print("A")
    print("B")


message()
print("C")
message()

# 207
print("A")


def message():
    print("B")


print("C")
message()
# 208
print("A")


def message1():
    print("B")


print("C")


def message2():
    print("D")


message1()
print("E")
message2()


# 209
def message1():
    print("A")


def message2():
    print("B")
    message1()


message2()


# 210
def message1():
    print("A")


def message2():
    print("B")


def message3():
    for i in range(3):
        message2()
        print("C")
    message1()


message3()


# 211
def 함수(문자열):
    print(문자열)


함수("안녕")
함수("Hi")


# 212
def 함수(a, b):
    print(a + b)


함수(3, 4)
함수(7, 8)


# 213
def 함수(문자열):
    print(문자열)


함수("문자열")


# 214
def 함수(a, b):
    print(a + b)


# 함수("안녕",3) 숫자가 아니라서 안됨
함수(5, 3)


# 215
def print_with_smile(word):
    print(word + ":D")


# 216
print_with_smile("안녕하세요")


# 217
def print_upper_price(price):
    print(price * 1.3)


# 218
def print_sum(a, b):
    print(a + b)


# 219
def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)


# 220
def print_max(a, b, c):
    print(max(a, b, c))


print_max(1, 3, 5)


# 221
def print_reverse(string):
    print(string[::-1])


print_reverse("python_algorithm")


# 222
def print_score(scores):
    print(sum(scores) / len(scores))


# 226
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1):
        print(line[x * 5: x * 5 + 5])


time.sleep(1)


# 227
def print_mxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1):
        print(line[x * num: x * num + num])


after = datetime.datetime.now()

print("before : ", before)
print("after : ", after)
print("during : ", after - before)


# 273

class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count


kim = Account("김민수", 100)
lee = Account("이민수", 100)
kim.get_account_num()
