# Math operation 

a = {10, 20, 30 ,50, 40}
b = {20, 40, 60, 80, 90}


print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)
print( b - a )

print(a.symmetric_difference(b))
print(a ^ b )


# Relationship

p = {30 ,40 }
q = {20, 30, 40, 60 }

print(p.issubset(q))
print(q.issuperset(p))

print(p.isdisjoint(q)) # is both sharing no item then T