class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        
        row_vectors = self.convert_to_row_vectors(A)
        col_vectors = self.convert_to_col_vectors(B)
        
        matrix = [] 
        
        for row_vector in row_vectors:
            
            row = []
            
            for col_vector in col_vectors:
                
                row.append(self.multiply_vectors(row_vector, col_vector))
                
            matrix.append(row)
            
        return matrix
        
    def convert_to_row_vectors(self, matrix):
        
        vectors = [] 
        
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n):
            
            vector = [] 
            
            for j in range(m):
                
                if matrix[i][j] != 0:
                    
                    vector.append((j, matrix[i][j]))
                    
            vectors.append(vector)
            
        return vectors
        
        
    def convert_to_col_vectors(self, matrix):
        
        vectors = [] 
        
        n, m = len(matrix), len(matrix[0])
        
        for j in range(m):
            
            vector = [] 
            
            for i in range(n):
                
                if matrix[i][j] != 0:
                    
                    vector.append((i, matrix[i][j]))
                    
            vectors.append(vector)
            
        return vectors
        
    def multiply_vectors(self, row_vector, col_vector):
        
        i, j = 0, 0 
        
        result = 0 
        
        while i < len(row_vector) and j < len(col_vector):
            
            if row_vector[i][0] < col_vector[j][0]:
                
                i += 1 
                
            elif row_vector[i][0] > col_vector[j][0]:
                
                j += 1 
                
            else:
                
                result += row_vector[i][1] * col_vector[j][1]
                
                i += 1 
                j += 1
                
        return result