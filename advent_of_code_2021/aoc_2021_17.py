
targetX = (206, 250)
targetY = (-105, -57)

def canHit(x, y):
    px, py = 0, 0
    result = -10
    while True: 
        px += x
        py += y
        result = max(result, py)
        if px >= targetX[0] and px <= targetX[1] and py >= targetY[0] and py <= targetY[1]:
            return (True, result)
        if py < targetY[0] or (x == 0 and px < targetX[0]) or (x == 0 and px > targetX[1]):
            return (False, result)
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        y -= 1

maxi = -10
count = 0
for x in xrange(0, 400):
    for y in xrange(-400, 400):
        v, ch = canHit(x, y)
        if v:
            maxi = max(maxi, ch)
            count += 1
print '-------------'
print maxi, count

