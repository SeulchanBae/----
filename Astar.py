import queue

#상태를 나타내는 클래스, f(n)값을 저장한다.
class State:
    def __init __(self, board, goal, depth=0):
        self.board = board  #현재의 보드 길이
        self.depth = depth  #깊이
        self.goal = goal    #목표 상태

# i1과 i2를 교환하여서 새로운 상태를 반환한다.
def get_new_board(self, i1, i2, depth):
    new_board = self.board[:]
    new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
    return State(new_board, self.goal, depth)

# 자식 노드를 확장하여서 리스틍 저장하여서 반환한다.
def expand (self,moves):
    result = []
    i = self.board.index(0) # 숫자 0(빈칸)의 위치를 찾는다.
    if not i in [0, 3, 6]:  # LEFT 연산자
        result,append(self, get_new_board(i, i-1, moves))
    if not i in [0, 1, 2]:  # UP연산자
        result,append(self, get_new_board(i, i-3, moves))
    if not i in [2, 5, 8]:  # UP연산자
        result,append(self, get_new_board(i, i+1, moves))
    if not i in [6, 7, 8]:  # UP연산자
        result,append(self, get_new_board(i, i+3, moves))
    return result

# f(n)을 계산하여 반환한다,
def f(self):
    return self.h()+self.g()

# 휴리스틱 함수값인 h(n)을 계산하여 반환한다.
# 현제 제 위치에 있지 않은 타일의 개수를 계산하여 반환한다.
def h(self):
    score = 0
    for i in range(9)
        if self.board[i]!=0 and self.board[i] != self.goal[i]:
            score += 1
