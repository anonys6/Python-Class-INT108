#include <iostream>

using namespace std;

int main()
{
    int keepCoding();
    int tired();
    int drinkCoffee();

    while (true) {
        if (!tired()) {
            keepCoding();
        } else {
            drinkCoffee();
        }
    }

}

