# Определите общие символы в двух строках, введенных с клавиатуры.
txt_1 = input('>>>')
txt_2 = input('>>>')
result = 0
for i in txt_2:
    if i in txt_1:
        result += 1
