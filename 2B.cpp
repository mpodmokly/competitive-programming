#include <bits/stdc++.h>
using namespace std;

typedef struct {
    bool zero;
    int two;
    int five;
    string path;
} cell;

int factors(int number, int factor){
    int curr = number;
    int count = 0;

    while (curr % factor == 0){
        count++;
        curr /= factor;
    }

    return count;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<vector<int>> tab(n, vector<int>(n));

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> tab[i][j];
        }
    }

    vector<vector<cell>> dp(n, vector<cell>(n, {false, 0, 0, ""}));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (tab[i][j] == 0){
                
            }
        }
    }

    return 0;
}
