#include <bits/stdc++.h>

using namespace std;
#define ll long long

void Solve()
{
	char s1[100];
	char s2[100];
	cout << "Enter Old Name\n";
	cin >> s1;
	cout << "Enter New Name\n";
	cin >> s2;

	if (!rename(s1, s2))
	{
		cout << "Done\n";
	}
	else
	{
		cout << "Error\n";
	}

}
int main()
{
	int Test = 1;
	//cin >> Test;
	while (Test--) {
		Solve();
	}
	return 0;
}