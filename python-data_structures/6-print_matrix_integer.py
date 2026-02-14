#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Əgər element sətirin sonuncusu deyilsə, boşluqla çap et
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                # Sonuncu elementdirsə, boşluqsuz çap et
                print("{:d}".format(row[i]), end="")
        # Hər sətirdən sonra yeni sətirə keç
        print()
