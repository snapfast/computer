#include <iostream>
using namespace std;

int mscount, mergep;

void merge(int *,int, int , int );
void mergesort(int *a, int low, int high)
{
    int mid;
    ++mscount;
    if (low < high)
    {
        mid=(low+high)/2;
        mergesort(a,low,mid);
        mergesort(a,mid+1,high);
        merge(a,low,high,mid);
    }
    return;
}
void merge(int *a, int low, int high, int mid)
{
    int i, j, k, c[50];
    i = low;
    k = low;
    j = mid + 1;
    while (i <= mid && j <= high)
    {
        if (a[i] < a[j])
        {
            c[k] = a[i];
            k++;
            i++;
        }
        else
        {
            c[k] = a[j];
            k++;
            j++;
        }
    }
    while (i <= mid)
    {
        c[k] = a[i];
        k++;
        i++;
    }
    while (j <= high)
    {
        c[k] = a[j];
        k++;
        j++;
    }
    for (i = low; i < k; i++)
    {
        a[i] = c[i];
    }
    ++mergep;

}
int main()
{
    int nokeys;
	cout << "Enter Number of Keys to be Placed in Merge Sort:- ";
	cin >> nokeys;
	int i, a[nokeys];
	cout << "Enter data in Array:- ";
	for (i = 0; i<nokeys; i++)
	{
		cin >> a[i];
	}
	cout << "\nStored Data in Array:- ";
	for (i = 0; i<nokeys; i++)
	{
		cout << a[i] << " " ;
	}

    mergesort(a, 0, nokeys-1);
    cout << "\nMergeSort calling:" << mscount;
    cout << "\nMerge Procedure ran:" << mergep;
    cout << "\nSorted:- " << " " ;
    for (int i = 0; i < nokeys; i++)
		cout << a[i] << " " ;
    cout << endl;

    return 0;

}
