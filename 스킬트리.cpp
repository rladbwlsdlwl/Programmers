#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    for(int i=0; i<skill_trees.size(); i++){
        int k=0; bool check=true;
        for(int j=0; j<skill_trees[i].size(); j++){
            if(!check) break;
            if(skill_trees[i][j]==skill[k]) k++;
            else{
                for(int p=k; p<skill.size(); p++){
                    if(skill_trees[i][j]==skill[p]){
                        check=false; break;
                    }
                }
            }
        }
        if(check) answer++;
    }
    
    return answer;
}
