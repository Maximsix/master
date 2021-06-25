
# example 1
# index
bingno_blacklist = ['Tyler Beverly', 'William Ford', 'Alex Wallace']
poker_blacklist = ['Anthony Labert', 'Brandon Newman', 'Alex Wallace']
majong_blacklist = ['Alex Wallace', 'George Allen', 'Oscar Scott']

print('Alex Wallace found at index position = ', bingno_blacklist.index('Alex Wallace'))
print('Alex Wallace found at index position = ', poker_blacklist.index('Alex Wallace'))
print('Alex Wallace found at index position = ', majong_blacklist.index('Alex Wallace'))


# example 2
# count
bingno_blacklist = ['Tyler Beverly', 'William Ford', 'Alex Wallace']
poker_blacklist = ['Anthony Labert', 'Brandon Newman', 'Alex Wallace']
majong_blacklist = ['Alex Wallace', 'George Allen', 'Oscar Scott']

r1 = bingno_blacklist.count('Alex Wallace')
r2 = poker_blacklist.count('Alex Wallace')
r3 = majong_blacklist.count('Alex Wallace')
if r1 + r2 + r3 == 3:
    print('Alex Wallace found in all black list')
else:
    print('Didn\'t in all black list')


# example 3
# count
bingno_blacklist = ['Tyler Beverly', 'William Ford', 'Alex Wallace']
poker_blacklist = ['Anthony Labert', 'Brandon Newman', 'Alex Wallace']
majong_blacklist = ['Alex Wallace', 'George Allen', 'Oscar Scott']

all_poker_blacklists = [bingno_blacklist, poker_blacklist, majong_blacklist]
b = []
name = []
for x in all_poker_blacklists:
    for n in x:
        if b.count(n):
            name.append(n)
        else:
            b.append(n)
else:
    print(name[0], 'found in all black list')

# example 4
# count
bingno_blacklist = ['Tyler Beverly', 'William Ford', 'Alex Wallace']
poker_blacklist = ['Anthony Labert', 'Brandon Newman','Alex Wallace']
majong_blacklist = ['Alex Wallace','George Allen', 'Oscar Scott']
result = bingno_blacklist + poker_blacklist + majong_blacklist

print("Alex Wallace found =", bool(result.count('Alex Wallace')))
