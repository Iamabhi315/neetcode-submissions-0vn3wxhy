class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int size=flowerbed.size();
        int check=0;
        for(int i=0;i<size;i++){
            if(check==0 && flowerbed[i]==0){
                n--;
                check=1;
            }
            else if(check==1 && flowerbed[i]==1){
                n++;
                check=flowerbed[i];
            }
            else{
                check=flowerbed[i];
            }
        }
        if(n<=0) return true;
        return false;
    }
};