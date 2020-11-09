import Physical_model as pm
import Time_Control as tc


# 计算比较成绩
def FinalScoreCalculation(score):
    return score / (
            tc.Time_back.second +
            tc.Time_go.second +
            tc.Time_grab.second +
            tc.Time_locate.second +
            tc.Time_retrieve.second +
            tc.Time_unload.second)


# 计算SDIM标准成绩：总分/(小车质量*预算金额)
def StandardScore(score):
    return score / (
            pm.Car.weight * tc.budget)


# 计算Token总分值
def ScoreCalculation(list_of_grab):
    score0 = 0
    for i in list_of_grab:
        #test only: print(pm.Item.correctionCoeff(i),pm.Item.weight(i),pm.Item.distance(i),pm.Item.shape(i))
        score0 = pm.Item.score(i) + score0
    return score0


def manualScore():
    return 0
