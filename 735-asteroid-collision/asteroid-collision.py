class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            survived = True

            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()

                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    survived = False
                    break

                else:
                    survived = False
                    break

            if survived:
                stack.append(asteroid)

        return stack
        