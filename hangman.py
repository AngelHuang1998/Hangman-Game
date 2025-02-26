from turtle import *
from time import sleep
from drawing import people, car, last_car, draw_blood_splatter


def question():
    """ 提示使用者輸入問題 """
    ques = textinput("Hangman Game", "Enter the word you want others to guess:")
    print(ques)
    return ques


def solution(solution):
    """ 顯示要猜的單字個數(以底線表示) """
    penup()
    goto(-260, 140)
    pendown()
    color('black')
    num_letters = len(solution)
    for _ in range(num_letters):    #根據字長畫底線
        write("_", align='left', font=('Arial', 30, 'normal'))
        penup()
        forward(25)
        pendown()


def left_time(time):
    """ 顯示剩餘時間 """
    penup()
    goto(100, 200)
    pendown()
    color("white")   #用白色覆蓋掉本來的left time
    write("Time Left : " + str(time + 1), align='left', font=('Arial', 25, 'normal'))
    color("black")   #再用黑色寫上剩餘的left time
    write("Time Left : " + str(time), align='left', font=('Arial', 25, 'normal'))



def answer(solution):
    """ 處理遊戲回答邏輯 """
    solution_list = list(solution.lower())  # 把題目存成list。eg. she => solution_list = ['s','h','e']
    opportunity = 5  #總共給予5次猜題機會
    correct_count = 0  #紀錄正確次數
    left_time(opportunity)    #顯示剩餘次數(初始次數為5)

    while opportunity > 0:
        ans_letter = textinput("Guess the word!", "Enter the word:")
        ans_letter = ans_letter.lower()   #統一用小寫字母

        if ans_letter in solution_list:   #如果猜的字有在題目內
            while ans_letter in solution_list:  #用while的原因是因為，題目中可能有相同的字母出現。例如:['h','e','l','l','o']
                correct_count += 1
                penup()
                goto(-260, 140)
                forward(25 * solution_list.index(ans_letter))   #看猜對的字在第幾格位子，就要往前多少
                pendown()
                color('black')
                write(ans_letter, align='left', font=('Arial', 30, 'normal'))   #在對應的空格印出猜對的字
                solution_list[solution_list.index(ans_letter)] = None   #把猜對的字母，從題目list中移除
          

            if correct_count == len(solution):    #全部猜對
                penup()
                goto(-165, -200)
                pendown()
                color('Green')
                write("!!SUCCESS!!", align='left', font=('Arial', 40, 'normal'))
                return    #結束
            


        else:            #如果猜的字"沒有"在題目內
            opportunity -= 1  #機會減少一次
            left_time(opportunity)  #顯示剩餘次數
            if opportunity > 0:   
                car(opportunity)    #繪製車子位子(車子位子是根據剩餘機會來決定。機會越少就離人愈近)

        sleep(0.5)


    last_car()   #機會用完了(挑戰失敗)，就繪製被車撞圖
    draw_blood_splatter()   #繪製血液噴濺
    penup()
    goto(-115, -200)
    pendown()
    color('Red')
    write("!!Failed!!", align='left', font=('Arial', 40, 'normal'))




# 遊戲流程
ques = question()   # 玩家輸入題目
people()            # 畫人在畫面上
car(5)              # 繪製車子(於起始位子)
solution(ques)      # 繪製題目的底線(依照題目長度)
answer(ques)        # 進行遊戲回答邏輯

done()
