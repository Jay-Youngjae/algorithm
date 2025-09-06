N = int(input())                                                              
M = int(input())                                                              
students = list(map(int, input().split()))                                    
picture = []                                                                  
cnt = {}                                                                      
order = {}                                                                    
                                                                              
for t, s in enumerate(students): # enumerate : idx, value를 각각 받는다             
    if s in picture: # 만약 사진틀에 학생이 있으면                                        
        cnt[s] += 1  # 해당 학생 카운트 증가                                           
        continue                                                              
                                                                              
    if len(picture) < N: # 사진틀에 자리가 있으면                                       
        picture.append(s) # 학생 추가                                             
        cnt[s] = 1    # 처음 들어왔으니까 초기화                                         
        order[s] = t                                                          
    else: # 사진틀에 자리가 없으면 -> 비우기                                               
        min_student = min(picture, key = lambda x: (cnt[x], order[x]))        
        picture.remove(min_student) # remove: 값 제거, pop: 인덱스 제거               
        cnt[min_student] = 0                                                  
        order[min_student] = 0                                                
                                                                              
        # 자리 비웠으면 추가                                                          
        picture.append(s)                                                     
        cnt[s] = 1                                                            
        order[s] = t                                                          
                                                                              
picture = sorted(picture)                                                     
print(*picture)                                                               