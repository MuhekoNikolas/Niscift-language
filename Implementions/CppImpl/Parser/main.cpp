

#include <iostream>
#include <cstdio>
#include <fstream>

#include "functions.h"

using namespace std;

int main(int argc, char* argv[]) {

    for (int i = 1; i < argc; i++) {
        string content = _readFile(argv[i]);
        cout << content;
    }

    return 0;
}