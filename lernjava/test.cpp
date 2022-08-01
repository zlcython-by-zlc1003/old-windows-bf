#include <iostream>
u
int main() {
    int f,e;
    std::cin >> f;
    std::cin >> e;
    int $$$=0;
    int t=0;
    for (int i=f;i<=e;i++){
        if (i%2==1){
            std::cout << i << std::endl;
            $$$+=i;
            t++;
        }
    }
    std::cout << "average:" << $$$/t << std::endl;
    return 0;
}