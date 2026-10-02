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

