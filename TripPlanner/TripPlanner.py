#this is a simple trip planner
def Planner():
    speed = 30
    distance = 600
    time = (distance/speed) *60
    return time

print('you arrive at your destination in' , Planner(), 'hours')