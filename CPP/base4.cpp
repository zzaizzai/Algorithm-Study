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
        } else {
            ans = 1;
        }

        // for (int n = 0 ; n < 3 ; ++n) {
        //     for (int x = 0 ;  x <= n ; ++ x ) {

        //     }

        // }

        return 0;
    };

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
    sq.show_map();
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer;
}
int main()
{
    solution({{0, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {0, 0, 1, 0}});
    return 0;
}