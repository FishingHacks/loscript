from msilib.schema import Error
import os
import loscript as basic
import sys
import tools
import progress

try:
    file = open("language/lang.lsc")
except:
    exit()
lines = file.readlines()
code = ""
for line in lines:
    code += line.strip() + "\n"
result, error = basic.run("Loads functions", code)
if error:
    print(error.as_string())

quit = False
while True:
    text = input('lolscript > ')
    if ((text == "--stop") | (text == "stop") | (text == "exit")):
        progress.createprogress(50, .02, 'Stopping', 'Stopped!')
        break
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    if result:
        if len(result.elements) == 1:
            print(tools.colors.parse(str(result.elements[0])))
        else:
            print(tools.colors.parse(str(result)))
