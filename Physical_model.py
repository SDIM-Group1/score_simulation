# 定义小车参数
from enum import Enum


class Car:
    def __init__(self, weight_kg, power, speed, volume):
        self.weight = weight_kg
        self.power = power
        self.speed = speed
        self.volume = volume


# 定义重物参数
class Item:
    # position: []
    # weight: float
    # difficultyCoeff: int
    # correctionCoeff: int
    # shape = 1  # FIXME!
    # score = 1  # FIXME!

    # xy坐标(position[0]是x横坐标，position[1]是y纵坐标)、质量、形状、分值
    # 物体板的低分左侧为原点
    def __init__(self, position):
        self.position = position  # (x,y)

    def weight(self):
        return judgeWeight(self.position[0], self.position[1])

    def shape(self):
        return judgeShape(self.position[0], self.position[1])

    def correctionCoeff(self):
        return judgeCorrectionCoefficient(self.position[1])

    def weight(self):
        return judgeWeight(self.position[0], self.position[1])

    def distance(self):
        return judgeDistance(self.position[1])

    def score(self):
        return self.shape() * self.correctionCoeff() * self.weight() * self.distance()


# 定义物件板，5*5的空间，
class ChessBoard:
    def __init__(self, x, y, object_components):
        self.x = x
        self.y = y
        self.objectComponents = object_components


# 总时间
class Time:
    def __init__(self, second):
        self.second = second


"""
class Placement:
    def __init__(self, height):
        self.Coefficient = judgePlacementCoefficient(height)
"""


# 定义抓取路线参数，"抓取路线"
class Route:
    totalScore = 0

    def __init__(self, serial_number, num, totalscore):
        self.serialNumber = serial_number
        self.time = num
        self.totalScore = totalscore


# 修正系数
def judgeCorrectionCoefficient(x):
    if x == 0:
        return 100
    elif x == 1:
        return 80
    elif x == 2:
        return 60
    elif x == 3:
        return 50
    elif x == 4:
        return 40


# 判断重物的重量
def judgeWeight(x, y):
    if x == 0 or x == 4:
        weight = 200 + 300 * y
    elif x == 1 or x == 3:
        weight = 200 + 500 * y
    else:
        weight = 200 + 700 * y

    if y ==0:
        weight = 500
    return weight / 1000


# 判断重物的形状
def judgeShape(x, y):
    if x == 0 or x == 4:
        return 1
    elif x == 1 or x == 2:
        if y != 4:
            return 1.2
        else:
            return 1.5
    else:
        if y <= 1:
            return 1.3  # CYLINDER
        elif y <= 3:
            return 1.4  # CONE
        else:
            return 1.5  # TETRAHEDRON


def judgeDistance(y):
    return y * 0.2 + 0.5


def judgePlacementCoefficient(height):
    if height == 0:
        return 1
    elif height == 1:
        return 1.25
    elif height == 2:
        return 1.5
    else:
        return 0.4


"""
class shape(Enum):
    SPHERE = 1
    CUBE = 2
    CYLINDER = 3
    CONE = 4
    TETRAHEDRON = 5
"""

# class Shape:
#     SPHERE = 1
#     CUBE = 1.2
#     CYLINDER = 1.3
#     CONE = 1.4
#     TETRAHEDRON = 1.5


# Shape = Enum("Shape", ("circle", "cube", "cylinder", "tetrahedron"))
"""
#继承"抓取路线"，路线1
class Route1(Route):
    pass
#继承"抓取路线"，路线2
class Route2(Route):
    pass
#继承"抓取路线"，路线3
class Route3(Route):
    pass
#继承"抓取路线"，路线4
class Route4(Route):
    pass
#继承"抓取路线"，路线2
class Route2(Route):
    pass
"""
