# point.py
# Defines a class to represent two-dimensional discrete points.
import math


class Point:
    def __init__(self, x=0, y=0):
        self.xCoord = x
        self.yCoord = y

    def __str__(self):
        return "(" + str(self.xCoord) + ", " + str(self.yCoord) + ")"

    def getX(self):
        return self.XCoord

    def getY(self):
        return self.yCoord

    def shift(self, xInc, yInc):
        self.xCoord += xInc
        self.yCoord += yInc


class Point2D(Point):
    def __init__(self, point_a):
        self.p = point_a

    def __str__(self):
        return "(" + str(self.p.yCoord) + ", " + str(self.p.yCoord) + ")"

    def distcanciaOutroPonto(self, other_point):
        side_a = math.pow(other_point.xCoord - self.p.xCoord, 2)
        side_b = math.pow(other_point.yCoord - self.p.yCoord, 2)
        return math.sqrt(side_a + side_b)

    def distanciaOrigem(self):
        return self.distcanciaOutroPonto(Point(0, 0))


point_1 = Point(10, 20)
point2d_1 = Point2D(point_1)
point_2 = Point(5, 5)
point2d_2 = Point2D(point_2)
point_1.__str__()
point_2.__str__()

print(point2d_1.distcanciaOutroPonto(point_2))
print(point2d_2.distcanciaOutroPonto(point_1))

print(point2d_1.distanciaOrigem())
print(point2d_2.distanciaOrigem())


class Point3D(Point):
    def __init__(self, point, z):
        self.point = point
        self.zCoord = z

    def getPoint(self):
        return self.point

    def getZ(self):
        return self.zCoord

    def __str__(self):
        return "(" + str(self.point) + ", " + str(self.zCoord) + ")"

    def distcanciaOutroPonto3D(self, other_point_3d):
        side_a = math.pow(other_point_3d.getPoint().xCoord - self.getPoint().xCoord, 2)
        side_b = math.pow(other_point_3d.getPoint().yCoord - self.getPoint().yCoord, 2)
        side_c = math.pow(other_point_3d.getZ() - self.getZ(), 2)
        return math.sqrt(side_a + side_b + side_c)

    def distanciaOrigem(self):
        return self.distcanciaOutroPonto3D(Point3D(Point(0, 0), 0))


point_3 = Point(10, 20)
point3d_1 = Point3D(point_3, 20)
point_4 = Point(5, 5)
point3d_2 = Point3D(point_4, 4)
print(point3d_1.__str__())
print(point3d_2.__str__())

print("---------------------------------")
print(point3d_1.distcanciaOutroPonto3D(point3d_2))
print(point3d_2.distcanciaOutroPonto3D(point3d_1))
print("---------------------------------")

print(point3d_1.distanciaOrigem())
print(point3d_2.distanciaOrigem())


class Circulo:
    def __init__(self, point, raio):
        self.Point = point
        self.raio = raio

    def diametro(self):
        return self.raio * 2

    def perimetro(self):
        return math.pi * self.diametro()

    def area(self):
        return math.pi * math.pow(self.raio, 2)

    def __str__(self):
        return "(" + str(self.Point) + ", " + str(self.raio) + ")"


print("-----Circulo----------")
p = Point(1, 10)
cir = Circulo(p, 20)
print(cir.diametro())
print(cir.area())
print(cir.perimetro())
