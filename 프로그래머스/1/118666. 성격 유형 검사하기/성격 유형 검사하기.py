def solution(survey, choices):
    scores = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M': 0, 'A': 0, 'N': 0}
 
    for i in range(len(choices)):
        if choices[i] == 1:
            scores[survey[i][0]] += 3
        elif choices[i] == 2:
            scores[survey[i][0]] += 2
        elif choices[i] == 3:
            scores[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
             scores[survey[i][1]] += 1
        elif choices[i] == 6:
             scores[survey[i][1]] += 2
        elif choices[i] == 7:
            scores[survey[i][1]] += 3
            
    result = ""
    if scores["R"] >= scores["T"]:
        result += "R"
    else:
        result += "T"
    
    if scores["C"] >= scores["F"]:
        result += "C"
    else:
        result += "F"
    
    if scores["J"] >= scores["M"]:
        result += "J"
    else:
        result += "M"
        
    if scores["A"] >= scores["N"]:
        result += "A"
    else:
        result += "N"
    
    
        
    answer = result
    return answer