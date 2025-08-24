class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[] #to store the result arrays
        #creating board with places initialised to .
        board=[]
        for i in range(n):
            r=[]
            for j in range(n):
                r.append(".")
            board.append(r)
        # these 3 sets store the tags and tell us whether the pos is valid or not
        cols=set()
        diag1=set() #row-col
        diag2=set() #row+col

        def fun(row):
            if row==n:#success 
                #converting to string of arrays
                sol=[]
                for i in board:
                    sol.append("".join(i))
                res.append(sol)
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    #invalid pos
                    continue
                #take
                board[row][col]="Q"
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                fun(row+1)#recurssive call for next row
                #not-take
                board[row][col]="."
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

        fun(0)
        return res

        
