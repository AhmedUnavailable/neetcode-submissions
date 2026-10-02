class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]

        cars.sort(reverse=True)
        stack = []
        for p, s in cars:
            at = (target - p) / s
            if not stack or at >  stack[-1]:
                stack.append(at)     
            


        return len(stack)