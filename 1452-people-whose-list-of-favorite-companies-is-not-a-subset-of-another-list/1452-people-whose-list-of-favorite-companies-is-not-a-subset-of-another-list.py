class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(companies) for companies in favoriteCompanies]
        result = []

        for i, current in enumerate(favoriteCompanies):
            is_subset = False
            for j, other in enumerate(favoriteCompanies):
                if i != j and current.issubset(other):
                    is_subset = True
                    break
            if not is_subset:
                result.append(i)

        return sorted(result)