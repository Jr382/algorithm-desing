void moveZeroes(int* nums, int numsSize) {
    int last_index = 0;
    for(int i=0; i < numsSize; i++) {
        if (nums[i] != 0) {
            int temp = nums[last_index];
            nums[last_index] = nums[i];
            nums[i] = temp;
            last_index++;
        }
    }
}