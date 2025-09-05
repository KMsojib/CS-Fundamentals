# Agorithms Name   : Kadane's Algorithm Brute Forces Implmenation.
# Time Complexity  : O(n^2)

#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int>nums = {1,2,3,4,5};
    int maxSum = nums[0];

    for (int i = 0; i < nums.size(); i++) {
        int curSum = 0;
        for (int j = i; j < nums.size(); j++) {
            curSum += nums[j];
            maxSum = max(maxSum, curSum);
        }
    }
    printf("Maximum Subarray sum %d",maxSum);

    return 0;
}