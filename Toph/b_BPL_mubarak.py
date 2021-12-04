




def ball_counter(string):
    total_ball = 0
    for ball in string:
        if ball.upper() in 'NWD': continue
        total_ball += 1
    return total_ball

def bpl_mubarak(ball: list):
    string = ''
    string_over = None
    string_ball = None
    for ball in ball:
        overs = ball // 6 
        balls = ball % 6
        string_over = 'OVER' if overs == 1 else 'OVERS'
        string_ball = 'BALL' if balls == 1 else 'BALLS'
        if overs and balls:
            print(overs, string_over, balls, string_ball)
        elif overs and not balls:
            print(overs, string_over)
        else:
            print(balls, string_ball)


bpl_mubarak([ball_counter(input()) for x in range(int(input()))])

