#List / 리스트, 배열
# 1. 여러개 or 순서대로 or 내용 바뀜 (엘레먼트)

x = list()
x = [1,2,3,4]
print(x)

x = [1,2,3]
x.append(4)
x.append(5)
x.pop()
x[3] = 5
print(x)

# list와 tuple의 차이점 : tuple은 나중에 내용물 바꿀 수 없음.
# list = 내용물을 바꿀 수 있는 자료구조 : mutable
# tuple = 내용물을 바꿀 수 없는 자료구조 : immutable
# tuple 자료 구조로 나중에 버그 안생기게 하려고 쓰는 거임

x = tuple()
x = (1,2,3)
print(x)

x = set()
x.add(1)
x.add(2)
x = {1,2}
x = set((1,2,3))
print(x)
# 1. 순서가 뒤죽박죽이 될 수 있다.(속도)
# 2. Set도 immutable
# 3. 어떤 내용물이 있는지 확인하는 게 빠르다.

# Key, Value
x = {}
x = dict()
x["이름"] = "abc"
x["나이"] = 20
x["위치"] = "한국"
print(x["이름"])
# 1. 순서가 뒤죽박죽일 수 있다.
# 2. Key에 해당되는 값을 나중에 불러오고 싶을 때
# 3. 어떤 Key가 자료 구조안에 들어있는지 빨리 알고 싶을 때

# set vs dictionary
# set : key-value가 필요 없고 key만 필요할 때
# dictionary : key-value가 필요할 때

# list + tuple vs set + dictionary
# list + tuple : 
# 1) ordered - 순서가 정해져 있다 - 내용물이 자료구조에 들어간 순서대로 저장된다
# 2) 멤버쉽 검색이 느리다 - 어떤 엘레먼트가 들어있는지 파악하기가 순서대로 돼서
# set + dictionary :
# 1) unordered - 내용물이 자료구조에 들어간 순서대로 저장되지 않을 수 있다
# 2) 멤버쉽 검색이 빠르다