from collections import defaultdict
import re

def within(x, ran):
  r1, r2 = ran
  return x >= r1 and x < r2

def within_cube(cube1, cube2):
  # ((x1, y1, z1), (x2, y2, z2)) = cube1
  # ((x11, y11, z11), (x12, y12, z12)) = cube2
  result = True
  for dim in xrange(3):
    for coord in xrange(2):
      result = result and within(cube1[coord][dim], (cube2[0][dim], cube2[1][dim] + 1))
  return result

def intersect(cube1, cube2):
  ((x1, y1, z1), (x2, y2, z2)) = cube1
  ((x11, y11, z11), (x12, y12, z12)) = cube2
  if x11 >= x2 or x12 < x1 or y11 >= y2 or y12 < y1 or z11 >= z2 or z12 < z1:
    return False
  return True

def valid_cube(cube):
  ((x1, y1, z1), (x2, y2, z2)) = cube
  return x2 > x1 and y2 > y1 and z2 > z1

# breaks up cube1
def break_up(cube1, cube2):
  ((x1, y1, z1), (x2, y2, z2)) = cube1
  ((x11, y11, z11), (x12, y12, z12)) = cube2
  xyzs = [[x1, x2, x11, x12], [y1,y2, y11, y12], [z1,z2, z11, z12]]
  xs, ys, zs = xyzs
  xs.sort()
  ys.sort()
  zs.sort()
  result = []
  for i in xrange(len(xs)-1):
    x_range = (xs[i], xs[i+1])
    if x_range[1] <= x_range[0]:
      continue
    xin = True
    for dim in xrange(2):
      xin = xin and within(x_range[dim], (cube1[0][0], cube1[1][0]+1))
    if not xin:
      continue
    for j in xrange(len(ys)-1):
      y_range = (ys[j], ys[j+1])
      if y_range[1] <= y_range[0]:
        continue
      yin = True
      for dim in xrange(2):
        yin = yin and within(y_range[dim], (cube1[0][1], cube1[1][1]+1))
      if not yin:
        continue
      for k in xrange(len(zs)-1):
        z_range = (zs[k], zs[k+1])
        if z_range[1] <= z_range[0]:
          continue
        zin = True
        for dim in xrange(2):
          zin = zin and within(z_range[dim], (cube1[0][2], cube1[1][2]+1))
        if not zin:
          continue
        new_cube = []
        for w in xrange(2):
          t = []
          t.append(x_range[w])
          t.append(y_range[w])
          t.append(z_range[w])
          new_cube.append(tuple(t))
        new_cube = tuple(new_cube)
        result.append(new_cube)
  return result

def process(cubes, is_on, bounds):
  new_cubes = []
  for existing in cubes:
    if not intersect(existing, bounds):
      new_cubes.append(existing)
      continue
    small_cubes = break_up(existing, bounds)
    for sc in small_cubes:
      if not within_cube(sc, bounds):
        new_cubes.append(sc)
  if is_on:
    new_cubes.append(bounds)
  return new_cubes

def count_cubes(cubes):
  count = 0
  for cube in cubes:
    ((x1, y1, z1), (x2, y2, z2)) = cube
    count += (x2 - x1) * (y2 - y1) * (z2 - z1)
  return count

def debug_process(debug_cubes, is_on, cube):
  ((x1, y1, z1), (x2, y2, z2)) = cube
  for x in xrange(x1, x2):
    for y in xrange(y1, y2):
      for z in xrange(z1, z2):
        debug_cubes[(x,y,z)] = is_on

def debug_count(debug_cubes):
  r = 0
  for c, v in debug_cubes.iteritems():
    r += v
  return r

f = open('input.txt', 'r')
cubes = []
# debug_cubes = {}
lines = f.read().strip().split('\n')
for ln, line in enumerate(lines):
  r = re.search(r'(on|off) x=([-+]?[0-9]+)..([-+]?[0-9]+),y=([-+]?[0-9]+)..([-+]?[0-9]+),z=([-+]?[0-9]+)..([-+]?[0-9]+)', line)
  values = map(lambda x: 1 if x == 'on' else 0 if x == 'off' else int(x), r.groups())
  is_on, x1, x2, y1, y2, z1, z2 = values
  cubes = process(cubes, is_on, ((x1, y1, z1), (x2+1, y2+1, z2+1)))
  # debug_process(debug_cubes, is_on, ((x1, y1, z1), (x2+1, y2+1, z2+1)))
  print ln
print count_cubes(cubes)
