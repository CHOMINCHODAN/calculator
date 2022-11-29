class Calcul:  # 클래스 선언
    def __init__(self, first, second):  # 함수(메소드) 생성 ( 맨 처음 오는 매개 변수 객체 그 자체 두에 오는건 값들)
        self.first = first  # 매소드 수행문
        self.second = second  # 매소드 수행문

    # 더하기 기능 만들기
    def add(self):  # 더하기에 대한 메소드를 생성한다. 그리고 객체를 지정하여 위에 꺼 활용
        result = self.first + self.second  # 결과를 매소드 수행문 활용
        return result
        # print(a.mul())  곱하기

    # 곱하기 하다가 한가지 알게 된점 다시 한번더 함수는 항상 위에 선언하는게 중요하다. 안그럼 에러뜬다.
    def mul(self):
        result = self.first * self.second
        return result

    # print(a.sub())  빼기
    def sub(self):
        result = self.first - self.second
        return result

    # print(a.div())  나누기
    def div(self):
        result = self.first / self.second
        return result


