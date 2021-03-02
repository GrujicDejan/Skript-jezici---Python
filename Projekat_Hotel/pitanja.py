# grafikoni

import matplotlib.pyplot as plt

list1 = [1,2,3,4,5]
list2 = [1,4,9,16,25]

plt.scatter(list1, list2)
plt.plot(list1, list2)
plt.ylabel=('kvadrati brojeva')
plt.xlabel=('brojevi')
plt.xticks(rotation=90)
plt.ylim(ymin = 0, ymax = 26)
plt.xlim(xmin = 0, xmax = 7)
plt.show()




# stringovi

#s[0] = b NIJE MOGUCE!

s = ''
s+= 'Novi Sad'
print(s)
print(s[5])
print(s[0:3])
s1,s2 = s.split(" ")
print(s2)
print(s*3)
for i in s:
    print(i, end = " ")
print()
print(s.upper())
print((s*2).count('a'))
s3 = s.lower()
print(s3)
print(s3.capitalize())
print(s3.title())
print("Prvo {0}, drugo {1}, opet prvo {0}".format("1", "2"))
print("Prvo {0:>8.2f}, drugo {1:^10d}".format(123.456, 257))








