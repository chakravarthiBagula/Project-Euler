/* """ Project Euler #14: Longest Collatz sequence """ */

#include <iostream>
#include <stdio.h>
typedef unsigned long long int ulli;
ulli *arr = new ulli[5000001];
ulli Collatz(ulli n)
{
    if (arr[n] != 0)
    {
        return arr[n];
    }
    ulli temp = 0;
    if (n % 2 == 0)
    {
        arr[n] = 1 + Collatz(n / 2);
        return arr[n];
    }
    temp = 3 * n + 1;
    ulli cnt = 01;
    while (temp > 5000001)
    {
        if (temp % 2 == 0)
            temp /= 2;
        else
            temp = 3 * temp + 1;
        cnt++;
    }
    arr[n] = cnt + Collatz(temp);
    return arr[n];
}
int main()
{
    ulli count = 0;
    arr[1] = 1;
    for (int a = 2; a < 5000001; a *= 2)
    {
        arr[a] = ++count;
    }
    for (int i = 1; i < 5000001; i++)
    {
        Collatz(i);
    }
    ulli *results = new ulli[5000001];
    results[1] = 1;
    for (int a = 2; a < 5000001; a++)
    {
        if (arr[a] >= arr[results[a - 1]])
        {
            results[a] = a;
        }
        else
            results[a] = results[a - 1];
    }
    int testCases, n;
    std::cin >> testCases;
    while (testCases--)
    {
        std::cin >> n;
        std::cout << results[n] << std::endl;
    }

    return 0;
}
