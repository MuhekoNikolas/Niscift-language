

## Compile grammar
cd "./Grammar"
#java -jar ../Jars/antlr-4.13.0-complete.jar -o ../Implementions/CppImpl/Parser/libs -Dlanguage=Cpp -visitor ./*.g4

## Now you can run the parser!
cd ../Implementions/CppImpl/Parser

#rm -rf cppMainExe
g++ -std=c++20 -o ./cppMainExe main.cpp

./cppMainExe ../../PyImpl/TestCases/_all.py