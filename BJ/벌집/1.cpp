#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    
    
    
    // freopen("input.txt", "r", stdin);
    
   
    int N;
    int tempN;
    

    int answer=1;

    cin >> N;
    int count=1;

    tempN=N-1;
    while(tempN>0)
    {
        tempN=tempN-6*count;
        count++;
    }
    answer=count;

    cout << answer << endl;


}