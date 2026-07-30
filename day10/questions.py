#Q1
def fizzbuzz(num):
    for i in range (1,num+1):
        if i%3==0:
            print ("Fizz")
        elif i%5==0:
            print ("Buzz")
        elif i%3 and i%5==0:
            print ("FizzBuzz")
        else:
            print(i)
fizzbuzz(15)


#Q2
def count_vowels(s):
    vowel = {"a", "e", "i", "o", "u"}
    count=0
    s=s.lower()
    for i in s:
        if i in vowel:
            count+=1
    return count
print(count_vowels("hello world"))
print(count_vowels("PYTHON"))


#Q3
def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    rev=[]
    for i in s:
        rev.append(i)
    revers=""
    while rev:
        revers+=rev.pop()
    return revers==s
print (is_palindrome("racecar"))
print (is_palindrome("A man a plan a canal Panama"))


#Q4
from collections import Counter
def find_duplicates(lst):
    counts = Counter(lst)
    duplicates = []
    for i, count in counts.items():
        if count > 1:
            duplicates.append(i)
    return duplicates
print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
print(find_duplicates([1, 2, 3]))
print(find_duplicates([5, 5, 5]))


#Q5
def word_frequency(text):
    text=text.lower()
    for chars in ".,?!":
        text=text.replace(chars,"")
    phrase=text.split()
    freq={}
    for word in phrase:
        freq[word]=freq.get(word,0)+1
    return freq
print(word_frequency("Hello world hello"))
print(word_frequency("python, python is great"))


#Q6
def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


#Q7
def read_numbers(filename):
    numbers = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                try:
                    numbers.append(int(line))
                except ValueError:
                    print(f"Warning: '{line}' is not a valid integer.")
    except FileNotFoundError:
        print("File not found.")
        return []
    return numbers
print(read_numbers("numbers.txt"))


#Q8
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance
    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"
acc = BankAccount("Alice", 500)
acc.deposit(400)
print(acc)
acc.withdraw(300)
print(acc)
try:
    acc.withdraw(1000)
except ValueError as e:
    print(e)


#Q9
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}
    def add_grade(self, subject, score):
        self.grades[subject] = score
    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    def highest(self):
        if not self.grades:
            return None
        return max(self.grades.items(), key=lambda item: item[1])
    def __repr__(self):
        return f"Student(name='{self.name}', grades={len(self.grades)})"
s = Student("Ali")
s.add_grade("Math", 90)
s.add_grade("Science", 85)
s.add_grade("English", 92)
print(s)
print(s.average())
print(s.highest())


#Q10
from abc import ABC, abstractmethod
PI = 3.14159
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def describe(self):
        print(f"I am a {self.__class__.__name__} with area {self.area():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return PI * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(8, 2)
]
for shape in shapes:
    shape.describe()
print("Total Area:", total_area(shapes))


#Q11
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    @abstractmethod
    def pay(self):
        pass

class FullTimeEmployee(Employee):
    def pay(self):
        return self.base_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def pay(self):
        return self.hourly_rate * self.hours_worked
    
class ContractEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
    def pay(self):
        return self.base_salary + self.bonus
    
def print_payroll(employees):
    for employee in employees:
        print(f"{employee.name}: {employee.pay()}")
employees = [
    FullTimeEmployee("Abebe", 20000),
    PartTimeEmployee("Melat", 200, 40),
    ContractEmployee("Kebede", 15000, 3000)
]
print_payroll(employees)


#Q2
from abc import ABC, abstractmethod
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailChannel(NotificationChannel):
    def __init__(self, server):
        self.server = server
    def send(self, message):
        print(f"Email ({self.server}): {message}")

class SMSChannel(NotificationChannel):
    def __init__(self, phone):
        self.phone = phone
    def send(self, message):
        print(f"SMS to {self.phone}: {message}")

class PushChannel(NotificationChannel):
    def __init__(self, device):
        self.device = device
    def send(self, message):
        print(f"Push to {self.device}: {message}")

class NotificationService:
    def __init__(self):
        self.channels = []
    def add_channel(self, channel):
        self.channels.append(channel)
    def notify_all(self, message):
        for channel in self.channels:
            channel.send(message)
service = NotificationService()
service.add_channel(EmailChannel("smtp.example.com"))
service.add_channel(SMSChannel("+251900000000"))
service.add_channel(PushChannel("Alem's Phone"))
service.notify_all("Server is down!")


#Q13
class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance
    def log(self, level, message):
        self.logs.append(f"[{level}] {message}")
    def get_logs(self):
        return self.logs
logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)

logger1.log("INFO", "Program started")
logger2.log("ERROR", "File not found")
print(logger1.get_logs())


#Q14
def is_valid(s):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))


#Q15
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))


#Q16
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(1)
print(ms.get_min())
print(ms.pop())
print(ms.get_min())
print(ms.top())


#Q17
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search([1,3,5,7,9,11], 7))
print(binary_search([1,3,5,7,9,11], 6))
print(binary_search([], 5))


#Q18
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(flatten([1,[2,3],[4,[5,6]]]))
print(flatten([1,[2,[3,[4,[5]]]]]))
print(flatten([]))


#Q19
def max_water(height):
    left = 0
    right = len(height) - 1
    maximum = 0
    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width
        maximum = max(maximum, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maximum
print(max_water([1,8,6,2,5,4,8,3,7]))
print(max_water([1,1]))


#Q20
def longest_unique(s):
    seen = set()
    left = 0
    longest = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        longest = max(longest, right - left + 1)
    return longest
print(longest_unique("abcabcbb"))
print(longest_unique("bbbbb"))
print(longest_unique("pwwkew"))
print(longest_unique(""))