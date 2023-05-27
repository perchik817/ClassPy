def sum_of_numbers():
    total_sum = 0

    for number in range(100, 1000):
        if number % 3 == 0 and number % 5 != 0 and '2' not in str(number):
            total_sum += number

    return total_sum

result = sum_of_numbers()
print("Сумма всех трехзначных чисел:", result)

def get_longest_word(word_list):
    longest_word = ""

    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
result = get_longest_word(word_list)
print("Самое длинное слово:", result)
