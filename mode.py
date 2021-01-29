from scipy import stats

speed = [45,55,60,70,75,70,100,80,87,88,86,88,65,60,60,60,70,70,20]

x = stats.mode(speed)

print (x)