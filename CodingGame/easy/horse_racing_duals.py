n = int(input())

horses_strength = []
for i in range(n):
    horses_strength.append(int(input()))
horses_strength = sorted(horses_strength)

closest = float("inf")
for i in range(len(horses_strength)-1):
    diff_between_horses = abs(horses_strength[i] - horses_strength[i+1])
    if diff_between_horses < closest:
        closest = diff_between_horses

print(closest)
