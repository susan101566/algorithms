
def get(registers, v):
  try:
    int(v)
  except ValueError:
    return registers[v]
  else:
    return int(v)

def run(registers, i, v1, v2):
  print 'running instruction', i, v1, v2
  if i == 'inp':
    registers[v1] = int(v2)
  elif i == 'mul':
    registers[v1] = get(registers, v1) * get(registers, v2)
  elif i == 'add':
    registers[v1] = get(registers, v1) + get(registers, v2)
  elif i == 'div':
    registers[v1] = get(registers, v1) / get(registers, v2)
  elif i == 'mod':
    registers[v1] = get(registers, v1) % get(registers, v2)
  elif i == 'eql':
    registers[v1] = 1 if get(registers, v1) == get(registers, v2) else 0
  else:
    print 'running error', i
  print registers

f = open('input.txt', 'r')
sections = f.read().strip().split('\n\n')
values = {}
for r in list('wxyz'):
  values[r] = 0
numbers = [9, 0]
for n in xrange(10):
  numbers[1] = n
  for r in list('wxyz'):
    values[r] = 0
  for i, section in enumerate(sections):
    lines = section.split('\n')
    for line in lines:
      ins = line.split(' ')
      if ins[0] == 'inp':
        run(values, ins[0], ins[1], numbers[i])
      else:
        run(values, ins[0], ins[1], ins[2])
    if i == 1:
      break
  print '----------------'
  print values
  print '----------------'
