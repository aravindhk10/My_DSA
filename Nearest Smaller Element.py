class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        ans = [-1]*len(A)
        st = []
        for i in range(len(A)):
            while st and st[-1]>=A[i]:
                st.pop()
            if st:
                ans[i] = st[-1]
            st.append(A[i])
        return ans
