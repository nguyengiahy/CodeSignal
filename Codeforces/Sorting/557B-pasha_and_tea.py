n, w = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

max_boy = a[n]		# max water can pour for a boy
max_girl = a[0]		# max water can pour for a girl

max_water = min(max_boy/2, max_girl)
if w <= 3 * max_water * n:
    print(w)
else:
    print(3 * max_water * n)