class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:
            if current < minimum:
                energy += minimum - current
                current = minimum
            current -= actual

        return energy