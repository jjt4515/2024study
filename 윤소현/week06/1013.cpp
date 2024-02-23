#include <iostream>
#include <regex>
#include <string>
using namespace std;

bool matching(const string& number) 
{
    regex e("(100+1+|01)+");
    return regex_match(number, e);
}

int main()
{
    string input;
    int count;
    cin >> count;

    for(int i = 0; i < count; i++){
        cin >> input;
        if (matching(input))
            cout << "YES\n";

        else
            cout << "NO\n";
    }

    return 0;
}
