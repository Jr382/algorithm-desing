/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** buildArray(int* target, int targetSize, int n, int* returnSize) {
    char** ans = (char**)malloc(2*n*sizeof(char*));
    
    int i = 0, current = 1;
    for (int j = 0; j < targetSize; j++) {
        for(; current < target[j]; current++) {
            ans[i++] = "Push";
            ans[i++] = "Pop";
        }
        ans[i++] = "Push";
        current++;
    }

    ans = (char**)realloc(ans, i*sizeof(char*));
    *returnSize = i;

    return ans;
}