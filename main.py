from modules import all_divisors,three_args,is_palindrome,find_most,create_spiral_matrix,is_magic_square
number1 = 23436
number2 = 190187200
number3 = 380457890232

result1 = all_divisors(number1)
result2 = all_divisors(number2)
result3 = all_divisors(number3)

print(result1)
print(result2)
print(result3)

################################################################################################################
three_args(var1=2, var3=10)
################################################################################################################
example_str = "A man, a plan, a canal: Panama"
result = is_palindrome(example_str)
print(f'"{example_str}" является палиндромом: {result}')

################################################################################################################
input_text = "Это образец текста с образцами слов. Текст может содержать повторяющиеся слова для проверки.."
result = find_most(input_text)
print(f"Наиболее часто встречающееся слово: {result[0]}")
print(f"Самое длинное слово: {result[1]}")
#############################################################################################################

n_value = 3
m_value = 4
spiral_matrix = create_spiral_matrix(n_value, m_value)
for row in spiral_matrix:
    print(row)
#############################################################################################################
magic_square = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
result = is_magic_square(magic_square)
print(f"Это магический квадрат: {result}")