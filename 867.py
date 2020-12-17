# maybe best Solution
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(line) for line in zip(*A)]



'''
# my Solution
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = [[item] for item in A[0]]
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                B[j].append(A[i][j])
        return B
'''