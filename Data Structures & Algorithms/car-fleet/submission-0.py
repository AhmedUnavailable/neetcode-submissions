class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = list(zip(position, speed))
        l.sort(reverse=True)

        stack  = []
        for p, s in l:
            arrival = (target - p) / s
            
            if not stack:
                stack.append(arrival)

            if stack and arrival > stack[-1]:
                stack.append(arrival)
             

        return len(stack)
