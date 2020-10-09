#include <string>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    stack <int> stk;
    
    for(auto iter=moves.begin();iter!=moves.end();iter++){
        int col=*iter-1;
        int row,i;
        for(i=0;i<board.size();i++){
            if(board[i][col]!=0){
                row=i; break;
            }
        }
        if(i==board.size())
            continue;
        if(stk.empty())
            stk.push(board[row][col]);
        else{
            if(stk.top()==board[row][col]){
                stk.pop(); answer+=2;
            }
            else
                stk.push(board[row][col]);
        }
        board[row][col]=0;
        
        
    }
    return answer;
}
