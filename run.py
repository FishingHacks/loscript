import sys
import loscript as basic
import progress

try:
    file = open(repr(__file__) + "/language/lang.lsc")
except:
    exit()
lines = file.readlines()
code = ""
for line in lines:
    code += line.strip() + "\n"
result, error = basic.run("Loads funcions", code)
if error:
    print(error.as_string())

if error:
    print(error.as_string())

file = open(sys.argv[1])
lines = file.readlines()
code = ""
for line in lines:
    code += line.strip() + "\n"
result, error = basic.run(sys.argv[1], code)
if error:
    print(error.as_string())
progress.createprogress(50, .02, 'Stopping', 'Stopped!')
