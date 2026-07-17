/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* finalPrices(int* prices, int pricesSize, int* returnSize) {
    int *ans = (int*)malloc(pricesSize * sizeof(int));

    for(int i = 0; i < pricesSize; i++){
        int paidPrice = prices[i];
        for(int j = i+1; j < pricesSize; j++){
            if(prices[j] <= paidPrice) {
                paidPrice -= prices[j];
                break;
            }
        }
        ans[i] = paidPrice; 
    }

    *returnSize = pricesSize;
    return ans;
}