#include <string>
#include <vector>
#include<algorithm>

using namespace std;
bool showIter[201]={false,};
vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    int len=numbers.size();
    
    for(int i=0;i<len;i++){
        for(int j=i+1;j<len; j++){
            int sum=numbers[i]+numbers[j];
            if(showIter[sum]==false){
                answer.push_back(sum);
                showIter[sum]=true;
            }
        }
    }
    
    sort(answer.begin(),answer.end());
    return answer;
}
