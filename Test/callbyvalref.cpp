//Actual vs formal Argument

#include <iostream>
using namespace std;

//call by ref
void swappointer(int* x, int* y) //Parameters as address in address variables
{
    int temp = *x; // * for value at operator
    *x = *y;
    *y = temp;
}

int main(){

    int a = 10;
    int b = 123;

    cout<<"The value of a is "<<a<<" and value of b is "<<b<<endl;
    swappointer(&a,&b);
    cout<<"The value of a is "<<a<<" and value of b is "<<b<<endl;
    
    return 0;
}