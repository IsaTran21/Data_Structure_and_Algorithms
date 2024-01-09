#include <iostream>

void insert_array(int pos, int arr[], int m);

void merge(int nums1[], int m, int nums2[], int n);  

int main() {
    int nums1[] = {1, 2, 3, 0, 0, 0};
    int m = 3;
    int nums2[] = {2, 5, 6};
    int n = 3;
    merge(nums1, m, nums2, n);  

    for (int i = 0; i < m + n; i++) {
        std::cout << nums1[i] << " ";
    }
    return 0;
}

void merge(int nums1[], int m, int nums2[], int n) {
    for (int i = 0; i < n; i++) {
        insert_array(nums2[i], nums1, m);
        m++;
    }
}

void insert_array(int pos, int arr[], int m) {
    bool is_position = false;
    for (int i = 0; i < m; i++) {
        if (arr[i] > pos) {
            is_position = true;
            for (int j = m - 1; j >= i; j--) {

                    arr[j + 1] = arr[j];

            }
            arr[i] = pos;
            break;
        }
    }
    if (!is_position) {
        arr[m] = pos;
    }
}
