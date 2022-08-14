class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_Row = False
        first_Col = False

        for i in range(0,len(matrix)):
            if(matrix[i][0] ==0):
                first_Col = True

        for i in range(0,len(matrix[0])):
            if(matrix[0][i] ==0):
                first_Row = True

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if(matrix[i][j] ==0):
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,len(matrix)):
            if(matrix[i][0]==0):
                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0

        for i in range(1,len(matrix[0])):
            if(matrix[0][i]==0):
                for j in range(1,len(matrix)):
                    matrix[j][i]=0

        if first_Row:
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0

        if first_Col:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0

        return matrix
