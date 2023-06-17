import math
import tkinter as tk

def add_to_expression(value):
    current_expression = entry.get()
    new_expression = current_expression + str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_expression)

def calculate_expression():
    expression = entry.get()

    # 괄호 계산
    while "(" in expression:
        end = expression.find(")")
        start = expression.rfind("(", 0, end)
        if start == -1:
            result_label.config(text="잘못된 괄호 사용입니다.")
            return
        sub_expression = expression[start + 1:end]
        result = evaluate_expression(sub_expression)
        expression = expression[:start] + str(result) + expression[end + 1:]

    # 수식 계산
    result = evaluate_expression(expression)
    if result == "잘못된 연산":
        result_label.config(text="잘못된 연산입니다.")
    else:
        result_label.config(text="결과: " + str(result))

def evaluate_expression(expression):
    # 루트 계산
    while "√" in expression:
        root_start = expression.find("√")
        root_end = expression.find(" ", root_start)
        if root_end == -1:
            root_end = len(expression)
        number = float(expression[root_start + 1:root_end])
        root_result = math.sqrt(number)
        expression = expression[:root_start] + str(root_result) + expression[root_end:]

    # 사칙연산 계산
    try:
        result = eval(expression)
        if math.isnan(result):
            return "0으로 나눌 수 없습니다."
        else:
            return result
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    except:
        return "잘못된 연산입니다."

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("계산기")

# 입력 필드
entry = tk.Entry(window, width=30)
entry.pack()

# 숫자 및 연산 버튼
button_frame = tk.Frame(window)
button_frame.pack()

number_buttons = [
    [7, 8, 9, "+"],
    [4, 5, 6, "-"],
    [1, 2, 3, "*"],
    [0, "=", "/"]
]

for row in number_buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack()
    for value in row:
        button = tk.Button(button_row, text=str(value), command=lambda v=value: add_to_expression(v))
        button.pack(side=tk.LEFT)

# 괄호 버튼
parentheses_row = tk.Frame(button_frame)
parentheses_row.pack()
parentheses_buttons = ["(", ")", "√"]
for value in parentheses_buttons:
    button = tk.Button(parentheses_row, text=str(value), command=lambda v=value: add_to_expression(v))
    button.pack(side=tk.LEFT)

# 결과 텍스트
result_label = tk.Label(window, text="")
result_label.pack()

# Tkinter 이벤트 루프 시작
window.mainloop()
