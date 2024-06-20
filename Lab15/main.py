import re

def clean_data(data):
    data_points = data.split(',')
    stripped_points = map(str.strip, data_points)
    cleaned_points = map(str.lower, stripped_points)
    return list(cleaned_points)

def filter_emails(emails):
    words = emails.split()
    valid_emails = list(filter(lambda email: email.count('@') == 1, words))
    return valid_emails

def extract_keywords(data, length):
    words = data.split()
    long_words = filter(lambda word: len(word) > length, words)
    return list(long_words)


def process_text(data):
    entries = data.split(',')
    processed_entries = map(lambda entry: re.sub(r'[^a-zA-Z0-9\s]', '', entry).strip().lower(), entries)
    filtered_entries = filter(lambda entry: len(entry) > 0, processed_entries)
    return list(filtered_entries)

def normalize_data(data):
    num_strings = data.split(',')
    numbers = list(map(float, map(str.strip, num_strings)))
    max_value = max(numbers)
    normalized_numbers = [num / max_value for num in numbers]
    return normalized_numbers

def concatenate_strings(data, separator):
    parts = data.split(separator)
    concatenated_string = ''.join(parts)
    return concatenated_string

def sum_numeric_strings(data):
    elements = data.split(',')
    total_sum = 0
    for element in elements:
        stripped_element = element.strip()
        try:
            number = float(stripped_element)
            total_sum += number
        except ValueError:
            pass
    return total_sum

def filter_numbers(data, threshold):
    numbers = re.findall(r'\d+', data)
    numbers = list(map(int, numbers))
    filtered_numbers = list(filter(lambda x: x > threshold, numbers))
    return filtered_numbers

def map_to_squares(numbers):
    number_list = numbers.split(',')
    squared_numbers = [int(num.strip())**2 for num in number_list]
    return squared_numbers

def reverse_strings(words):
    word_list = words.split(',')
    reversed_words = [word[::-1] for word in word_list]
    return reversed_words














