def add(x, y):
  return x + y

def sub(x, y):
    return x - y

def mul(x, y):
     return x * y

def div(x, y):
    return x / y

def pow(x,y):
    return x ** y
print("사칙연산을 선택 하세요.")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")
print("5.몇승")

choice = input("선택 하세요(1/2/3/4):")

num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", sub(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", mul(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", div(num1,num2))

elif choice == '5':
    print(num1,"**",num2,"=", pow(num1,num2))

else:
    print("잘못된 선택")

        # 들여쓰기 힘들네....