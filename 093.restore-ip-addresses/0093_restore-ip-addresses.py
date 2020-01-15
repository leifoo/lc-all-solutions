class Solution(object):
    def restoreIpAddresses(self, s):

        def isValid(c):
            if not c:
                return False
            
            if c[0] == '0' and len(c) > 1:
                return False

            if 0 <= int(c) < 256:
                return True
            
            return False

        if not s:
            return []

        length = len(s)
        res = []

        def helper(pos = 0, temp = []):
            print(pos, temp)
            if pos == length and len(temp) == 4:
                res.append('.'.join(temp))
            elif len(temp) < 4:
                for i in range(3):
                    if pos + i < length:
                        ts = s[pos : pos+1+i]
                        if isValid(ts):
                            temp.append(ts)
                            helper(pos + i + 1, temp)
                            temp.pop()

        helper()
        return res

if __name__ == "__main__":
    y = Solution()
    x = "25525511135"
    print(x, y.restoreIpAddresses(x))