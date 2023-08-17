#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

bool solution(vector<int> arr)
{
    bool answer = true;

    vector<bool> v_check(arr.size(), false);
    for (int iter : arr)
    {

        
        if (v_check[iter] == false)
        {
            v_check[iter] = true;
        }
        else
        {
            answer = false;
            break;
        }
        cout << v_check[iter] << endl;
        // for (auto iter : v_check) {
        //     cout << iter << endl;
        // }

        // if (count(v_check.begin(), v_check.end(), false))
        // {
        //     answer = false;
        // }
    }

    return answer;
}
int main()
{
    cout << solution({1, 2, 3, 4}) << endl;
    cout << solution({1, 2, 4}) << endl;
    cout << solution({1, 2, 4, 5}) << endl;
    cout << solution({1, 2, 3,4 ,5}) << endl;
    return 0;
}