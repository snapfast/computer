
// C++ program for B-Tree insertion
#include<iostream>
using namespace std;
// Driver program to test above functions
int main()
{
	int nokeys;
	cout << "Enter Number of Keys to be Placed in Insertion Sort:- ";
	cin >> nokeys;
	int i, a[30];
	cout << "Enter data in Array:- ";
	for (i = 0; i<nokeys; i++)
	{
		cin >> a[i];
	}
	cout << "\n\nStored Data in Array:- ";
	for (i = 0; i<nokeys; i++)
	{
		cout << a[i];
		cout << "  ";
	}

	int j,key,k, comparison=0, compare=0;
	for (j = 1; j < nokeys; j++)
	{
		key = a[j];
		k = j - 1;
		while (k >= 0 && key < a[k])
		{
			a[k + 1] = a[k];
			k = k - 1;
			comparison++;
		}
		if(key >= a[k]){
            compare++;
		}
		a[k + 1] = key;
	}

	for (j = 0; j < nokeys; j++)
	{
		cout << "\n\n";
		cout << a[j];
		cout << "   ";

	}
	cout <<"Compare"<<compare<<endl;
	cout <<"Comparison"<< comparison<<endl;
	cout<< "Number of comparisons  " << compare+comparison;

	return 0;

}

