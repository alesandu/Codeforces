#include <iostream>
using namespace std;
 
int main() {
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    int n=0;
    string s;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>s;
        if(s.length()>10){
            int a = s.length()-2;
            s=s[0]+to_string(a)+s[s.length()-1];
        }
        cout<<s<<endl;
    }
 
    return 0;
}