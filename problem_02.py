def max_subarray_sum(arr, k):
    n = len(arr)
    if n < k or k <= 0:
        print("Entrada inválida")  #fix: Verificação para entrada inválida
        return -1

    max_sum = sum(arr[:k])  #fix: Inicialização correta do máximo de soma
    window_sum = max_sum

    for i in range(1, n - k + 1):
        window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
        max_sum = max(max_sum, window_sum)

    return max_sum

def read_input():
    try:
        arr = list(map(int, input("Digite os números da matriz separados por espaços: ").split()))
        k = int(input("Digite o tamanho da submatriz (k): "))
        if k <= 0:
            raise ValueError("k deve ser um número positivo")  #fix: Verificação para k positivo
        return arr, k
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return [], 0

def main():
    arr, k = read_input()
    result = max_subarray_sum(arr, k)
    if result != -1:
        print(f"Soma máxima de uma submatriz de tamanho {k} é {result}")

if __name__ == "__main__":
    main()
