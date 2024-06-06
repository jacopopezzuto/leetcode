class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = {}
        for c in words[0]:
            if c not in common:
                common[c] = 1
            else:
                common[c] += 1

        for i in range(1, len(words)):
            current = {}
            for c in words[i]:
                if c not in current:
                    current[c] = 1
                else:
                    current[c] += 1

            keys_to_remove = []
            for key in common:
                if key in current:
                    common[key] = min(common[key], current[key])
                else:
                    keys_to_remove.append(key)

            for key in keys_to_remove:
                del common[key]

        result = []
        for key, count in common.items():
            result.extend([key] * count)

        return result