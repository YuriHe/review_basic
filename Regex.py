import re

# def useSub():
#     """
#     replace all matches of pattern with repl
#     re.sub(pattern, replace, string)
#     """
#     # replace all number with $
#     s1 = re.sub(r'\d+', '$', '123 abc 123')
#     print(s1) # output:$ abc $
# useSub()

# def useMatch():
#     line = "Cats are smarter than dogs"
#     matchObj = re.match()

#     m1 = re.match(r'hello', 'xhello world')
#     print(bool(m1)) # output:True
#     print(m1) # output:<re.Match object; span=(0, 5), match='hello'>

#     m2 = re.match(r'hello', 'say hello world')
#     print(m1.group() if m2 else "No match") # output:No match
# useMatch()


def usefindAll():
    f1 = re.findall(r'\d+', 'There are 3 cats, 4 dogs, and 5 birds.')
    print(f1) # output: ['3','4','5']

    f2 = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=19')
    print(f2) # output: [('width', '20'), ('height', '19')]
usefindAll()

# def useCompile():
#     """
#     compiles a regex pattern into a regex object which can be reused
#     re.compile(pattern)
#     """
#     # valid if phone number only valid format is nnn-nnn-nnnn or (nnn) nnn-nnnn
#     pass




# def useSearch():
#     """
#     searches the entire string for the first match
#     re.search(pattern, string)
#     """
#     m1 = re.search(r'world', 'hello world, my world')
#     print(m1.group() if m1 else 'No found') # output:world
# useSearch()
