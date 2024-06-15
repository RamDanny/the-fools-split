import string, random
import os
letters = list(string.ascii_uppercase)
numbers = list(string.digits)

def generate_name():
    return random.choice(letters) + random.choice(numbers)

def isvalid(name, arr):
    return True if name in arr else False

def gen_output(N, arr, mat):
    for i in range(N):
        name = arr[i]
        print(f'{name} owes ', end='')
        isempty = True
        for j in range(N):
            debt = mat[i][j]
            if debt > 0:
                isempty = False
                print(f'{debt} to {arr[j]}  ', end='')
        if isempty:
            print(f'nothing!', end='')
        print()
    print()

def add_payment(N, arr, mat):
    amt = int(input('Amount = '))
    paidby = input('Paid by = ')
    include = input('Include = ').split(' ')
    for name in include:
        if not isvalid(name, arr):
            break
    yet_to_add = len(include)
    due = amt / (len(include)+1)
    for i in range(N):
        for j in range(N):
            if yet_to_add <= 0:
                break
            if arr[i] in include and arr[j] == paidby:
                mat[i][j] += due
                yet_to_add -= 1

def resolve_dues(N, arr, mat):
    # resolve commutative
    for i in range(N):
        for j in range(N):
            if i != j:
                if mat[i][j] > mat[j][i]:
                    mat[i][j] -= mat[j][i]
                    mat[j][i] = 0
                elif mat[i][j] < mat[j][i]:
                    mat[j][i] -= mat[i][j]
                    mat[i][j] = 0
                else:
                    mat[i][j], mat[j][i] = 0, 0
    # resolve transitive
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i != j and j != k and k != i:
                    if mat[i][k] > mat[k][j] > 0:
                        mat[i][j] += mat[i][k] - mat[k][j]
                        mat[i][k] -= mat[k][j]
                    elif mat[k][j] > mat[i][k] > 0:
                        mat[i][j] += mat[k][j] - mat[i][k]
                        mat[k][j] -= mat[i][k]
                    elif mat[k][j] == mat[i][k] > 0:
                        mat[i][j] += mat[i][k]
                        mat[i][k] = 0
                        mat[k][j] = 0

def main():
    N = int(input('Number of people = '))
    arr = [generate_name() for i in range(N)]
    mat = [[0 for i in range(N)] for j in range(N)]
    while True:
        os.system('cls')
        print('\t\tThe Fool\'s Split\t\t\n')
        gen_output(N, arr, mat)
        choice = input('Enter (a) Add Payment (s) Resolve Dues (q) Quit : ').lower()
        if choice == 'q':
            break
        elif choice == 'a':
            add_payment(N, arr, mat)
        elif choice == 's':
            resolve_dues(N, arr, mat)
    #print(arr, mat)

if __name__ == '__main__':
    main()
