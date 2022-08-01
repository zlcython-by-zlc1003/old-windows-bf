#include <iostream>


/*
Write a program which accepts as input a positive integer and checks, using the algorithm described below, to see
whether or not the integer is divisible by 11. This particular test for divisibility by 11 was given in 1897 by
Charles L. Dodgson (Lewis Carroll).

Algorithm:
As long as the number being tested has more than two digits, form a new number by:
deleting the units digit
subtracting the deleted digit from the shortened number
The remaining number is divisible by 11 if and only if the original number is divisible by 11.
Note:
Leading zeroes are not considered part of the number and should not be printed.
As usual, the first number in the input indicates the number of positive integers that follow. Each positive integer
 has a maximum of 50 digits. You may assume no leading zeroes exist in the positive integers.

For each positive integer in the input, the output consists of a series of numbers formed as a digit is deleted and
 subtracted, followed by a message indicating whether or not the original number is divisible by 11. Outputs for
 different positive integers are separated by blank lines.


 Sample input




1234567884
123456784
12345674
1234563
123453
12342
1232
121
11
0
True
 */




int factorial(int num) {
    if (num < 3)
        return num;
    return factorial(num - 1) * num;
}

bool func(int num) {
    //12342
    if (num == 0) return true;
    else if (num < 0) return false;
    std::cout << num << std::endl;
    return func(num / 10 - num % 10);
}


int fib(const int& num) {
    if (num < 2)
        return 1;
    return fib(num - 1) + fib(num - 2);
}


int main() {

    std::cout << func(1234567884) << std::endl;
    return 0;
}