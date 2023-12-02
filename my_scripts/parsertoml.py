"""
Сканирует файл pyproject.toml, созданный poetry,
находит какие пакеты установлены в текущем проекте
и формирует файл req.txt, пригодный для установки
пакетов в pip.
"""

import re

isStartParsDepedenses = False
packages = {}

with open("pyproject.toml", "r") as file:
    for line in file:
        if "[tool.poetry.dependencies]" in line:
            isStartParsDepedenses = True
            continue
        if isStartParsDepedenses:
            if line=="\n":
                isStartParsDepedenses = False
                break

            # выделение имени пакета
            match = re.search(r"\b.+=", line)
            if match:
                print(str(match))
                start = match.start()
                end = match.end() - 2
                name_package = line[start:end]


            # выделение версии пакета
            match = re.search("\".*\"", line)
            if match:
                start = match.start() + 2
                end = match.end() - 1
                version_package = line[start:end]

            packages[name_package] = version_package

out_line=""
for package in packages:
    if package == "python":
        continue
    out_line += package + "==" + packages[package] + "\n"

print(out_line, file=open("req.txt", "w"))
