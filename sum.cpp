#include <iostream>
using namespace std;

int main ()
{
    int b = 0;
    int sum = 0;

    cout<<"You want average of how many numbers: ";
    cin>>b;

    int a [b];

    for (int i = 0; i < b; i++)
    {
        cout<<"Enter values: ";
        cin>>a[b];

        sum = sum + a[i];
        
    }
    cout<<"sum "<<sum<<endl;
    
}
