import math

L, W, H = map(int, input().split())
S = ((L + W)*2*H)
print(math.ceil(S/16))