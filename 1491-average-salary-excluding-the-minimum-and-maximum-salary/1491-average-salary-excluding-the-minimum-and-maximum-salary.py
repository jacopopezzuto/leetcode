class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = maximum = salary[0]
        result = 0
        for i in range(len(salary)):
            minimum = min(minimum, salary[i])
            maximum = max(maximum,salary[i])
            result += salary[i]
        return (result-minimum-maximum)/(len(salary)-2)