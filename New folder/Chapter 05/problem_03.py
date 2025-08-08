# Check the length of set

s = set()

s.add(20)
s.add(20.0)
# Both 20 & 20.0 are same for python
s.add('20')

print(len(s))

print(s)