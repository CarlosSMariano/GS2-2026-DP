def knapsack(custo, beneficio, orcamento):
    n = len(beneficio)

    matriz = [[0 for _ in range(orcamento + 1)]for _ in range(n + 1)]

    for row in range(1, n+1):
        for col in range(1, orcamento+1):
            if custo[row - 1] <= col: 
                matriz[row][col] = max(
                    matriz[row - 1][col], 
                    beneficio[row - 1] + matriz[row - 1][col - custo[row - 1]]
                )
            else: 
                matriz[row][col] = matriz[row - 1][col]

    valor_maximo = matriz[n][orcamento]

    itens_escolhidos = []
    w = orcamento

    for i in range(n,0,-1):
        if matriz[i - 1][w] != matriz[i][w]:
            itens_escolhidos.append(i - 1)
            w -= custo[i - 1]

    return valor_maximo, itens_escolhidos[::-1]