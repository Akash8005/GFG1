#User function Template for python3
##############################################  Find All Four Sum Numbers ############3 PROBLEM CODE : FAFSN, GFG
# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, L, K):
        # code here
        L.sort()
        res = []
        for i in range(3,len(L)):
             empL = []
             for j in range(2,i):
                 for k in range(1,j):
                      for l in range(0,k):
                          if(L[i]+L[j]+L[k]+L[l] == K):
                    # count = count + 1;
                            #   if(L[i] not in empL):
                                    empL = []
                                    empL.append(L[i])
                            #   if(L[j] not in empL):
                                    empL.append(L[j])
                            #   if(L[k] not in empL):
                                    empL.append(L[k])
                            #   if(L[l] not in empL):
                                    empL.append(L[l])
                                    empL.sort()
                                    if(empL not in res and sum(empL) == K ):
                                       res.append(empL)
                                       empL = []
                    # print(L[i],L[j],L[k],L[l]);
# print(count);
# print(res);
        return sorted(res);