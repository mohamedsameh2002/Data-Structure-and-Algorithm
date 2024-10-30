"""
Given N number of activities with their start and end times.
We need to select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.
"""
def max_activities(activities:list):
    activities.sort(key=lambda x:x[2])
    current_activity=activities[0]
    print(current_activity[0])
    for next_activity in range(1,len(activities)):
        if current_activity[2] < activities[next_activity][1]:
            print(activities[next_activity][0])
            current_activity=activities[next_activity]

activities=[
    ["A1",0,6],
    ["A2",3,4],
    ["A3",1,2],
    ["A4",5,8],
    ["A5",5,7],
    ["A6",8,9],
]

# max_activities(activities)

#!--------------------------------------------------------------
"""
You are given coins of different denominations and total amount of money.
Find the minimum number of coins that you need yo make up the given amount.
Infinite supply of denominations: {1,2,5,10,20,50,100,1000}
"""

def coin_change(totalNumber,coins:list):
    coins.sort()
    n=totalNumber
    index=len(coins)-1
    while True:
        if n >= coins[index]:
            print(coins[index])
            n-=coins[index]
        if n < coins[index]:
            index-=1
        if n == 0:
            break

coins=[1000,20,5,100,2,50,10,1]
# coin_change(2003,coins)

#!--------------------------------------------------------------
"""
Given a set of items, each with a weight and a value,
determine the number of each item to include in a collection
so that the total weight is less than or equal to a given limit
and the total value is as large as possible.
"""
class Item:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.ratio=value/weight

def fractional_knapsack(items:list,capacity):
    items.sort(key=lambda x:x.ratio,reverse=True)
    used_capacity = 0
    total_value = 0
    for i in items:
        if i.weight+used_capacity <= capacity:
            total_value+=i.value
            used_capacity+=i.weight
        else:
            unused_capacity=capacity - used_capacity
            total_value+=i.ratio * unused_capacity
            used_capacity+=unused_capacity
        if used_capacity == capacity:
            break
    print("Total value obtained: "+str(total_value))

item1=Item(20,100)
item2=Item(30,120)
item3=Item(10,60)
all_items=[item1,item2,item3]
fractional_knapsack(all_items,50)