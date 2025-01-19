import bisect
import heapq
from multiprocessing import heap
from typing import List

class Solution:
  def minGroups(self, intervals: List[List[int]]) -> int:
    # order intervals by start time
    # then for each interval, find the first group that ends before the start time
    # keep track of the end time of the group
    # store groups in a max heap
    
    groups = []
    # intervals.sort() # this already orders them by start time somehow?
    intervals.sort(key=lambda x : x[0])
    # print("sorted intervals:", intervals)
    
    first_interval = intervals.pop(0)
    heapq.heappush(groups, [[first_interval[1], first_interval[0]]])
    for interval in intervals:
      head_group : List[List[int]] = groups[0]
      group_end_time = head_group[0][0]
      if (group_end_time) < interval[0]:
        head_group.insert(0, [interval[1], interval[0]])
        heapq.heapreplace(groups, head_group)
      else:
        # create a new group
        heapq.heappush(groups, [[interval[1], interval[0]]])
      # print(groups)

    return len(groups)
    
print(Solution.minGroups(Solution, [[441459,446342],[801308,840640],[871890,963447],[228525,336985],[807945,946787],[479815,507766],[693292,944029],[751962,821744]]))