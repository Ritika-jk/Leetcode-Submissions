class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD = 1000000007
        n = len(board)

        score = [-1] * (n + 1)
        ways = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            diagonal_score = -1
            diagonal_ways = 0

            for j in range(n - 1, -1, -1):
                down_score = score[j]
                down_ways = ways[j]

                cell = board[i][j]

                if cell == 'X':
                    score[j] = -1
                    ways[j] = 0

                elif cell == 'S':
                    score[j] = 0
                    ways[j] = 1

                else:
                    right_score = score[j + 1]
                    right_ways = ways[j + 1]

                    best = down_score

                    if right_score > best:
                        best = right_score

                    if diagonal_score > best:
                        best = diagonal_score

                    if best == -1:
                        score[j] = -1
                        ways[j] = 0
                    else:
                        count = 0

                        if down_score == best:
                            count += down_ways

                        if right_score == best:
                            count += right_ways

                        if diagonal_score == best:
                            count += diagonal_ways

                        value = 0 if cell == 'E' else ord(cell) - 48

                        score[j] = best + value
                        ways[j] = count % MOD

                diagonal_score = down_score
                diagonal_ways = down_ways

        if score[0] == -1:
            return [0, 0]

        return [score[0], ways[0]]