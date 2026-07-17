double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    const int min = -1000001;
    int total = nums1Size + nums2Size;
    if (nums1Size == 0) return (nums2[(nums2Size) / 2] + nums2[(nums2Size - 1) / 2]) / 2.0f;
    if (nums2Size == 0) return (nums1[(nums1Size) / 2] + nums1[(nums1Size - 1) / 2]) / 2.0f;

    int i = nums1Size-1, j = nums2Size-1, target = total / 2 - (total % 2 == 0 ? 1 : 0);
    while (target) {
        if (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) i--;
            else j--;
        }
        else if (i < 0) j--;
        else i--;
        target--;
    }
    
    int opt1 = i == -1 ? min : nums1[i], opt2 = j == -1 ? min : nums2[j];
    double median = opt1 > opt2 ? opt1 : opt2;

    if (total % 2 == 0) {
        if (median == opt1) i--;
        else j--;
        opt1 = i == -1 ? min : nums1[i];
        opt2 = j == -1 ? min : nums2[j];
        median += opt1 > opt2 ? opt1 : opt2;
        median /= 2;
    }

    return median;
}