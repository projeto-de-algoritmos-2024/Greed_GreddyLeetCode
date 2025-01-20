import heapq
from typing import List
from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # guardar tempos de término de cada servidor em uma heap de mínimo
        # manter os servidores livres em uma sortedlist
        # manter o número de operações de cada servidor em uma lista count
        # para cada request:
          # atualizar os servidores livres
          # alocar o request para um servidor disponível se possível
        # retornar os maiores servidores do vetor count
        
        finish_time_heap = []
        idle_servers = SortedList()
        server_count = [0] * k
        
        for server in range(k):
          idle_servers.add(server)
        
        for request in range(len(arrival)):
          while len(finish_time_heap) != 0 and finish_time_heap[0][0] <= arrival[request]:
            idle_servers.add(heapq.heappop(finish_time_heap)[1])
            
          if len(idle_servers) == 0:
            continue
          
          id = request % k
          server_index = idle_servers.bisect_left(id)
          if server_index == len(idle_servers):
            server_index = idle_servers.bisect_left(0)
          selected_server = idle_servers[server_index]
          
          idle_servers.remove(selected_server)
          heapq.heappush(finish_time_heap, (arrival[request] + load[request], selected_server))
          server_count[selected_server] += 1
          
          # if len(idle_servers) > 0:
          #   for i in range(k):
          #     server_id = (request + i) % k
          #     if (server_id in idle_servers):
          #       idle_servers.remove(server_id)
          #       heapq.heappush(finish_time_heap, (arrival[request] + load[request], server_id))
          #       server_count[server_id] += 1
          #       break
        #   print(finish_time_heap)
        # print(server_count)
        
        max_count = max(server_count)
        ans = []
        for server in range(k):
          if server_count[server] == max_count:
            ans.append(server)
        return ans
            
          
print(Solution.busiestServers(Solution, k = 3, arrival = [1,2,3], load = [10,12,11] ))