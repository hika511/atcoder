#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k;
  cin >> n >> k;
  long A[1000009] = {0};
  long prev[1000009] = {0};
  for (int i = 0; i < k; i++){
    A[i] = 1;
    prev[i] = i;
  }
  for (int i = k; i <= n; i++){
    A[i] = prev[i-1];
    prev[i] = (A[i] + prev[i-1] - A[i-k-1]) % 1000000000;
  }
  cout << A[n] << endl;
}