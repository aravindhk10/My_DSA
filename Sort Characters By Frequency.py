class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        arr = defaultdict(list)
        for i, j in d.items():
            arr[j].append(i)
        res = []
        for i in range(len(s),0,-1):
            for j in arr[i]:
                res.append(j*i)
        return "".join(res)
