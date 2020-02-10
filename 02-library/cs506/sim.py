import math
def euclidean_dist(x, y):
    if len(x) != len(y):
        return "Vectors have different dimention"
    else:
        sum = 0
        for i in range(len(x)):
            sum = sum + (x[i] - y[i])*(x[i] - y[i])
        distance = math.sqrt(sum)
        return distance

def manhattan_dist(x, y):
    if len(x) != len(y):
        return "Vectors have different dimention"
    else:
        sum = 0
        for i in range(len(x)):
            sum = sum + abs(x[i] - y[i])
        
        return sum

def jaccard_dist(x, y):
    same = 0
    diff = 0
    if len(x) <= len(y):
        for i in range(len(x)):
            if abs(x[i] - y[i]) == 0:
                same = same + 1
            else:
                diff = diff + 1
    else:
        for j in range(len(y)):
            if abs(y[j] - x[j]) == 0:
                same = same + 1
            else:
                diff = diff + 1

    distance = 1 - same / (same + diff)
    return distance

def cosine_sim(x, y):
    if len(x) != len(y):
        return "Vectors have different dimention"
    else:
        numerator = 0
        denominator_compo1 = 0
        denominator_compo2 = 0
        for i in range(len(x)):
            numerator = numerator + x[i] * y[i]
            denominator_compo1 += x[i] * x[i]
            denominator_compo2 += y[i] * y[i]
        
        deno1_sqrt = math.sqrt(denominator_compo1)
        deno2_sqrt = math.sqrt(denominator_compo2)
        sim = numerator / (deno1_sqrt * deno2_sqrt)
        return sim
