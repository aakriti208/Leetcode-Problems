class Solution:
    def slidingWindow(self, s):
        window = {}
        l = 0
        res = 0
        for r in range(len(s)):
            # Add s[r] to window
            window[s[r]] = window.get(s[r], 0)
            
            while window_in_invalid:
                # shrink window
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            res = max(res, r-l+1)
        return res