//https://www.hackerrank.com/challenges/insertion-sort/problem

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the insertionSort function below.
int insertionSort(vector<int> arr) {

    //copy(arr.begin(), arr.end(), ostream_iterator<int>(cout, " "));
    int result=0;
    
    for (int i = 0; i < arr.size(); i++)
    {
        // i is pointer
        //copy(arr.begin(), arr.end(), ostream_iterator<int>(cout, " "));
        //cout << "--------" << endl;
        for (int k = 0; k < i; k++)
        {
            // k looping all sorted elements
            // cout << k << "-" << i << endl;
            if (arr[i] < arr[k])
            {
                result += (i-k);
                //cout << k << "-" << i << endl;
                //cout << i-k << endl;
                
                // Using std::partial_sort 
                // std::partial_sort(arr.begin(), arr.begin() + (i+1), arr.end());
                sort(arr.begin(), arr.begin()+i+1);
                break;
            }

        }
        //cout << "---" << endl;
        
    }

    //copy(arr.begin(), arr.end(), ostream_iterator<int>(cout, " "));
    
    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        string arr_temp_temp;
        getline(cin, arr_temp_temp);

        vector<string> arr_temp = split_string(arr_temp_temp);

        vector<int> arr(n);

        for (int i = 0; i < n; i++) {
            int arr_item = stoi(arr_temp[i]);

            arr[i] = arr_item;
        }

        int result = insertionSort(arr);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
