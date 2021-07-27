# class Point:
#     "Класс для представления координат точек на плоскости"
#     x = 1
#     y = 1
#
# pt = Point()
# print(pt.__dict__)
# pt.x = 5
# pt.y = 10
# print(pt.__dict__)
# print(getattr(pt, "x"))
# print(getattr(pt, "z", False))
# setattr(pt, "z", 7)
# print(pt.__dict__)
# delattr(pt, "z")
# print(pt.__dict__)
#

print("Задание для самостоятельной работы")
print("----------------------------------")

class Point3D:
    x = 1
    y = 2
    z = 3

p = Point3D()
t = Point3D()

print(getattr(p, "x", False))
print(getattr(p, "y", False))
print(getattr(p, "z", False))

delattr(Point3D, "z")

print(getattr(p, "x", False))
print(getattr(p, "y", False))
print(getattr(p, "z", False))

setattr(p, "x", 5)

print(getattr(p, "x", False))
print(getattr(p, "y", False))
print(getattr(p, "z", False))

print(p.__dict__)

print(getattr(t, "x", False))
print(getattr(t, "y", False))
print(getattr(t, "z", False))

setattr(Point3D, "x", 10)
print(getattr(p, "x", False))
print(getattr(t, "x", False))

print(p.__dict__)
print(t.__dict__)

