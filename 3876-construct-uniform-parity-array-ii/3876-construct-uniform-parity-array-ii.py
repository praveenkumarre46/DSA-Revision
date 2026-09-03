class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        eventrue=True
        for i in range(len(nums1)):
            partial=False
            if nums1[i]%2==0:
                partial=True
            else:
                for j in range(len(nums1)):
                    if i!=j:
                        if nums1[i]-nums1[j]>=1 and (nums1[i]-nums1[j])%2==0:
                            partial=True
            if partial==False:
                eventrue=partial
                break

        oddtrue=True
        for i in range(len(nums1)):
            partial=False
            if nums1[i]%2!=0:
                partial=True
            else:
                for j in range(len(nums1)):
                    if i!=j:
                        if nums1[i]-nums1[j]>=1 and (nums1[i]-nums1[j])%2!=0:
                            partial=True
            if partial==False:
                oddtrue=partial
                break


        return eventrue or oddtrue
                

