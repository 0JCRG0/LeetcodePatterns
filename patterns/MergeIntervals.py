from typing import List

class MergeIntervalSolutions:
    def MergeInterval_56(self, intervals: List[List[int]] = [[1,3],[2,6],[8,10],[15,18]]):
        """
        56. Merge Intervals

        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
        return an array of the non-overlapping intervals that cover all the intervals in the input.

        Example 1:

        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
        Example 2:

        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.
        

        Constraints:

        1 <= intervals.length <= 104
        intervals[i].length == 2
        0 <= starti <= endi <= 104
        """

        intervals.sort(key=lambda x:x[0])


        merged = [intervals[0]]

        for current in intervals[1:]:
            previous = merged[-1]

            if previous[1] >= current[0]:
                #print(f"previous[1], current[0]: {previous[1], current[0]}")
                #We create the list with the max value
                merged[-1] = [previous[0], max(previous[1], current[1])]
            else:
                merged.append(current)
        return merged



if __name__ == "__main__":
    instance = MergeIntervalSolutions()
    ans = instance.MergeInterval_56()
    print(ans)



