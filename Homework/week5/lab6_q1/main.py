import text_utils as text

input = " Python is Amazing "
print(f"Raw Text:'{input}'")
print(f"1.Cleaned:'{text.clean_text(input)}'")
print("2.Word Count:", text.count_words(input))
print("3.Vowel Count:", text.count_vowels(input))
print("4.Highlighted:", text.highlight(input))

# result:
# Raw Text:' Python is Amazing '
# 1.Cleaned:'python is amazing'
# 2.Word Count: 5
# 3.Vowel Count: 8
# 4.Highlighted: ***  Python is Amazing  ***