int eval(int a, int b, char operation) {
    switch (operation) {
        case '+':
            return a+b;
        case '-':
            return a-b;
        case '*':
            return a*b;
        case '/':
            return a/b;
        default:
            return -1;
    }
}

int evalRPN(char** tokens, int tokensSize) {
    int* stack = (int*)malloc(tokensSize*sizeof(int));
    int top = 0;

    for(int i = 0; i < tokensSize; i++) {
        char *endptr;
        int num;
        num = strtol(tokens[i], &endptr, 10);
        if (*endptr != '\0' && *endptr != '\n') {
            int b = stack[--top], a = stack[--top];
            stack[top++] = eval(a, b, tokens[i][0]);
        }else {
            stack[top++] = num;
        }
    }

    return stack[--top];
}