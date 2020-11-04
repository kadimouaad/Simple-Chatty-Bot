A = int(input())
B = int(input())
H = int(input())
if A <= H and B >= H:
    print("Normal")
else:
    if H < A:
        print("Deficiency")
    else:
        print("Excess")