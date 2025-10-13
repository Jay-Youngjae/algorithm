def solution(video_len, pos, op_start, op_end, commands):
    def time(time):
        minute, second = time.split(":")
        minute = int(minute)
        second = int(second)
        return minute * 60 + second
    
    
    now_pos = time(pos)
    for i in range(len(commands)):
        if time(op_start) <= now_pos <= time(op_end):
            now_pos = time(op_end)
        if commands[i] == "prev":
            if now_pos <= 10:
                now_pos = 0
            else:
                now_pos -= 10
        elif commands[i] == "next":
            if time(video_len) - now_pos <= 10:
                now_pos = time(video_len)
            else:
                now_pos += 10
    if time(op_start) <= now_pos <= time(op_end):
        now_pos = time(op_end)
    minute, second = now_pos // 60, now_pos % 60
    return f"{minute:02}:{second:02}"

"""
만약 현재 위치가 오프닝 사이에 있다면 오프닝 end로이동 
10초보다 작은데 prev나오면 0초로
10초보다 적게 남은데 next나오면 맨 끝으로
"""