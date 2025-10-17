from mammals import Dog
from birds import Eagle

my_dog = Dog(name="초코")
my_eagle = Eagle(name="망고")


print("====================================")
print("          동물 정보 출력")
print("====================================")

# Dog 객체의 정보 출력
print(f"{my_dog.info()}")
# Eagle 객체의 정보 출력
print(f"{my_eagle.info()}")
print("====================================")