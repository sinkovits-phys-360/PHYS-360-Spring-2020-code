from Vec2 import Vec2

a = Vec2(3,4)
print("a =", a)

b = Vec2(2, -1)
print("b =", b)

s = 5

print("a*s =", a*s)
print("s*a =", s*a)

print("a @ b =", a @ b)
print("a =", a)
print("b =", b)

z = Vec2(0,0)

if a:
    print("True")
else:
    print("False")

if b:
    print("True")
else:
    print("False")

if z:
    print("True")
else:
    print("False")

print(a.x, a.y)

print("-b =", -b)

print("a.mag() =", a.mag())
