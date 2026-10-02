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


raw_input = input("inch 단위의 숫자를 입력해주세요: ")
inch = int(raw_input)
cm = inch * 2.54
print(inch, "inch는 cm 단위로", cm, "cm입니다.")

# format() = 문자열이 가지고 있는 함수. {}를 포함한 문자열 뒤에 .format() / 중괄호 개수 = format() 안에 들어가는 값의 개수
 
format_a = "{}만원".format(5000)
format_b = "파이썬 열공해 첫 연봉 {}만원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

#  {} 개수가 forat() 안에 들어가는 값의 개수보다 많으면 IndexError 발생

# upper() = 문자열의 알파벳을 모두 대문자로 변환, lower() = 문자열의 알파벳을 모두 소문자로 변환
# strip() = 문자열의 양쪽 공백 제거, lstrip() = 문자열의 왼쪽 공백 제거, rstrip() = 문자열의 오른쪽 공백 제거
# isㅇㅇ() = 문자열이 특정 조건을 만족하는지 확인하는 함수 > 출력은 True or False
# find() = 문자열에서 특정 문자열을 찾아서 위치를 반환, 없으면 -1 반환
# rfind() = 문자열에서 특정 문자열을 뒤에서부터 찾아서 위치를 반환, 없으면 -1 반환
# split() = 문자열을 특정 구분자로 나누어 리스트로 반환
# in 연산자 = 특정 문자열이 포함되어 있는지 확인 > 출력은 True or False
# f-string = 문자열 앞에 f를 붙이고, {} 안에 변수명을 넣으면 해당 변수의 값이 문자열 안에 들어감

# 보통 f-string을 format()보다 더 많이 사용함 but 문자열 내용이 너무 많을 때, 데이터를 리스트에 담아서 사용할 때 format()이 더 유리함
pi = 3.141592
r = float(input("구의 반지름을 입력해주세요> "))
부피 = (4/3) * 3.14 * (r ** 3)
겉넓이 = 4 * 3.14 * (r ** 2)
print(f"구의 부피는 {부피}입니다.")
print(f"구의 겉넓이는 {겉넓이}입니다.")

밑변 = float(input("밑변의 길이를 입력해주세요> "))
높이 = float(input("높이의 길이를 입력해주세요> "))
빗변 = (밑변 ** 2 + 높이 ** 2) ** 0.5
print(f"빗변의 길이는 {빗변}입니다.")

