
def IsAscending(A):
    i = 0
    f = True
    while f and i + 1 < len(A):
        f = A[i] < A[i + 1]
        i += 1
    return f

lt = list(map(int, input()))
print('YES' if IsAscending(lt) else 'NO')
