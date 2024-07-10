

#include <iostream>
#include <cstdio>
#include <fstream>
#include <format>
#include <string>

#pragma once

using namespace std;

template <typename T>
T _readFile(const T& filename){
    ifstream fileInput;

    fileInput.open(filename); 

    printf("\nReading file %s\n", filename);

    if (!fileInput) {
        cerr << "Error: Unable to open the file." << endl;
        return "none";
    }

    string content;
    string line;

    while (std::getline(fileInput, line)) {
        content += "\n" + line;
    }

    fileInput.close();

    return content;
}