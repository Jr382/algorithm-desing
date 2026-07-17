/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int size = 2*numsSize;
    int* ans = (int*)malloc(size * sizeof(int));
    for(int i = 0; i < size; i++) {
        ans[i] = nums[i%numsSize];
    }
    *returnSize = size;

    return ans;
}