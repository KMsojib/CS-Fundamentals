# Algorithms Name  : Kadane's Algorithm
# Time Complexity  : O(n)

#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int>nums = {1,2,3,4,5};
    int maxSum = nums[0];
    int curnSum = 0;

    for(auto num : nums){
        curnSum = max(curnSum, 0);
        curnSum += num;
        maxSum = max(maxSum,curnSum);
    }
    printf("maxium Subarray sum %d",maxSum);
    return 0;
}