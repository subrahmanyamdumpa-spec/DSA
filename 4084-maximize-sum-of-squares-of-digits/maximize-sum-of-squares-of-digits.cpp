class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        int s=0;string ans="";
        for(int i=0;i<num;i++){
            int r=sum-s;
            if(r>=9) {
                s+=9;
                ans+=(9+'0');
            }
            else{
                s+=r;
                ans+=(r+'0');
            }
        }
        if(s!=sum)return "";
        return ans;
    }
};