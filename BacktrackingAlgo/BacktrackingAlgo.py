
#Todo: N - Queens Problem
class NQueens:
    def __init__(self,n):
        self.directions_num=n
        self.queens_num=n
        self.chess_table=[[0 for i in range(self.directions_num)] for j in range(self.directions_num)]

    def print_queens(self):
        for i in range(self.directions_num):
            for j in range(self.directions_num):
                if self.chess_table[i][j]:
                    print(" Q ",end="  ")
                else:
                    print(" - ",end="  ")
            print("\n")
        
    def is_place_valid(self,row_index,col_index):
        #checks horizontally
        for i in range(self.directions_num):
            if self.chess_table[row_index][i]:
                return False
        
        #to top left
        j=col_index
        for i in range(row_index,-1,-1):
            if i < 0:
                break
            if self.chess_table[i][j]:
                return False
            j-=1
        #to bottom left *there is not any Queens in right ^_^*
        j=col_index
        for i in range(row_index,self.directions_num):
            if i < 0:
                break
            if self.chess_table[i][j]:
                return False
            j-=1
        return True

    def solve(self,col_index):
        if col_index == self.directions_num:
            return True
        for row_index in range(self.directions_num):
            if self.is_place_valid(row_index,col_index):
                self.chess_table[row_index][col_index] = 1
                if self.solve(col_index+1):
                    return True
                else:
                    self.chess_table[row_index][col_index] = 0
        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("There is no solution") 


queens = NQueens(8)
queens.solve_NQueens()





