def solve(self, s):
  mapp = {')':'(', '}':'{', ']':'['}
  ans = []
  for i in s:
    if i in mapp.values():
      ans.append(i)
    else:
      if not ans or ans[-1] != mapp[i]:
        return False
      ans.pop()
  return not(ans)
