int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int max = 0, count = 0;
    for(int i=0; i < numsSize; i++) {
        if (nums[i] != 1) {
            if (max < count) max = count;
            count = 0;
        }else count++;
    }
    if (max < count) max = count;

    return max;
}