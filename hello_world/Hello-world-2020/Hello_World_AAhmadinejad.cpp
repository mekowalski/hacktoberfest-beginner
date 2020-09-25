// AUTHOR: Arian Ahmadinejad
// LANGUAGE: C++
// GITHUB: https://github.com/arian81

#include <iostream>

using namespace std;

int
main ()
{
  char hello[11] = { 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100 };
  for (int word = 0; word < 11; word++){
      cout << hello[word];
  }
}
