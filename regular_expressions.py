import re

hi_regex = re.compile("hi")
hi_regex.search("hi")
hi_regex.findall("hi high white")

import re

re.search("pattern here", "the string to be searched")
re.findall("pattern", "the string to be searched")

toe_pattern = re.compile("\\\\toe")
texts = ["\toe", "\\toe", "\\\toe", "\\\\toe"]
for text in texts:
    print(f"Match {text!r}: {toe_pattern.match(text)}")

toe_regex = re.compile(r"\\toe")
texts = ["\toe", "\\toe", "\\\toe", "\\\\toe"]
for text in texts:
    print(f"Match {text!r}: {toe_regex.match(text)}")

re.search(r"^hi", "hi Python")
re.search(r"hey$", "Python, hey")
re.search(r"^hi hey$", "hi hey")
re.search(r"^hi hey$", "hi hello hey")

test_string = "h hi hii hiii hiiii"
test_patterns = [r"hi?", r"hi*", r"hi+", r"hi{3}", r"hi{2,3}", r"hi{2,}"]
for pattern in test_patterns:
    print(f"{pattern: <8}", "-->  ", re.findall(pattern, test_string))
    
test_string1 = "$1e2_ d\t"
patterns = ["\d", "\D", "\s", "\S", "\w", "\W", ".", "[ed]"]
for pattern in patterns:
    print(f"{pattern: <8}", "-->  ", re.findall(pattern, test_string1))
    
    
re.findall(r"a|b", "a c d d b ab")
re.findall(r"a|b", "c d d b")
re.findall(r"(abc)", "ab bc abc ac")
re.findall(r"(abc)", "ab bc ac")
re.findall(r"[^a]", "abcde")



# ASCII flag
text = "a \u0117"
print(text)
a_regex = re.compile("\w", flags=re.A)
a_regex.findall(text)
re.findall("\w", text)

# Ignore case flag
i_regex = re.compile("hi", flags=re.I)
i_regex.findall("hi HIGH")
re.findall("hi", "hi HIGH")

# Multiline flag
m_regex = re.compile("^hi", flags=re.M)
m_regex.findall("hi\nhi\nhi")
re.findall("^hi", "hi\nhi\nhi")

# Dotall flag
s_regex = re.compile(".", flags=re.S)
s_regex.findall("123abc\n")
re.findall(".", "123abc\n")

# Verbose flag
x_regex = re.compile(". # it will match any character", flags=re.X)
x_regex.findall("123abc")
re.findall(". # it will match any character", "123abc")

re.findall("^hi", "hi\nHi\nhI", flags=re.I|re.M)



match = re.match(r"(.\d)*", "a1b2c3dd")
print(match)

print("span:", match.span())
print("matched:", match.group())
print(f"start: {match.start()} & end: {match.end()}")

float_match = re.match(r"([a-z]+)\.(\d+)", "ab.23")
float_match.groups()

float_match.group(0)
float_match.group(1)
float_match.group(2)

float_match.span(0)
float_match.span(1)
float_match.span(2)


text_to_parse = """Smith, John; 39
A random record
Davis, Ashley; 24
Robinson, Zoe; 37
Another random record"""

parsing_regex = re.compile(r"(?P<last_name>[a-zA-Z]+), (?P<first_name>[a-zA-Z]+); (?P<age>\d+)")for line in text_to_parse.split("\n"):
    if matched := parsing_regex.match(line):
        print(f"Found Record: last_name={matched.group('last_name')}, first_name={matched.group('first_name')}, "
              f"age={matched.group('age')}")
    else:
        print("Nothing matched")

matched.groupdict()

re.search(r"\d+", "abc123xyz")
re.search(r"\d+", "abcdef")
re.match(r"\d+", "abc123")
re.match(r"\d+", "123abc")

text_to_match = 'Hi hi hey hI, heY hello'
regex = re.compile(r"hi", flags=re.I)
regex.findall(text_to_match)
list(regex.finditer(text_to_match))

text_to_split = 'a1b2c3d4e555f99'
re.split(r"\d+", text_to_split, maxsplit=4)

text_to_sub = '123,456,789_012_345/678'
re.sub(r"\D", "-", text_to_sub)