def max_profit(w: int, weights: list[int], costs: list[int]) -> int:
    n = len(weights)
    dp = [[0 for _ in range(w + 1)]for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(0, w + 1):
            dp[i][j] = dp[i - 1][j]
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i - 1]] + costs[i - 1])
    [print(*i) for i in  dp]
    return dp[-1][-1]


if __name__ == '__main__':
    W = 13
    w = [3, 4, 5, 8, 9]
    c = [1, 6, 4, 7, 6]
    # _, W = map(int, input().split())
    # w = list(map(int, input().split()))
    # c = list(map(int, input().split()))
    cost = max_profit(W, w, c)
    print(f"{cost}")

