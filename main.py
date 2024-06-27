'''
This is a script to calculate the longest common sequence of elements
between two sequences (lists or strings) and return the LCS string
'''


def lcs(A, B):
    # Initilise a 2D list with each element set to 0
    # this list will be used to store the length of the longest common sequence
    F = [[0]*(len(B) + 1) for i in range(len(A) + 1)]

    # iterate over each character in A, iterate over each character in B
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):

            # if the characters are equal, they are added to the sequence
            # if they are not equal, the LCS will exclude either A or B
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])

    # Trace back trough F to find the LCS
    i, j = len(A), len(B)
    lcs_result = []

    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            lcs_result.append(A[i - 1])
            i -= 1
            j -= 1
        elif F[i - 1][j] > F[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # reverse the lcs_result
    lcs_result.reverse()
    return ''.join(lcs_result)


if __name__ == "__main__":
    A = input("Enter the first sequence: ")
    B = input("Enter the second sequence : ")
    print(lcs(A, B))