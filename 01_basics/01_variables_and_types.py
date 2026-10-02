# statement(문장) = 실행할 수 있는 코드의 최소 단위
# program(프로그램) = statement + statement + statement + ...
# expression(표현식) = 값을 만들어내는 간단한 코드(값=숫자,수식,문자열 등)
# identifier(식별자) = 변수, 함수, 클래스 등의 이름 1.키워드사용금지 2.숫자로 시작금지 3.특수문자사용금지(단, _는 허용) 4.대소문자구분 5. 공백포함X
# 캐멀 케이스로 작성 = 클래스, 스네이크 케이스로 작성 = 변수, 함수 -> 뒤에 () 있으면 함수, 없으면 변수

# indexing and slicing = [], [:]
print("what is indexing?")
print("hello"[0])
print("hello"[1])
print("hello"[2])
print("hello"[3])
print("hello"[4])

print("back indexing")
print("hello"[-1])
print("hello"[-2])
print("hello"[-3])
print("hello"[-4])
print("hello"[-5])

print("slicing")
print("hello"[1:4])
print("hello"[1:3])
print("hello"[0:5])
print("hello"[:5])

# IndexError = 리스트/문자열의 수를 넘는 요소/글자를 선택할 때 발생

print(len("hello"))
print(type("hello"))

# type() = 자료형 확인, len() = 길이 확인

# 연산자 = +, -, *, /, //, %, **, ==, !=, >, <, >=, <=, and, or, not
# 복합연산자 = +=, -=, *=, /=, //=, %=, **=

# input(프롬프트문자열: 사용자에게 입력을 요구하는 안내 내용) > 결과는 무조건 문자열 자료형
string = input("입력> ")
print("자료:", string)
print("자료형:", type(string))

# casting(형변환) = 자료형을 다른 자료형으로 변환하는 것
# int() = 정수형으로 변환, float() = 실수형으로 변환, str() = 문자열형으로 변환
string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)

#----------------------------------------

float_a = float(input("첫 번째 숫자> "))
float_b = float(input("두 번째 숫자> "))

print("덧셈 결과:", float_a + float_b)
print("뺄셈 결과:", float_a - float_b)
print("곱셈 결과:", float_a * float_b)
print("나눗셈 결과:", float_a / float_b)

# ValueError = 자료형이 맞지 않을 때 발생 1. 숫자가 아닌 값을 숫자로 변환하려 할 때, 2. int() 함수로 변환 시 소수점이 있는 값을 변환하려 할 때



