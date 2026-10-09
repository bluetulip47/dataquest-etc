from itertools import combinations

# Given a list of things, of the form [[c1, r1], [c2, r2], ..., [cn, rn]],
# and the capacity y, calculate the maximum return that can be made by
# using up to one of each of the costs (so, say, r1 + r3 where c1 + c3 <= y)

def calculate_max_payout(options, capacity):
    totals = []
    max_so_far = 0
    choice = []
    for i in range(1,len(options)+1):
        for comb in combinations(options, i):
            #print(comb)
            combcost = [cost[0] for cost in comb]
            #print(sum(combcost))
            combpayout = [payout[1] for payout in comb]
            #print(sum(combpayout))
            if sum(combcost) <= capacity:
                totals.append(sum(combpayout))
                if sum(combpayout) > max_so_far:
                    max_so_far = sum(combpayout)
                    choice = comb

    #print(totals)
    #print(max_so_far)
    print("choice: " + str(choice))


options1 = [[1,3],[2,5],[3,7],[4,9]]
capacity1 = 7

calculate_max_payout(options1, capacity1)

options2 = [[4,8],[5,9],[6,10],[7,11]]
capacity2 = 10

calculate_max_payout(options2, capacity2)
