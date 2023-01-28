import numpy

matrix1 = numpy.array([[4, 2, 0, 0, 5],
                       [2, 3, 1, 6, 1],
                       [0, 0, 6, 0, 5],
                       [3, 4, 0, 3, 1],
                       [0, 0, 0, 0, 5],
                       [4, 5, 6, 2, 1],
                       [5, 6, 0, 0, 5],
                       [6, 7, 0, 0, 1]], float)

class Matrix:

    def __init__(self, matrix, row=0, col=0):
        """
        :param matrix:  A 2 dimensional array as an input
        :param row:     The row (the m value) position of the pivot on matrix. The pivot can be indicated as matrix[row][column]
        :param column:  The column (the n value) position of the pivot on matrix. The pivot can be indicated as matrix[row][column].
        """
        self.matrix = matrix
        self.row = row
        self.column = col

    def sorter_v2(self):
        """ Without breaking the order of the numbers in the same column as the pivot point, assigns the row with 0 (in same column) to the bottom
        :return:       Returns sorted version of matrix
        """
        row1 = self.row
        col1 = self.column
        for i in range(self.row, numpy.shape(self.matrix)[0] - self.row + 1):
            if self.matrix[row1][col1] == 0:
                self.matrix = numpy.append(self.matrix, [self.matrix[row1]], 0)
                self.matrix = numpy.delete(self.matrix, row1, 0)
            else:
                row1 += 1
        return self.matrix


    def pivot_finder_v2(self):
        """ Checks for a non-zero element whose position is both row and column greater than the previous pivot.
         Scans the second column after completely scanning the first column from top to bottom.
        :return:        Returns the new pivot position
        """
        for i in range(numpy.shape(self.matrix)[1]):
            for j in range(numpy.shape(self.matrix)[0]):
                if i > self.row and j > self.column and self.matrix[j][i] != 0:
                    self.row, self.column = j, i
                    return self.row, self.column

    def pivot_creator(self):
        """ Checks for the pivot value (matrix[row][Column]).
        Divides the entire row containing the pivot by the value of the pivot to make the pivot value 1.
        :return:        Returns the new version of matrix
        """
        self.matrix[self.row] = self.matrix[self.row] / self.matrix[self.row][self.column]
        return self.matrix

    def zero_creator(self):
        """ Using the pivot value (which is 1) makes the values below the pivot zero.
        :return:        Returns the new version of matrix
        """

        for i in range(self.row, numpy.shape(self.matrix)[0] - 1):
            self.matrix[i + 1] = self.matrix[i + 1] - (self.matrix[self.row] * self.matrix[i + 1][self.column])
        return self.matrix


    def main(self):
        """ Synchronously executes sorter, pivot_finder, pivot_creator and zero_creator functions
        :return: Returns the new version of matrix
        """
        for i in range(4):
            self.sorter_v2()
            self.pivot_creator()
            self.zero_creator()
            self.pivot_finder_v2()
        return self.matrix

M1 = Matrix(matrix1)
print(M1.main())