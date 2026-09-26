class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """

        # Convert knowledge into a dictionary
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                start = i

                # Find closing bracket
                while s[i] != ')':
                    i += 1

                key = s[start:i]

                # Replace with value or '?'
                if key in mp:
                    result.append(mp[key])
                else:
                    result.append('?')

                i += 1

            else:
                result.append(s[i])
                i += 1

        return ''.join(result)