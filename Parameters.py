import Physical_model as pm
import calculate as ccl

time = 0
score = 0
"""objectList = []
objectRow = []
for i in range(5):
    for j in range(5):
        objectRow.append([pm.Item([i, j])])
    objectList.append(objectRow)
    objectRow = []
"""

list_of_grab = [pm.Item([0, 0]), pm.Item([1, 1])]

car = pm.Car(15, 150, 1, 1)

score = ccl.ScoreCalculation(list_of_grab)
print(list_of_grab[0])
print("score = ", score)

"""
object00 = S.Object([0,0],)
object01 = S.Object([0,1],)
object02 = S.Object([0,2],)
object03 = S.Object([0,3],)
object04 = S.Object([0,4],)
object10 = S.Object([1,0],)
object11 = S.Object([1,1],)
object12 = S.Object([1,2],)
object13 = S.Object([1,3],)
object14 = S.Object([1,4],)
object20 = S.Object([2,0],)
object21 = S.Object([2,1],)
object22 = S.Object([2,2],)
object23 = S.Object([2,3],)
object24 = S.Object([2,4],)
object30 = S.Object([3,0],)
object31 = S.Object([3,1],)
object32 = S.Object([3,2],)
object33 = S.Object([3,3],)
object34 = S.Object([3,4],)
object40 = S.Object([4,0],)
object41 = S.Object([4,1],)
object42 = S.Object([4,2],)
object43 = S.Object([4,3],)
object44 = S.Object([4,4],)
"""
