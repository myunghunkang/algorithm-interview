from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리^
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
                print('height[i]:{} height[stack[-1]]:{}'.format(height[i], height[stack[-1]]))
                print('i:{}, height[i]:{} top{}, distance:{}, waters:{}, volume:{}'.format(i, height[i], top, distance, waters, volume))

            stack.append(i)
            print('i:{}'.format(i))
        return volume
