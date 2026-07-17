/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize*sizeof(int));
    *returnSize = numsSize;

    for(int i=0; i < numsSize; i++){
        ans[nums[i]-1] = 1;
    }

    int j = 0;
    for(int i=0; i < numsSize; i++){
        if (ans[i] != 1) {
            ans[j] = i+1;
            j++;
        }
    }

    *returnSize = j;
    return ans;
}