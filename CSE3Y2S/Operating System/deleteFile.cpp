#include <bits/stdc++.h>

using namespace std;

int main()
{
	char s1[100];
	cout << "Enter a file name to remove\n";
	cin >> s1;

	if (!remove(s1))
	{
		cout << "Successfully Removed\n";
	}
	else cout << "Error Occured\n";
}