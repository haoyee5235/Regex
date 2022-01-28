import re

test_string = '123abc456789abc123ABC'

#0 RE module
#in re.compile(r"abc") the r specify raw string
# pattern = re.compile(r"abc")
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match)



#1 Methods to search for matches
#finall() //findall() methods will print all the strings that matches the pattern
# pattern1 = re.compile(r"abc")
# matches1 = pattern1.findall(test_string)
#
# for match1 in matches1:
#     print(match1)
#
# #match() //match() method will only print the string that appear in the beginning
# pattern2 = re.compile(r"abc")
# matches2 = pattern2.match(test_string)
#
# print(matches2)
#
# pattern3 = re.compile(r"123")
# matches3 = pattern3.match(test_string)
#
# print(matches3)
#
# #search() //search() method will only return the first match
# pattern4 = re.compile(r"abc")
# matches4 = pattern4.search(test_string)
#
# print(matches4)




#2 Methods on a match object
# pattern = re.compile(r"abc")
# matches = pattern.finditer(test_string)

# #span() // this method return the position of the match and adding .start() and .end() provides the position of start and end
# for match in matches:
#     print(match.span(),match.start(),match.end())

#group() // this methods return the actual string of the match and adding argument will access to which matches

# for match in matches:
#     print(match.group())



#3 Meta Character
# . Any character(except newline character)
# pattern = re.compile(r".")
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match.group())


# ^ Starts with "^hello"
# pattern = re.compile(r"^123")
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match.group())


# $ Ends with "world$"
# pattern = re.compile(r"ABC$")
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match.group())



#4 Special Sequence
test_string2 = 'hello 123_ heyho hohey'

#\d matches any decimal digit [0-9]
# pattern = re.compile(r'\d')
# matches = pattern.finditer(test_string2)
# for match in matches:
#     print(match.group())

#\D matches any non-digit character
# pattern = re.compile(r'\D')
# matches = pattern.finditer(test_string2)
# for match in matches:
#     print(match.group())

# \s find any whitespace character
# pattern = re.compile(r"\s")
# matches = pattern.finditer(test_string2)
# for match in matches:
#     print(match)

# \S find any non whitespace Character
# pattern = re.compile(r"\S")
# matches = pattern.finditer(test_string2)
# for match in matches:
#     print(match)


# \w matches any alphanumeric character [a-zA-Z0-9_]
# pattern = re.compile(r"\w")
# matches = pattern.finditer(test_string2)
# for match in matches:
#     print(match)


# \W matches any non alphanumeric character
# pattern = re.compile(r"\W")
# matches = pattern.finditer(test_string2)
# for match in matches:
#     print(match)


# \b(string) matches any (string) that starts in the block
# pattern = re.compile(r"\bhey")
# matches = pattern.finditer(test_string2)
# for match in matches:
#     print(match)

#\B(string) matches any (string) that end in the block
# pattern = re.compile(r"\Bho")
# matches = pattern.finditer(test_string2)
# for match in matches:
#     print(match)



#5 Sets
test_string3 = 'hello 123_'

# [] anything inside the bracket will return all the occurence of the string specify
# - will define a range
# pattern = re.compile(r"[lo]")
# matches = pattern.finditer(test_string3)
# for match in matches:
#     print(match)

#for a-z
# pattern2 = re.compile(r"[a-z]")
# matches2 = pattern2.finditer(test_string3)
# for match in matches2:
#     print(match)

#for 0-9
# pattern3 = re.compile(r"[0-9]")
# matches3 = pattern3.finditer(test_string3)
# for match in matches3:
#     print(match)

#for 0-9 and _
# pattern4 = re.compile(r"[0-9_]")
# matches4 = pattern4.finditer(test_string3)
# for match in matches4:
#     print(match)

#for 0-9 and a-z
# pattern5 = re.compile(r"[0-9a-z]")
# matches5 = pattern5.finditer(test_string3)
# for match in matches5:
#     print(match)
