class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l = 0
        h = max(houses[-1], heaters[-1])
        radius = 0
        while l<=h:
            m = (l+h)//2
            if (self.check(m, houses, heaters)==True):
                radius = m
                h = m - 1               
            else:
                l = m + 1
        return radius

    def check(self,  radius, houses, heaters):
        i_ho = 0
        j_he = 0
        num_house = len(houses)
        num_heater = len(heaters)
        while i_ho<num_house:
            while j_he<num_heater and heaters[j_he]+radius<houses[i_ho]:
                j_he += 1
            if j_he<num_heater and abs(heaters[j_he] - houses[i_ho])<=radius:
                i_ho += 1
            else:
                return False
        return True
