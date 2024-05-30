#include <iostream>
using namespace std;
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int testcases = 0;
    int tab[3];
    int maks;
    int max_count;

    cin >> testcases;

    for (int j = 0; j < testcases; j++)
    {
        maks = 0;
        max_count = 0;
 
        for (int i = 0; i < 3; i++)
        {
            cin >> tab[i];
        }

        for (int i = 0; i < 3; i++)
        {
            if (tab[i] > maks)
            {
                maks = tab[i];
            }
        }

        for (int i = 0; i < 3; i++)
        {
            if (tab[i] == maks)
            {
                max_count++;
            }
        }
        
        if (max_count > 1)
        {
            for (int i = 0; i < 3; i++)
            {
                if (tab[i] == maks)
                {
                    cout << 1 << ' ';
                }
                else
                {
                    cout << maks - tab[i] + 1 << ' ';
                }
            }
        }
        else
        {
            for (int i = 0; i < 3; i++)
            {
                if (tab[i] != maks)
                {
                    cout << maks - tab[i] + 1 << ' ';
                }
                else
                {
                    cout << 0 << ' ';
                }
            }
        }
        
        cout << '\n';
    }

    return 0;
}
