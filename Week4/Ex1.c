#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// #define m 1000;

int recus[1000000];

int power(int x, int y)
{
    if (y == 0)
    {
        recus[y] = 1;
        return recus[y];
    }
    if (recus[y] != 0)
    // tra ngay ket qua neu trong mảng recus da co luu ket qua tinh trước
    {
        return recus[y];
    }
    recus[y] = power(x, y - 1) * x % 1000;
    return recus[y];
}

int hashfunction(char *string)
{
    int len = strlen(string);
    int sum = 0;

    for (int i = 0; i < len; i++)
    {
        int coe = power(7, len - 1 - i);
        sum += string[i] * coe;
    }

    return sum % 1000;
}

typedef struct Node
{
    char string[50];
    struct Node *next;
} Node;

typedef struct HashTable
{
    Node *buckets[1000]; // == m
} HashTable;

void initHashTable(HashTable *ht)
{
    for (int i = 0; i < 1000; i++)
    {
        ht->buckets[i] = NULL;
    }
};

void insert(char *string, HashTable *ht)
{
    int key = hashfunction(string);
    Node *newNode = (Node *)malloc(sizeof(Node));
    strcpy(newNode->string, string);
    newNode->next = ht->buckets[key];
    ht->buckets[key] = newNode;
}

int find(char *string, HashTable *ht)
{
    int key = hashfunction(string);
    Node *tempNode = ht->buckets[key];
    while (tempNode != NULL)
    {
        if (strcmp(tempNode->string, string) == 0)
        {
            return 1;
        }
        tempNode = tempNode->next;
    }
    return 0;
}

int main()
{
    // 1st block
    char string[50];
    HashTable ht;
    initHashTable(&ht);
    while (strcmp(string, "*") != 0)
    {
        scanf("%s", string);
        insert(string, &ht);
    }
    char choice[10];
    int step[100000];
    int i = 0;
    do
    {
        scanf("%s", choice);
        if (strcmp(choice, "insert") == 0)
        {
            char test[50];
            scanf("%s", test);
            if (find(test, &ht) == 0)
            {
                insert(test, &ht);
                step[i] = 1;
                i++;
            }
            else
            {
                step[i] = 0;
                i++;
            }
        }
        else if (strcmp(choice, "find") == 0)
        {
            char test[50];
            scanf("%s", test);
            if (find(test, &ht) == 1)
            {
                step[i] = 1;
                i++;
            }
            else
            {
                step[i] = 0;
                i++;
            }
        }
    } while (strcmp(choice,"***") != 0);

    for(int j = 0; j < i; j++)
    {
        printf("%d\n",step[j]);
    }
}
