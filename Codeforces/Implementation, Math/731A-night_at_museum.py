wheel = input()
idx = 'a'
res = 0

st = map(ord, st)
for c in wheel:
	dist = abs(ord(idx) - ord(c))
    
    # If go clockwise shorter
	if dist < 13:
		res += dist
	# If go counter-clockwise faster
	else:
		res += 26 - dist

	idx = c

print(res)
