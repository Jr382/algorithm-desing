/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    int* count = (int*)malloc(numsSize*sizeof(int));
    int expected = numsSize*(numsSize+1)/2, actual = 0;
    for(int i = 0; i < numsSize; i++){
        count[i] = 0;
        actual += nums[i];
    }

    int repeated;
    for(int i = 0; i < numsSize; i++){
        if (count[nums[i]-1]++) {
            actual -= nums[i];
            repeated = nums[i];
            break;
        }
    }

    int* ans = (int*)malloc(2*sizeof(int));
    ans[0] = repeated;
    ans[1] = expected-actual;
    *returnSize = 2;

    return ans;
}