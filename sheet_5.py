
# Exercise 1: Generate lists using range
a = list(range(6))
b = list(range(4, 11, 2))
c = list(range(10, 5 - 1, -1))
d = list(range(10, -11, -5))

print(a)
print(b)
print(c)
print(d)

# Exercise 2: zip function with coordinates
x_coor = [1, 2, 3, 4, 5]
y_coor = [2, 4, 6, 8, 10]
z_coor = [0, -1, -2, -3, -4]

points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]
print(points)

# Exercise 3: apply function using map
def apply(lst, fn):
    result = []
    for elem in lst:
        result.append(fn(elem))
    return result

def add_1(num):
    return num + 1

r = apply([1, 2, 3], add_1)
print(r)

r = list(map(add_1, [1, 2, 3]))
print(r)

# Exercise 4: using lambda function
r = list(map(lambda num: num + 1, [1, 2, 3]))
print(r)

# Exercise 5: variable and list modification
def modlist(lst):
    for i in range(len(lst)):
        lst[i] = 10 * lst[i]

def modvar(num):
    num += 10

lst = [1, 2, 3]
modlist(lst)
print(lst)

x = 0
modvar(x)
print(x)

# Exercise 6: even check using list comprehension
x = [1, 2, 10, 13, 1]
output = [n % 2 == 0 for n in x]
print(output)

# Exercise 7: Point3D class
class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def add(self, p):
        self.x += p.x
        self.y += p.y
        self.z += p.z

    def subtract(self, p):
        self.x -= p.x
        self.y -= p.y
        self.z -= p.z

    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        dz = self.z - p.z
        return (dx**2 + dy**2 + dz**2) ** 0.5

p1 = Point3D(1, 2, 3)
p2 = Point3D(4, -2, 0)

p2.add(p1)
print(p2)

print(p1.distance(p2))
