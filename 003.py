import re
string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

pattern = r"[a-zA-z]+"
repattern = re.compile(pattern)
print([len(repattern.match(word).group()) for word in string.split()])
