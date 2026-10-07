#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k=1;
    k%=nums.size();
reverse(nums.begin(), nums.end());
for(int i = 0; i < k; i++) {
    cout << nums[i] << " ";

}
cout<<"\n";
reverse(nums.begin(), nums.begin() + k);
for(int i = 0; i < nums.size(); i++) {
    cout << nums[i] << " ";
    
}
cout<<"\n";
reverse(nums.begin() + k, nums.end());
for(int i = 0; i < nums.size(); i++) {
    cout << nums[i] << " ";
}
return 0;
}
