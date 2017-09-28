class Solution:
    def constructArray(self, n, k):

        subs = []
        possible_subs = []
        accepted_subs = []
        result = [0]*(k+1)
        subs.extend(range(1, n+1))
        possible_subs.extend(range(1, n))
        accepted_subs.extend(range(k, 0, -1))

        for i in range(0, n):
            if i == 0:
                result[i] = 1
                subs.remove(result[i])
            else:
                if i-1 < k:
                    if 0 != i % 2:
                        a = result[i-1] + accepted_subs[i-1]
                        if abs(a) in subs:
                            result[i] = a
                            subs.remove(a)
                    else:
                        b = result[i-1] - accepted_subs[i-1]
                        if abs(b) in subs:
                            result[i] = abs(b)
                            subs.remove(abs(b))
                else:
                    if k >= abs(subs[0]-result[i-1]):
                        result.extend(subs)
                        break
        return result


if __name__ == "__main__":
    s = Solution()
    output = s.constructArray(70, 15)
    print(output)




