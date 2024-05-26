k = int(input()) - 1

fn = [0, 1]

if k < 2:
	print(fn[k])
else:
	for i in range(2, k+1):
		fn.append(fn[i-1] + fn[i-2])
		
	print(fn[-1]%1000000007)