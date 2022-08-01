#include <iostream>
#include <string>

typedef std::string str;
class any;

template<class any> int print(any t) {
    std::cout << t << endl;
    return 0;
};

int end() {
    std::cout << std::endl;
    return 0;
};

any input(any some) {
    cout << some;
    char a;
    cin >> a;
    return a;
};

int main() {
    char aa;
    print("Hello, World!");
    aa = input("Enter a number: ");
    int a = (int)aa;
    end();
    print("You entered: "+(aa));
    if (a % 2 == 0) {
        print("The number is even");
    }
    else {
        print("The number is odd");
    }
    return 0;
};