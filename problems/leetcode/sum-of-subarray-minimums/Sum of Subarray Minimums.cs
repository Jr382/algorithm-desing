public class Solution {
    int modulo = 1000000007;
    public int SumSubarrayMins(int[] arr) {
        var sums = 0;
        for(var i=0; i<arr.Length; i++){
            var sum = arr[i];
            var min = arr[i];
            var counter = 1;
            for(var j = i+1; j<arr.Length; j++){
                if (min < arr[j]){
                    counter++;
                }else {
                    sums += min*counter;
                    min = arr[j];
                    counter = 1;
                }
            }
            sums = (sums+min*counter)%modulo;
        }

        return sums;
    }
}

