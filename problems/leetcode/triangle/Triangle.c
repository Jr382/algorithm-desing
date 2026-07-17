void reduce(int* row, int* to_add, int rowSize); 

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize) {
    int last_row[triangleSize];
    memcpy(last_row, triangle[triangleSize-1], triangleSize * sizeof(int));
    for(int i = triangleSize - 1; i > 0; i--){
        reduce(last_row, triangle[i-1], i);
    }

    return last_row[0];
}

void reduce(int* row, int* to_add, int length) {
    for(int i = 0; i < length; i++) {
        row[i] = row[i] < row[i+1] ? row[i] : row[i+1];
        row[i] += to_add[i];
    }
}