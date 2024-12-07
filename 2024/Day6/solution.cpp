#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define fst first
#define snd second
#define sz(x) ((int)x.size())
#define all(x) x.begin(), x.end()
#define dbg(x) cerr << #x << ": " << (x) << endl
#define vb vector<bool>
using str = string;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = 130;
    vector<str> g(n);
    for (int i = 0; i < n; i++) {
        cin >> g[i];
    }

    vector<int> start(3);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (g[i][j] == '^') {
                start = {i, j, 0};
            } else if (g[i][j] == '>') {
                start = {i, j, 1};
            } else if (g[i][j] == 'v') {
                start = {i, j, 2};
            } else if (g[i][j] == '<') {
                start = {i, j, 3};
            }
        }
    }

    vector<pair<int, int>> moves = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    vector<vb> vis(n, vb(n));

    auto valid = [&](int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    };

    auto traverse = [&](vector<int> s) {
        auto curr = s;
        vis[curr[0]][curr[1]] = true;
        while (true) {
            int dir = curr[2];
            int new_r = curr[0] + moves[dir].fst;
            int new_c = curr[1] + moves[dir].snd;

            if (!valid(new_r, new_c)) {
                break;
            }

            if (g[new_r][new_c] == '#') {
                curr[2] = (curr[2] + 1) % 4;
            } else {
                vis[new_r][new_c] = true;
                curr[0] = new_r;
                curr[1] = new_c;
            }
        }
    };

    // Part 1
    int ans1 = 0;
    traverse(start);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (vis[i][j]) {
                ans1++;
                break;
            }
        }
    }

    // Part 2
    auto find_cycle = [&](vector<int> s) {
        auto curr = s;
        vector<vector<vb>> vis2(n, vector<vb>(n, vb(4)));
        vis2[curr[0]][curr[1]][curr[2]] = true;
        while (true) {
            int dir = curr[2];
            int new_r = curr[0] + moves[dir].fst;
            int new_c = curr[1] + moves[dir].snd;

            if (!valid(new_r, new_c)) {
                break;
            }

            if (vis2[new_r][new_c][dir]) {
                return true;
            } else if (g[new_r][new_c] == '#') {
                curr[2] = (curr[2] + 1) % 4;
            } else {
                vis2[new_r][new_c][dir] = true;
                curr[0] = new_r;
                curr[1] = new_c;
            }
        }

        return false;
    };

    int ans2 = 0;
    vis[start[0]][start[1]] = false;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (vis[i][j]) {
                g[i][j] = '#';
                ans2 += find_cycle(start);
                g[i][j] = '.';
            }
        }
    }

    cout << "Part 1: " << ans1 << "\n";
    cout << "Part 2: " << ans2 << "\n";

    return 0;
}
