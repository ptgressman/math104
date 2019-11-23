import re
import os

def check_weird(srctxt):
    pattern = re.compile(r"\\choice{.*?\n")
    foundthings = {}
    shouldbe = False
    for thing in re.finditer(pattern,srctxt):
        if thing.group(0) in foundthings:
            foundthings[thing.group(0)] += 1
        else:
            foundthings[thing.group(0)] = 1
    for item in foundthings:
        weirdones = foundthings[item]
        if (weirdones >= 4):
            print [weirdones,item]
            shouldbe = True
    return shouldbe

def cleansourcefile(srctxt):
    returntxt = srctxt

    returntxt = re.sub(r"\\begin{question} *(\[.*\])",r"\\begin{question}%%%%%\1",returntxt)
    returntxt = re.sub(r"\\choicebreak","",returntxt)
    envstohide = ['type','keywords','notes']

    for envname in envstohide:
        pattxt = r"\\begin{" + envname + r"}[^\\]*\\end{" + envname + "}"
        returntxt = re.sub(pattxt,"",returntxt)

    pattern = re.compile(r"\\bigmath")
    allbigmaths = []
    for found in re.finditer(pattern,returntxt):
        depth = 0
        started = 0
        startindex = 0
        ended = 0
        for index in range(found.end(0),len(returntxt)):
            if returntxt[index] == '\\':
                index += 1
                item = ""
            else:
                item = returntxt[index]
            if item == '{':
                depth += 1
                if started == 0:
                    startindex = index+1
                started = 1
            elif item == '}':
                depth -= 1
            if (depth == 0) and (started == 1):
                foundinstance = returntxt[found.start(0):index+1]
                replaceinstance = returntxt[startindex:index]
                replaceinstance = r"\(\displaystyle " + replaceinstance + r"\)"
                allbigmaths.append([re.escape(foundinstance),replaceinstance])
                break

    for pairs in allbigmaths:
        returntxt = re.sub(pairs[0],lambda x : pairs[1],returntxt)

    returntxt = re.sub(r"\\href{(.*?)}{(.*?)}",r"\\link[\2]{\1}",returntxt)
    returntxt = re.sub(r"(?<!%)\\author{(.*?)}",r"%%%%%\\author{\1}",returntxt)

    return returntxt

for (root,dirs,files) in os.walk('.'):
    for filename in files:
        if (filename.endswith('.tex')) and (filename != 'preamble.tex'):
            fullname = os.path.join(root,filename)
            text = open(fullname,"r").read()
            out = cleansourcefile(text)
            if (check_weird(text)):
                print "Something weird in " + filename
            if text != out:
                open(fullname,"w").write(out)
