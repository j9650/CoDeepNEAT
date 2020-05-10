import sys

filename = sys.argv[1]
f = open(filename, 'r')

exe_time = []

for line in f:
  if 'main training time:' in line:
    exe_time.append(float(line.strip().split()[-1]))

assert len(exe_time) == 4
assert len(exe_time) == 4

print(str(exe_time[0])+' '+str(exe_time[1])+' '+str(exe_time[2])+' '+str(exe_time[3]))

