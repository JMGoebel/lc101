l = [4,2,100,3,1,0]
n = []
print(l)

def thesort(l):
  for n in range(len(l) -1):
    if l[n] > l[n+1]:
      temp = l[n]
      l[n] = l[n+1]
      l[n+1] = temp
      thesort(l)
thesort(l)
print(l)

