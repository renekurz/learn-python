word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))

# Problem Solving - print out pages and word_per_page
# You can see, if you e.g. input 250 at word_per_page it's false, because there is '==' instead of '='
print(f"pages: {pages}")
print(f"word_per_page: {word_per_page}")

total_words = pages * word_per_page
print(total_words)