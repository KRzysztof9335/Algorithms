# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

temperatures = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    temperatures.append(int(i))
if not temperatures:
    print("0")
else:
    temp_abs = [abs(t) for t in temperatures]
    temp_min = min(temp_abs)
    if temp_min in temperatures:
        print(temp_min)
    else:
        print(-1*temp_min)