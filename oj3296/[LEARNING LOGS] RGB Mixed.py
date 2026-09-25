"""doc"""
r1,g1,b1 = map(int, input().split())
r2,g2,b2 = map(int, input().split())

R = (r1 + r2) // 2
G = (g1 + g2) // 2
B = (b1 + b2) // 2

print(R,G,B)
