#include <iostream>
// #include <conio.h>  // remove this line when compiling with g++  or  C++ compiler
using namespace std;

int main()
{
    char name[30],ch;
    int i=0,n;
    cout<< "enter name ";
    //cin >> name;


    while(ch!='\n')
	{
		ch=getwchar();
		name[i]=ch;
		i++;
	}
	n=i-1;   //      n = name.length();
	name[i]='\0';
	int j,key,k, comparison=0, compare=0;
	for (j = 1; j < n; j++)
	{
		key = name[j];
		k = j - 1;
		while (k >= 0 && key < name[k])
		{
			name[k + 1] = name[k];
			k = k - 1;
			comparison++;
		}
		if(key >= name[k])
        compare++;
		name[k + 1] = key;
	}

	for (j = 0; j < n; j++)
	{
		//cout << "\t";
		cout<<name[j];
		cout<<"   ";

	}
	cout<<"\nCompare:-"<<compare<<endl;
	cout<<"Comparison:-"<<comparison<<endl;
	cout<<"Number of comparisons:-" <<compare+comparison<<endl;

    return 0;
}
