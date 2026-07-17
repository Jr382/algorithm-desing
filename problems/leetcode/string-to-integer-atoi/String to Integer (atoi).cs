public class Solution {
    public int MyAtoi(string s) {
        int result = 0, multiplier = 1, i = 0;
        if (s.Length == 0) return 0;
        while (s[i] == ' ' && i < s.Length-1){
            i++;
        }
        if (s[i] == '-' || s[i] == '+'){
            multiplier = s[i] == '-' ? -1 : 1;
            i++;
        }
        for (; i < s.Length && result >= 0; i++ ){
            var numeric = s[i]-'0';
            if (numeric < 0 || numeric > 9){
                break;
            }
            if (!tryShiftAndAdd(result, numeric, out result)) {
                result = multiplier == -1 ? Int32.MinValue : Int32.MaxValue;
                multiplier = 1;
                break;
            }
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