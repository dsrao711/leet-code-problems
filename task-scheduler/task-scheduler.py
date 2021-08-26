class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        last_row = freq.count(max_freq)
        ans = (max_freq - 1) * (n + 1) + last_row
        return max(len(tasks),ans)