from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            print('@dfs({},{})'.format(i,j))
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                print(' Return grid[{}][{}]'.format(i, j))
                return
            print(' @grid[{}][{}]:{}'.format(i, j, grid[i][j]))
            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    print('bfound')
                    count += 1
        return count

if __name__ == '__main__':
    # i is y, j is x

    sol = Solution()
    # grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
    grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]

    ans = sol.numIslands(grid)
    print(ans)