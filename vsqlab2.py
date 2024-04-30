B_n = input("B(n) massivini rəqəmlərlə boşluq simvolləri ilə daxil edin: ")
B_n = [int(x) for x in B_n.split()]


def tek_indeksli_elementlerin_cemi(B_n):
    cem = 0
    for i in range(len(B_n)):
        if i % 2 == 0:
            cem += B_n[i]
    return cem

cem = tek_indeksli_elementlerin_cemi(B_n)

print("B(n) siyahısının tək indeksli elementlərinin cəmi:", cem)