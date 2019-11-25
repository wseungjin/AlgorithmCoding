#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    
    
    
    // freopen("input.txt", "r", stdin);
    
   
    int TC;
    

    

    cin >> TC;
    
    for(int i=0;i<TC;i++)
    {
        int answer;
        int x,y;
        int leng;
        double hl;
        cin >> x >> y;
        leng=y-x;

        int n=ceil(sqrt(leng));
        
        
        if(n*n-n<leng)
        {
            answer=2*n-1;
        }
        else
        {
            answer=2*n-2;
        }



        cout << answer << endl;
    }



}