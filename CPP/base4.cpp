// https://school.programmers.co.kr/learn/courses/18/lessons/1878

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Square
{
public:
    vector<vector<int>> map;
    int max_len;

    Square(vector<vector<int>> board)
    {
        this->map = board;
        this->max_len = board.size();
    };

    int get_size(vector<int> p_start)
    {
        int ans = 0;
        int p_value = map[p_start[0]][p_start[1]];

        if (p_value == 0)
        {
            return 0;
        }
        else
        {
            ans = 1;
        }

        for (int n = 0; n < max_len; ++n)
        {

            bool is_ok = true;
            for (int x = 0; x <= n; ++x)
            {

                for (int y = 0; y < n; ++y)
                {
                    cout << "check: "
                         << "[" << p_start[0] + x << "," << p_start[1] + y << "] : "
                         << map[p_start[0] + x][p_start[1] + y] << endl;

                    if (map[p_start[0] + x][p_start[1] + y] != 1)
                    {
                        is_ok = false;
                    }
                }
            }
            cout << is_ok << endl;
            if (is_ok && n != 0)
            {
                ans += n * 2 + 1;
            }

            if (!is_ok)
            {
                return ans;
            }
        }

        return ans;
    };

    int get_max_size(){

        int max_value = 0;
        vector<int> location(2);

        for (int i = 0 ; i < max_len ; ++ i ) {
            for (int j = 0; j < max_len ; ++ j) {
                
                cout << "location: "<< location[0] <<  "," <<location[1] << endl;
                location = {i, j} ;

                int value_temp = get_size(location);
                if (value_temp > max_value) {
                    max_value = value_temp;
                }
            }
        }

        return max_value;

    }

    void show_map()
    {
        for (int i = 0; i < map.size(); ++i)
        {
            for (int j = 0; j < map[i].size(); ++j)
            {
                cout << map[i][j];
            }
            cout << endl;
        }
    };
};

int solution(vector<vector<int>> board)
{
    int answer = 1234;

    Square sq = Square(board);
    cout << "size: " << sq.get_max_size() << endl;
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer;
}
int main()
{
    solution({{0, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {0, 0, 1, 0}});
    return 0;
}