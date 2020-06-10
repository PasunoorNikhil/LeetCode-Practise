" Filter Restaurants by Vegan-Friendly, Price and Distance "

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        tmp,res=[],[]
        restaurants.sort(key=lambda x :(-x[1],-x[0]))
        for restaurant in restaurants:
            if restaurant[2]>=veganFriendly:
                if restaurant[3]<=maxPrice:
                    if restaurant[4]<=maxDistance:
                        tmp.append([restaurant[0],restaurant[1]])
        
        for res_id in tmp:
            res.append(res_id[0])
        return res
        
