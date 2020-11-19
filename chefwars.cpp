#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int win (int, int);
int main() {
long long int t, p, h;
cin>>t;
while(t--)
{
    cin>>h>>p;
    int res = win(h, p);
    if(res == 1)
    cout<<1<<endl;
    else 
    cout<<0<<endl;
}
}
int win(int h, int p)
{
    if(h <= 0)
    {
        return 1;
    }
    else if(p <=0)
    {
        return 0;
    }
    else 
    return(win(h-p, p/2.0));
}