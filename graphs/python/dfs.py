    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            curr = stack.pop()
            print(curr)

            for adjV in self.gdict[curr]:
                if adjV not in visited:
                    visited.append(adjV)
                    stack.append(adjV)
