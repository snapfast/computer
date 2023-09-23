/*
author: rahul bali

compile: g++ -std=c++11 -pthread MergeSortThread.cpp -o mergesortthread

*/


#include <iostream>
#include <thread>
#include <vector>

using namespace std;

void merge(vector<int>& vec, int start, int mid, int end)
{
	vector<int> one(vec.begin() + start, vec.begin() + mid + 1);
	vector<int> two(vec.begin() + mid + 1, vec.begin() + end+1);

	int a = 0;
	int b = 0;
	int index = start;
	while (a < one.size() && b < two.size())
	{
		if (one[a] < two[b])
			vec[index++] = one[a++];
		else
			vec[index++] = two[b++];
	}

	// merge the left-over elements
	while (a < one.size())
		vec[index++] = one[a++];
	while (b < two.size())
		vec[index++] = two[b++];
	
}

void merge_sort(vector<int>& vec, int start, int end)
{
	if (start >= end)
		return;

	int mid = start + (end - start) / 2;

	// multi-thread version
	thread first(merge_sort, std::ref(vec), start, mid);
	cout << std::ref(vec[start, mid]) << "_" << start <<"-" <<mid <<"\n";
	thread second(merge_sort, std::ref(vec), mid + 1, end);
	cout << std::ref(vec[mid+1, end]) << "_" << mid+1 << "-" << end<< "----mergesort ran \n";
	first.join();
	second.join();

	/*
	// single-thread version, testified.
	merge_sort(vec, start, mid);
	merge_sort(vec, mid + 1, end);
	*/

	merge(vec, start, mid, end);
}


int main()
{
	int nokeys;
	cout << "Enter Number of Keys to be Placed in Merge Sort:- ";
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
	}


	vector<int> vec(a, a + nokeys);
	cout << "Original Vector:"<< "\n";
	for (int i = 0; i < nokeys; i++)
		cout << vec[i] << endl;
	merge_sort(vec, 0, nokeys-1);
	for (int i = 0; i < nokeys; i++)
		cout << vec[i] << endl;
	
	return 0;

}