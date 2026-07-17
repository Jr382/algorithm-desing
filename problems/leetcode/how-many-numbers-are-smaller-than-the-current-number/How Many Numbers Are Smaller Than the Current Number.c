/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int MAX_INT = 101;

int compare_integers(const void *a, const void *b) {
    // Cast the void pointers to integer pointers and dereference them
    int int_a = *((int *)a);
    int int_b = *((int *)b);
    return int_a - int_b;
}

int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize) {
    int sorted[numsSize]; 
    memcpy(sorted, nums, numsSize * sizeof(int));
    qsort(&sorted, numsSize, sizeof(int), compare_integers);
    int* ans = (int*)malloc(numsSize * sizeof(int));

    int greaterThan[MAX_INT];
    greaterThan[sorted[0]] = 0;
    for(int i = 1; i < numsSize; i++){
        if (sorted[i] == sorted[i-1]){
            continue;
        }
        greaterThan[sorted[i]] = i;
    }

    for(int i = 0; i < numsSize; i++){
        ans[i] = greaterThan[nums[i]];
    }
    *returnSize = numsSize;
    
    return ans;
}
