#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    
    
    
    // freopen("input.txt", "r", stdin);
    
   
    int a,b,c;


    int answer=-1;
    long double cal;
    cin >>  a >> b >> c ;
    if(c<=b)
    {
        
    }
    else
    {
        cal=(long double)a/(long double)(c-b);
        answer=ceil(cal);
        if(cal==answer)
        {
            answer++;
        }


    }
    cout << answer << endl;


}