#include <bits/stdc++.h>
using namespace std;

int main()
{

	string fileName;
	cout << "Enter a fileName to copy\n";
	cin >> fileName;
	cout << "Enter a destination\n";
	string des;
	cin >> des;

	des += "/";
	des += fileName;


	ifstream in(fileName);
	ofstream out(des);

	string s;

	while (getline(in, s))
	{
		out << s << "\n";
	}

	return 0;
}