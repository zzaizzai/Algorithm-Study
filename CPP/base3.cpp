// https://school.programmers.co.kr/learn/courses/18/lessons/1878

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<vector<int>> v)
{
    vector<int> ans;

    vector<int> x(2);
    vector<int> y(2);

    // get x...
    vector<int> v_x;
    for (int i = 0; i < 3; ++i)
    {

        v_x.push_back(v[i][0]);
    };
    x[1] = *max_element(v_x.begin(), v_x.end());
    x[0] = *min_element(v_x.begin(), v_x.end());

    // get y...
    vector<int> v_y;
    for (int i = 0; i < 3; ++i)
    {

        v_y.push_back(v[i][1]);
    };
    y[1] = *max_element(v_y.begin(), v_y.end());
    y[0] = *min_element(v_y.begin(), v_y.end());

    // cout << "x max: " << x[1] << endl;
    // cout << "x min: " << x[0] << endl;
    // cout << "y max: " << y[1] << endl;
    // cout << "y min: " << y[0] << endl;

    vector<int> x_point = {0, 0, 1, 1};
    vector<int> y_point = {0, 1, 0, 1};

    for (int i = 0; i < 4; ++i)
    {
        vector<int> v_temp = {x[x_point[i]], y[y_point[i]]};

        bool include = find(v.begin(), v.end(), v_temp) != v.end();
        // cout << include << endl;
        if (!include) {
            ans = v_temp;
        }
    }

    return ans;
}

int main()
{
    vector<vector<int>> vv = {{1, 4}, {3, 4}, {3, 10}};
    cout << solution(vv)[0] << " , " << solution(vv)[1]   << endl;
    return 0;
}