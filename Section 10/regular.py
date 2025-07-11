import re
text = "The quick brown fox jumps over the lazy dog fox."
# https://regexr.com/

# Search for a pattern
match = re.search("brown", text) # search for brown..
# print(match)
# if match:
#     print("Match found!") 
#     print("Start index:", match.start()) # starting index ..
#     print("End index:", match.end())

# Find all occurrences of a pattern
# matches = re.findall("the", text, re.IGNORECASE) # Case-insensitive search
# print("Matches:", matches)

new_text = re.sub("fox", "cat", text) # replace fox with cat ..
print("New text:", new_text)