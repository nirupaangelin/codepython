n =int(input())

fact= 0
for counter in range(1,n+1):
    fact = fact + counter

print("fact of num %d: %d" % (n,fact))