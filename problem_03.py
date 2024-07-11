def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Não é possível multiplicar as matrizes: dimensões incompatíveis.")  # Corrigido: Mensagem de erro mais clara
        return None

    #fix: Inicializa a matriz de resultado com zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    #fix: Realiza a multiplicação das matrizes
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  #fix: Range ajustado para cols_A
                result[i][j] += A[i][k] * B[k][j]

    return result

def read_matrix():
    try:
        rows = int(input("Digite o número de linhas: "))
        cols = int(input("Digite o número de colunas: "))
        print("Digite os elementos da matriz linha por linha:")
        matrix = []
        for _ in range(rows):
            row = list(map(int, input().split()))
            if len(row) != cols:
                print("Comprimento inválido da linha.")  #fix: Mensagem de erro mais clara
                return None
            matrix.append(row)
        return matrix
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros.")  #fix: Mensagem de erro mais clara
        return None

def main():
    print("Matriz A:")
    A = read_matrix()
    if A is None:
        return

    print("Matriz B:")
    B = read_matrix()
    if B is None:
        return

    result = matrix_multiply(A, B)
    if result is not None:
        print("Matriz resultante:")
        for row in result:
            print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
