#include <iostream>
#include<array>
int findNum(int x){
    int count = 0;
    while (x != 0){
        x = x / 10;
        count += 1;
    }
    return count;
}
int findOdd(int x[], int size){
    int count = 0;
   
    for (int i = 0; i < size; i++){
        
        if (findNum(x[i]) % 2  == 0){
            count ++;
        }
    }
    return count;
}

int main() {
    int arr[] = {123, 12, 333, 2, 12, 1234, 5555, 10};
    int size_x = sizeof(arr) / sizeof(arr[0]);
    std::cout << findOdd(arr, size_x);
}
