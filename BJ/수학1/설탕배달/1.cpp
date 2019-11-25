#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    
    
    
    // freopen("input.txt", "r", stdin);
    
   
    int N;
    int tempN;
    int x,y;
    int xnum,ynum;

    int answer=-1;
    int xcount=0;

    cin >> N;

    xnum=N/3+1;
    ynum=N/5+1;

    for(int i=ynum;i>=0;i--)
    {
        tempN=N;
        tempN=tempN-i*5;
        xcount=0;
        while(tempN>0)
        {
            tempN=tempN-3;
            xcount++;
        }
        if(tempN==0)
        {
            answer=xcount+i;
            break;
        }

    }


    cout << answer << endl;


}