def maxprofit(prices):
  mini = prices[0]
  maxi = 0
  for i in prices:
    if i<mini:
      mini = i
    else:
      maxi = max(maxi, i - mini)
  return maxi
