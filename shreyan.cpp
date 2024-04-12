#include  <iostream>
#include <string>

using namespace std;

int main() {
    int x = 0;
    cout << "How many years old are you: ";
    cin >> x;
    cout << "You are " << x << " years old\n";
    cout << "What is your name?\n";
    string name = "";
    cin >> name;
    cout << "Nah you're not " << name << ". I know who you really are. Hello Shreyan Purwar.";
    return 0;
}