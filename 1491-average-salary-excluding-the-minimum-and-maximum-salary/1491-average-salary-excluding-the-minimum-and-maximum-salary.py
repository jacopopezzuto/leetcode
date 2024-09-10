class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        salary.remove(salary[0])
        salary.remove(salary[len(salary)-1])
        result = 0
        for i in range(len(salary)):
            result += salary[i]
        return result/len(salary)