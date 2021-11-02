import math

IR = 3
n = 15
delta_P = 1/(IR*math.log(IR, 2))
delta_N = 1/(IR*math.log(IR, 2)) - 1
r_p = []
r_n = []
for i in range(1, n):
    r_i_p = 1/IR - (2**(i-n)*delta_P)
    r_p.append(r_i_p)
    r_i_n = 1/IR + (2**(i-n)*delta_N)
    r_n.append(r_i_n)

print("r_P:", r_p)
print("r_N:", r_n)

