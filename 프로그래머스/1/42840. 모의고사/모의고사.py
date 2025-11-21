def solution(answers):
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    points = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if (answers[i] == ans_1[i%len(ans_1)]):
            points[1] += 1
        if (answers[i] == ans_2[i%len(ans_2)]):
            points[2] += 1
        if (answers[i] == ans_3[i%len(ans_3)]):
            points[3] += 1
        
    max_value = max(points.values())
    max_keys = []
    for key, value in points.items():
        if (value == max_value):
            max_keys.append(key)
    return max_keys