class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # code here
        arr = []
        
        for i in range(n):
            x = Items[i].value/Items[i].weight
            arr.append([x,i])
            
        arr.sort(reverse = True)
            
        currentweight = 0
        finalvalue = 0.0
        
        for i in range(n):
            if currentweight + Items[arr[i][1]].weight <= W:
                currentweight += Items[arr[i][1]].weight
                finalvalue += Items[arr[i][1]].value
            else:
                '''
                rem = W - currentweight
                finalvalue += Items[arr[i][1]].value / Items[arr[i][1]].weight * rem
                break
                '''
                finalvalue += (W - currentweight) * arr[i][0]
                break
            
        return finalvalue
        
