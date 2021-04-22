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
