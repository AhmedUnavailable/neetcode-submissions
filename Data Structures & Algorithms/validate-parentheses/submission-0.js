class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        const stack = []

        for (let e of s){
            console.log(stack, stack.length -1 )
            if (!closeToOpen[e]){
                stack.push(e)
            } else {
                if (stack.length > 0 && stack[stack.length -1] === closeToOpen[e]){
                    stack.pop()
                }else{
                    return false
                }
            }
        }
        return stack.length === 0
    }
}
