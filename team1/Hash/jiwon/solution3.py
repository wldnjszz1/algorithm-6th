def solution(clothes):
    product = 1
    kindOfClothes = list()
    for i in range(len(clothes)):
        kindOfClothes.append(clothes[i][1])
    closet = dict()
    for i in range(len(clothes)):
        c = list()
        for j in range(len(clothes)):
            if clothes[i][1] == kindOfClothes[j]:
                c.append(clothes[j][0])
        closet[kindOfClothes[i]] = c
    for value in closet.values():
        product *= (len(value)+1)
    return product-1
    
    
