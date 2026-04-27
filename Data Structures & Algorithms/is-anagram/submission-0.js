class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        

        const lettersS = s.split("").sort()
        const lettersT = t.split("").sort()
        if (lettersS.length !== lettersT.length){
            return false
        }

        for (const i in lettersS){
            if (lettersS[i] !== lettersT[i]){
                return false
            }
        }
        return true
    }
}
