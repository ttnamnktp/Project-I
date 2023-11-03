#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int recus[100000];
int n, m;

int power(int x, int y)
{
    if (y == 0)
    {
        recus[y] = 1;
        return recus[y];
    }
    if (recus[y] != 0)
    //tra ngay ket qua neu trong mảng recus da co luu ket qua tinh trước
    {
        return recus[y];
    }
    recus[y] = power(x,y-1) * x % m;
    return recus[y];
}

int hashfunction(char *string)
{
    int len = strlen(string);
    int sum = 0;

    for (int i = 0; i < len; i++)
    {
        int coe = power(256, len - 1 - i);
        // printf("%lld\n", coe);
        sum += string[i] * coe;
        // printf("%lld", sum);
    }

    return sum % m;
}

int main()
{
    scanf("%d %d", &n, &m);

    char array[200];
    int hasharray[100000];
    for (int i = 0; i < n; i++)
    {
        scanf("%s", array);
        hasharray[i] = hashfunction(array);
    }

    for (int i = 0; i < n; i++)
    {
        printf("%d\n", hasharray[i]);
    }
}