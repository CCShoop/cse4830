#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>

// Compile with -lm to link the math library for pow()

void call_func(int func);
void func0(int num);
void func1(int num);
void func2(int num);
void func3(int num);
void func4(int num);
void func5(int num);
void func6(int num);
void func7(int num);
void retrieve_flag(int func);
void failed(int func);

int main(void) {
    srand(time(NULL));
    int func = -1, check, done = 0;
    int used[8];
    for (int ii = 0; ii < 8; ii++) {
        used[ii] = -1;
    }
    do {
        do {
            check = 0;
            func = rand() % 8;
            for (int ii = 0; ii < 8; ii++) {
                if (used[ii] == -1)
                    break;
                if (func == used[ii]) {
                    check = 1;
                    break;
                }
            }
            if (used[7] != -1)
                done = 1;
            if (check == 0 && done == 0)
                for (int ii = 0; ii < 8; ii++)
                    if (used[ii] == -1) {
                        used[ii] = func;
                        break;
                    }
        } while (check == 1 && done == 0);
        if (done == 0)
            call_func(func); 
    } while (done == 0);
    return 0;
}

void call_func(int func) {
    switch (func) {
        case 0:
            func3(5);
            break;
        case 1:
            func6(3);
            break;
        case 2:
            func1(0);
            break;
        case 3:
            func4(6);
            break;
        case 4:
            func7(2);
            break;
        case 5:
            func0(7);
            break;
        case 6:
            func5(1);
            break;
        case 7:
            func2(4);
            break;
    }
}

void func0(int num) {
    printf(">>> Unlock Phase 0: ");
    int input;
    scanf("%d", &input);
    int ans = input % num;
    switch (ans) {
        case 0:
            retrieve_flag(0);
            break;
        default:
            failed(0);
            break;
    }
}

void func1(int num) {
    printf(">>> Unlock Phase 1: ");
    int ans = ((num + 74) * 47362) * 2 - 9385, input;
    scanf("%d", &input);
    if (input == ans)
        retrieve_flag(1);
    else
        failed(1);
}

void func2(int num) {
    printf(">>> Unlock Phase 2: ");
    int ans = num * 29348 - 4, input;
    scanf("%d", &input);
    if (input == ans / 29347)
        retrieve_flag(2);
    else
        failed(2);
}

void func3(int num) {
    printf(">>> Unlock Phase 3: ");
    num += num;
    int ans = num;
    int input;
    scanf("%d", &input);
    if (input == ans)
        retrieve_flag(3);
    else
        failed(3);
}

void func4(int num) {
    printf(">>> Unlock Phase 4: ");
    int ans = num * 4830, input;
    ans /= 2;
    scanf("%d", &input);
    if (input * 2 == ans)
        retrieve_flag(4);
    else
        failed(4);
}

void func5(int num) {
    printf(">>> Unlock Phase 5: ");
    int num0 = (num * 4830 - num) / 4829;
    int num1 = num0 / 1 * 4830 - 4829;
    int num2 = num1 + 4830 - num1 - 4829;
    int ans = num2 * 1;
    int input;
    scanf("%d", &input);
    if (input == ans)
        retrieve_flag(5);
    else
        failed(5);
}

void func6(int num) {
    printf(">>> Unlock Phase 6: ");
    int ans = num * 100000 - 72264, input;
    ans = ceil(ans / 1080);
    scanf("%d", &input);
    if (input == ans)
        retrieve_flag(6);
    else
        failed(6);
}

void func7(int num) {
    printf(">>> Unlock Phase 7: ");
    int ans, input;
    ans = pow(num, 11) - pow(2, 5);
    scanf("%d", &input);
    if (input == ans)
        retrieve_flag(7);
    else
        failed(7);
}

void retrieve_flag(int func) {
    char file[10] = "flag", flags[10], txt[] = ".txt", flag[15];
    sprintf(flags, "%d", func);
    strcat(file, flags);
    strcat(file, txt);
    FILE *flagfile = fopen(file, "r");
    fgets(flag, 15, flagfile);
    fclose(flagfile);
    printf("Phase %d section of flag: %s\n", func, flag);
}

void failed(int func) {
    printf("You failed to unlock Phase %d.\n", func);
    exit(0);
}

/*
Answers:
Phase 0: 7
Phase 1: 7000191
Phase 2: 4
Phase 3: 10
Phase 4: 7245
Phase 5: 1
Phase 6: 210
Phase 7: 2016
*/