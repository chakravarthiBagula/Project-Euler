/* Project Euler #12: Highly divisible triangular number */
#include <bits/stdc++.h>
using namespace std;
int factors(int n)
{
    if (n == 1)
        return 1;
    int count = 0;
    int sq = (int)sqrt(n);
    for (int i = 1; i <= sq; i++)
    {
        if (n % i == 0)
            count += 2;
    }
    if (sq * sq == n)
        count--;
    return count;
}
int main()
{
    int sumup[1001];
    for (int i = 1; i <= 1000; i++)
        sumup[i] = 0;
    int a[] = {1, 2, 3, 7, 8, 15, 24, 32, 35, 63, 80, 104, 224, 384, 560, 935, 1224, 1664, 1728, 2015, 2079, 5984, 12375, 14399, 21735, 41040};
    for (auto x : a)
    {
        int y = ((x) * (x + 1)) / 2;
        int temp = factors(y);
        if (temp > 1000)
            temp = 1001;
        while (!(sumup[temp]))
        {
            sumup[temp--] = y;
        }
    }
    int testCases, n;
    cin >> testCases;
    while (testCases-- > 0)
    {
        cin >> n;
        //if (n == 1)
        //            std::cout << 1 << "\n";
        //        else if (n == 2)
        //            std::cout << 3 << "\n";



        //        else
        cout << sumup[n + 1] << "\n";
    }
    return 0;
}
