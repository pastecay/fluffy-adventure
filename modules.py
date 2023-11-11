def all_divisors(number):
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return sorted(divisors)


def three_args(*, var1=None, var2=None, var3=None):
    args_str = "Переданы аргументы:"

    if var1 is not None:
        args_str += f" var1 = {var1},"
    if var2 is not None:
        args_str += f" var2 = {var2},"
    if var3 is not None:
        args_str += f" var3 = {var3},"

    if args_str != "Переданы аргументы:":
        print(args_str.rstrip(','))



def is_palindrome(input_str):
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]




def find_most(text):
    words = text.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    most_frequent_word = max(word_counts, key=word_counts.get)

    longest_word = max(words, key=len)

    return most_frequent_word, longest_word



def create_spiral_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, m - 1, 0, n - 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix






def is_magic_square(matrix):
    n = len(matrix)
    target_sum = n * (n**2 + 1) // 2

    for i in range(n):
        if sum(matrix[i]) != target_sum or sum(matrix[j][i] for j in range(n)) != target_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != target_sum or sum(matrix[i][n - i - 1] for i in range(n)) != target_sum:
        return False

    return True


