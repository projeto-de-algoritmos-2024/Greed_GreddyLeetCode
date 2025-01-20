class Solution:
    def minCostConnectPoints(self, points):
        
        # Função para calcular a distância de Manhattan
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Construir as arestas com suas respectivas distâncias
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan_distance(points[i], points[j])
                edges.append((distance, i, j))
        
        # Ordenar as arestas pelo peso (distância)
        edges.sort()
        
        # Implementar o Union-Find
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False
        
        # Kruskal para encontrar a MST
        cost = 0
        for distance, u, v in edges:
            if union(u, v):
                cost += distance

        return cost
