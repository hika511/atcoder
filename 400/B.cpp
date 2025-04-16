#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  int errors = 0;
  bool login = false;
  cin >> n;
  string S[109];
  for (int i = 0; i < n; i++) {
    cin >> S[i];
  }
  for (int i = 0; i < n; i++) {
    if (S[i] == "login") {
      login = true;
    } else if (S[i] == "logout") {
      login = false;
    } else if (S[i] == "private") {
      if (login) {
        continue;
      } else {
        errors++;
      }
    }
  }
  cout << errors << endl;
}