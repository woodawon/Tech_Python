# 클래스
class Person:
    # constructor - 생성자
    def __init__(self, name, age, hometown):
        self.name = name
        self.age = age
        self.hometown = hometown

    def say_hello(self):
        print("안녕 나는 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")

    def introduce(self):
      print("내 고향은 " + self.hometown)


# wonie = Person("다원", 20, "서울")
# wonie.say_hello()
# wonie.introduce()

# 상속
# Programmer는 Person을 상속하는 클래스임
class Programmer(Person):
  def code(self):
    print("나는 코딩을 한다")

class Chef(Person):
  def cook(self):
    print("나는 요리를 한다")

p = Programmer("민희", 20, "대구")
c = Chef("민준", 20, "울산")

p.say_hello(), 
p.introduce()
p.code()