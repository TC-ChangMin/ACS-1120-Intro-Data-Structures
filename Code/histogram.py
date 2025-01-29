import os

def get_path(file_name):
    script_dir = os.path.dirname(__file__)
    file_dir = os.path.join(script_dir, "data", file_name)
    return file_dir


def histogram(source_text):
    histogram = {} 
    with open(source_text, "r") as f:
        for line in f:
            for word in line.split():
                word = word.lower()
                histogram[word] = histogram.get(word, 0) + 1 
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return f"'{word}' appears {histogram[word]} times" if word in histogram else "Word not found"

# def sorted_histogram(histogram):
#     def get_value(item):
#         return item[1]
    
#     return sorted(histogram.items(), key=get_value, reverse=True)



print(unique_words(histogram(get_path("sample.txt"))))
print("="*50)
print(histogram(get_path("sample.txt")))
print("="*50)
print(frequency("the", histogram(get_path("sample.txt"))))
print(frequency("aaaa", histogram(get_path("sample.txt"))))
# print(sorted_histogram(histogram(get_path("sample.txt"))))
# print("="*50)