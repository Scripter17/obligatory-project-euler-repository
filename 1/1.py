# https://projecteuler.net/problem=1

import math
target=1000
nums=set()
for x in range(1, math.ceil(target/3)):
	nums.add(x*3)
for x in range(1, math.ceil(target/5)):
	nums.add(x*5)
print(sum(nums))
