import math

def UA(arr, ave):
    sum = 0
    for i in arr:
        sum += (i - ave)**2
    return math.sqrt(sum / len(arr) / (len(arr) - 1))


# vpp = 5.010;
# upp = 5.60;
# print(math.fabs(vpp - upp) / vpp * 100)
# T = 1.02
# hz = 1.01
# print(math.fabs(T - 1 / hz) * hz *100)
# print(1 / hz)

fhz = [99.966381, 99.968115, 99.969462, 99.968531]
sum_hz = sum(fhz)
print(sum_hz / 4)
ua = UA(fhz, sum_hz / 4)
print("Ua: ", ua)
print("ur: ", ua * 4 / sum_hz)

fhz = [99.967460, 99.968440, 99.968280]
sum_ave = sum(fhz) / 3
print(sum_ave)
ua = UA(fhz, sum_ave)
print("Ua: ", ua)
print("Ur: ", ua / sum_ave)