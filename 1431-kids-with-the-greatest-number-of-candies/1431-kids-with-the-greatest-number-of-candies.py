class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy=candies[0]
        for i in range(len(candies)):
            max_candy = max(max_candy, candies[i])
        result = [False]*len(candies)
        for i in range(len(candies)):
            result[i]=candies[i]+extraCandies>=max_candy
        return result
            