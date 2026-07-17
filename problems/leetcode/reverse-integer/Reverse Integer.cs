public class Solution {
    public int Reverse(int x) {
        int result = 0, multiplier = 1;
        if (x < 0) {
            multiplier = -1;
            x *= -1;
        }
        while (x != 0){
            if (!tryShiftAndAdd(result, x%10, out result)){
                return 0;
            }
            x /= 10;
        }
        return result * multiplier;
    }

    private bool tryShiftAndAdd(int a, int b, out int result){
        result = 0;
        if (a > Int32.MaxValue / 10) return false;
        a *= 10;
        if (b > Int32.MaxValue - a) return false;
        result = a+b;
        return true;
    }
}