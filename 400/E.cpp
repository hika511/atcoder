#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  int u[200009];
  int v[200009];
  vector<int> G[200009];
  int ans[200009];
  for (int i = 1; i <= n; i++) {
    cin >> u[i] >> v[i];
    G[u[i]].push_back(v[i]);
    G[v[i]].push_back(u[i]);
  }
    set<int> reachable;
    reachable.insert(1);
    ans[1] = 0;
    cout << ans[1] << endl;

    for (int k = 2; k <= n; k++) {
      for (int i = 1, i <= k; i++) {
        if (G[k][i] <= k - 1) {
          reachable.insert(G[k][i]);
        } else {
          break;
        }
      }
      if (reachable.size() == k){
        ans[k] = G[1].size() - k;
      } else {
        ans[k] = -1;
      }
      cout << ans[k] << endl;
  }
}