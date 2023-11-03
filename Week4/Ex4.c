#include <stdio.h>
#include <stdlib.h>

void insertionSort(int A[], int n)
{
    // index tu 1 -> n

    for (int k = 2; k <= n; k++)
    {
        int last = A[k]; // last element of final array
        int j = k;
        while (j >= 2 && A[j - 1] > last)
        {
            A[j] = A[j - 1];
            j--;
        }
        A[j] = last;
    }
}

int binarySearch(int arr[], int first, int last, int key)
{
    if (first > last)
        return -1; // key not found in arr
    int mid = (first + last) / 2;
    if (arr[mid] == key)
        return mid;
    else if (arr[mid] > key)
        return binarySearch(arr, first, mid - 1, key);
    else
        return binarySearch(arr, mid + 1, last, key);
}

int main()
{
    int A[1000001];
    int n, M;

    scanf("%d %d", &n, &M);

    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &A[i]);
    }

    insertionSort(A, n);

    // for(int i = 1; i <= n ; i++)
    // {
    //     printf("%d ",A[i]);
    // }
    // printf("\n");

    int cnt = 0;
    // Tim complement = A[j] = M - A[i] voi i tu 1 -> n-1 trong day tu i+1 -> n
    for (int i = 1; i < n ; i++)
    {
        int complement = M - A[i];
        // Tim kiem complement, neu khong thay tra ve -1
        int index = binarySearch(A, i + 1, n, complement);
        if (index != -1)
        {
            cnt++;
        }
    }
    printf("%d\n", cnt);
}
