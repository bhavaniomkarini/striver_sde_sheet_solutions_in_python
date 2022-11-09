#User function Template for python3
class Solution:
    
    def func(self,ind, summ, arr, N, ansarr):
        if(ind == N):
            ansarr.append(summ)
            return 
        self.func(ind+1, summ+arr[ind], arr, N, ansarr)
        self.func(ind+1, summ, arr, N, ansarr)
        
	def subsetSums(self, arr, N):
		# code here
		ansarr = []
		self.func(0, 0, arr, N, ansarr)
		ansarr = sorted(ansarr)
		return ansarr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends
