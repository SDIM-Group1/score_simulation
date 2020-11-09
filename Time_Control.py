import Physical_model as pm
budget = 1000
budget_left = 5000-budget

Time_go = pm.Time(0)
Time_locate = pm.Time(0)
Time_grab = pm.Time(0)
Time_retrieve = pm.Time(0)
Time_back = pm.Time(0)
Time_unload = pm.Time(0)

class route:
    def __init__(self):
        self.objects = []
        self.num = self.objects.__len__()





