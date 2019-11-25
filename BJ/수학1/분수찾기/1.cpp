#include <iostream>
#include <cmath>
#include <vector>


using namespace std;

int main()
{
    
    
    
    // freopen("input.txt", "r", stdin);
    
    
    int N;

    int answer=1;

    cin >> N;


    vector <int> nlist;
    int x;
    int y=1;

    nlist.push_back(0);
    do
    {
        if(y%2==0)
        {
            nlist.push_back(nlist[y-1]+2*y-2);
        }
        else
        {
            nlist.push_back(nlist[y-1]+1);
        }
        
        y++;
    }while(nlist[y-1]<N);

    y=y-1;
    if(nlist[y]-N>=y)
    {
        y=y-1;
    }


    if(y%2==0)
    {
        x=nlist[y]-N;
    }
    else
    {
        x=N-nlist[y];
    }
    y=y-x;
    x=x+1;

    cout << y << "/" << x <<endl;




}