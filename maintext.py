# Main program
import mytext

# The input text
text = "An apple a day keeps the doctor away"

# Call the functions from MyText module
word_count = mytext.count_words(text)
words_by_length = mytext.sort_by_length(text)
words_alphabetically = mytext.sort_alphabetically(text)

# Print the results
print("Text:", text)
print("Number of words:", word_count)
print("Words from the longest:", ", ".join(words_by_length))
print("Words ordered alphabetically:", ", ".join(words_alphabetically))
