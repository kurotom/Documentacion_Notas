########################################################
########################################################
from collections import Counter

N = 10
X = list(map(int, '2 3 4 5 6 8 7 6 5 18'.split()))
C = 6
clientes = [[6, 55], [6, 45], [6, 55], [4, 40], [18, 60], [10, 50]]
DISP = Counter(X)
Money = 0

print(DISP)
for i in range(C):
    cliente = clientes[i]
    if DISP[cliente[0]] > 0:
        Money += cliente[1]
        DISP[cliente[0]] = DISP[cliente[0]] - 1
print(Money)

########################################################
########################################################

from itertools import permutations, 

A = list('HACK 2'.split())

strint = ''
x = list(permutations(A[0], int(A[1])))
x.sort()
for i in x:
    print("".join(i))
    
########################################################
# namedtuple:  namedtuples are easy to create, lightweight object types. #

from collections import namedtuple

N = int('5')
students = """
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5
"""

enter = students.strip(' ').split('\n')
data = [i for i in enter if i != '']
StudentObject = namedtuple('Student', data[0].split())
item = [i.split() for i in data[1:]]
print(f'{(sum([int(x.MARKS) for x in [StudentObject(i[0], i[1], i[2], i[3]) for i in item]]) / N):.2f}')


########################################################
# OrderedDict is a dictionary that remembers the order of the keys that were inserted first

from collections import OrderedDict

N = int(input())
data = []
dictProducts = OrderedDict()
for i in range(N):
    x = input().split()
    price = int(x[-1])
    product = " ".join(x[:-1])
    dictProducts[product] = dictProducts.get(product, 0) + price

for i in dictProducts.items():
    print(i[0], i[1])


########################################################
#  combinations :returns 'r' the length subsequences of elements from the input 
#                iterable.

from itertools import combinations

S, k = input().split()

a = [["".join(sorted(item)) for item in list(combinations(S, index))] for index in range(1, int(k) + 1)]
for i in a:
    i.sort()
    for x in i:
        print(x)

########################################################
#  itertools.combinations_with_replacement(iterable, r)
#  .combinations_with_replacement(iterable, r)  -  retorna combinaciones de elementos que tengan sucesión repetida.

from itertools import combinations_with_replacement

S, k = list(input().split())
k = int(k)
for i in sorted([sorted(i) for i in sorted(list(combinations_with_replacement(S, k)))]):
    print("".join(i))
    

########################################################
#  collections.deque()  :  (Doubly Ended Queue) in Python is implemented using
#                          the module “collections“. Deque is preferred over a
#                          list in the cases where we need quicker append and pop
#                          operations from both the ends of the container.
#

from collections import deque

N = int(input())
q = deque()

for i in range(N):
    r = input().split()
    if r[0] == 'append':
        q.append(r[1])
    elif r[0] == 'appendleft':
        q.appendleft(r[1])
    elif r[0] == 'pop':
        q.pop()
    elif r[0] == 'popleft':
        q.popleft()
print(" ".join(list(q)))



########################################################
#
#


