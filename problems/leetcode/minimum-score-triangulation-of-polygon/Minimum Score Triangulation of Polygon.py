class Solution:
    def minScoreTriangulation(self, values):
        self.memory = {}
        return self.triangulate(values)
    
    def triangulate(self, values):
        key = str(values)
        if key not in self.memory:
            if len(values) == 3:
                self.memory[key] = values[0]*values[1]*values[2]
            else:
                triangulations = [values[0]*values[1]*values[-1] + self.triangulate(values[1:])]    
                for i in range(2, len(values)-1):
                    triangulations.append(self.triangulate(values[:i+1])+self.triangulate([values[0]]+values[i:]))
                self.memory[key] = min(triangulations)
        return self.memory[key]
