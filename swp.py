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

file = open(sys.argv[1])
lines = file.readlines()
code = ""
for line in lines:
    code += line.strip() + "\n"
result, error = basic.run(sys.argv[1], code)
if error:
    print(error.as_string())
while True:
    text = input('loscript > ')
    if text == "--stop":
        progress.createprogress(50, .02, 'Stopping', 'Stopped!')
        break
    if text.strip() == "":
        continue
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
