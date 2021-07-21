n, k = map(int, input().split())
length = 101*[0]

for i in range(n):
    st = input()
    length[len(st)] += 1

password = input()
early_count = late_count = 0

for i in range(len(length)):
    if i < len(password):
        early_count += length[i]
    if i <= len(password):
        late_count += length[i]
        
late_count -= 1

early = (early_count//k) * 5 + early_count + 1
late = (late_count//k) * 5 + late_count + 1

print(early, late)