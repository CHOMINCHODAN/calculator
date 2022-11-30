class Calculator:
    def __init__(self):
        self.current_value = 0

    def get_current_value(self):
        return self.current_value

    def add(self, get_value: int):          # c++와 같이 타입 형태 정해주면 주면 좋다
        #print("get value : %d" % get_value)
        self.current_value += get_value

    def sub(self, get_value: int):
        #print("get value: %d" % get_value )
        self.current_value -= get_value

    def mul(self, get_value: int):
        #print("get value: %d" % get_value )
        self.current_value *= get_value

    def div(self, get_value: int):
        #print("get value: %d" % get_value )
        self.current_value /= get_value

    def tmb(self, get_value: int):
        #print("get value: %d" % get_value )
        self.current_value **= get_value



if __name__ == '__main__':
    calculator = Calculator()

    while True:
        print("계산기 시작")
        print("1.더하기")
        print("2.빼기")
        print("3.곱하기")
        print("4.나누기")
        print("5.몇승")

        choice = input("선택 하세요(1/2/3/4/5):")
        input_value = 0
        try:
            input_value = int(input("숫자 : "))
        except ValueError:

            print("숫자만 적어주세요")

        if choice == '1':
            calculator.add(get_value=input_value)   # 두개다 가능
        elif choice == '2':
            calculator.sub(input_value)
        elif choice == '3':
            calculator.mul(input_value)
        elif choice == '4':
            calculator.div(input_value)
        elif choice == '5':
            calculator.tmb(input_value)


        print("calculator current value : %d" % calculator.get_current_value())
