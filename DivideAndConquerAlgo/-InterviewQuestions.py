def number_factor():
    ...


"""
Given N number of houses along the street with
some amount of money Adjacent houses cannot be stolen
Find the maximum amount that can be stolen
"""
def house_robber(houses,current_house=0):
    if current_house >= len(houses):
        return 0
    steal_first_house=houses[current_house]+house_robber(houses,current_house+2)
    skip_first_house=house_robber(houses,current_house+1)
    return max(steal_first_house,skip_first_house)


houses=[6,7,1,30,8,2,4]
print(house_robber(houses))