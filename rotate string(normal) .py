def rotateString(self, s: str, goal: str) -> bool:
        x = goal[0]
        for i in range(len(s)):
            if s[i] == x:
                if s[i:]+s[:i] == goal:
                    return True
        return False
