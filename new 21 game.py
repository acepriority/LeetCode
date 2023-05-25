"""Alice plays the following game, loosely based on the card game "21".
Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
Alice stops drawing numbers when she gets k or more points.
Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted."""

def probabilityOfPoints(n, k, maxPts):
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(1, k + 1):
        for j in range(1, maxPts + 1):
            if i - j >= 0:
                dp[i] += dp[i - j] / maxPts

    probability = sum(dp[0:n+1])
    return probability
