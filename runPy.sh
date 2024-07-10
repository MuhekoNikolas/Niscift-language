


## Compile grammar
cd "./Grammar"
#java -jar ../Jars/antlr-4.13.0-complete.jar -o ../Implementions/PyImpl/Parser/libs -Dlanguage=Python3 -visitor ./*.g4

## Now you can run the parser!
echo 'Installing dependencies' 
cd ../Implementions/PyImpl/Parser
pip3 install -r ./../../../requirements.txt
printf '\n\n'

echo 'Running niscift code'
niscift_filename='../TestCases/_testing.nis'; #Change this variable to your niscift file.

python main.py $niscift_filename