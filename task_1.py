#подсчитайте количество гласных в строке, введенной с клавиатуры с использованием множеств.

txt = input('>>>')
print(len([letter for letter in txt if letter.lower() in 'aeiou']))

