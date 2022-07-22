class Person:
  # constructor - 생성자
  def __init__(self, a, b):
    self.name = a
    self.age = b

  def say_hello(self):
    print("안녕 나는 " 
          + self.name + 
         " 그리고 나는"
         + str(self.age) + 
          " 살이야")

wonie = Person("워니", 20)
wonie.say_hello()