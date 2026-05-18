import streamlit as st

# 웹 앱의 제목과 설명 설정
st.title("🔢 가장 큰 수 찾기 프로그램")
st.write("세 개의 정수를 입력하면 가장 큰 수를 찾아줍니다.")

# 1. 스트림릿 위젯을 이용한 숫자 입력 받기 (기본값은 0으로 설정)
num1 = st.number_input("첫 번째 숫자를 입력하세요 (num1)", value=0, step=1)
num2 = st.number_input("두 번째 숫자를 입력하세요 (num2)", value=0, step=1)
num3 = st.number_input("세 번째 숫자를 입력하세요 (num3)", value=0, step=1)

# 결과를 저장할 변수 초기화
max_num = 0

# 2. 기존 코드가 가진 최댓값 비교 로직 (그대로 유지)
if num1 > num2:
    if num1 > num3:
        max_num = num1
    else:
        max_num = num3
else:
    if num2 > num3:
        max_num = num2
    else:
        max_num = num3

# 3. 배포된 웹 화면에 결과 출력하기
st.write("---")  # 구분선
st.success(f"🎉 입력한 숫자 중 가장 큰 수는 **{max_num}**입니다!")