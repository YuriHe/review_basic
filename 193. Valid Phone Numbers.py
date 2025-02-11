import re
"""
1.Solution: python use regular expression
"""
def main(s):
    pattern = r'^((\(\d{3}\) \d{3}-\d{4})|(\d{3}-\d{3}-\d{4}))$'
    return bool(re.match(pattern, s))

phoneNum = [
    "987-123-4567",
    "123 456 7890",
    "(123) 456-7890"
]

for n in phoneNum:
    print(main(n))

"""
2.Solution: bash shell script
"""
grep -P '^((\(\d{3}\) \d{3}-\d{4})|(\d{3}-\d{3}-\d{4}))$' file.txt