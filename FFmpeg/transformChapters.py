import re
from sys import argv


if __name__ == '__main__':
    if len(argv) >= 2:
        if ".txt" in argv[1]:
            itemList = []
            with open(argv[1], "r") as fl:
                for linea in fl.readlines():
                    chapterTitle = re.match(r"([a-zA-Z].+)", linea.strip())
                    time = re.search(r"\d+:\d+:\d+",linea.strip())
                    title = re.search(r'[a-zA-Z].+', linea.strip())
                    if chapterTitle != None:
                        dictChapter = {chapterTitle.group(0): []}
                        itemList.append(dictChapter)
                    if time != None and title != None:
                        try:
                            itemDictChapter = list(itemList[-1].items())
                            itemDictChapter[0][1].append([time.group(0), title.group(0).title()])
                        except:
                            itemList.append([time.group(0), title.group(0).title()])
            s = ""
            i = 0
            if type(itemList[0]) == dict:
                for item in itemList:
                    titleChapter = list(item.keys())[0]
                    listChapter = list(item.values())[0]
                    for innerItem  in range(len(listChapter)):
                        try:
                            title = listChapter[innerItem][1]
                            start = listChapter[innerItem][0].split(":")
                            end = listChapter[innerItem + 1][0].split(":")
                            try:
                                miliStart = (int(start[0]) * 3600 +  int(start[1]) * 60 + int(start[2])) * 1000
                                miliEnd = ((int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])) * 1000) - 1
                            except ValueError:
                                miliEnd = ""
                            string = f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={miliStart}\nEND={miliEnd}\ntitle={title.title()}\n\n"
                            s += string
                        except IndexError:
                            stringEx = f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={miliEnd + 1}\ntitle={title.title()}\n\n"
                            s += stringEx
                    i += 1
                    ff = f';FFMETADATA{i}\ntitle={titleChapter}\n\n'
                    with open("metadataFile.txt", "a") as file:
                            file.write(ff + s + f'[STREAM]\ntitle={titleChapter}\n\n\n')
            else:
                if argv[2:] != []:
                    titleFFmetaData = argv[2]
                    try:
                        nFFmetadata = argv[3]
                    except IndexError:
                        nFFmetadata = 1
                else:
                    nFFmetadata = 1
                    titleFFmetaData = "Chapters"

                for item in range(len(itemList)):
                    try:
                        start = itemList[item][0].split(":")
                        end = itemList[item + 1][0].split(":")
                        try:
                            miliStart = (int(start[0]) * 3600 +  int(start[1]) * 60 + int(start[2])) * 1000
                            miliEnd = ((int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])) * 1000) - 1
                        except ValueError:
                            miliEnd = ""
                        string = f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={miliStart}\nEND={miliEnd}\ntitle={itemList[item][1].title()}\n\n"
                        s += string
                    except IndexError:
                            stringEx = f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={miliEnd + 1}\ntitle={itemList[item][1].title()}\n\n"
                            s += stringEx

                ff = f';FFMETADATA{nFFmetadata}\ntitle={titleFFmetaData}\n\n'
                with open("metadataFile.txt", "a") as file:
                    file.write(ff + s + f'[STREAM]\ntitle={titleFFmetaData}\n\n\n')

        elif "help" in argv[1].lower():
            print(f"\nUsage of {argv[0]}, --help:")
            print(f"\n\t#  {argv[0]} file_Chapter.txt TitleChapters idFFmetadata\n")
            print(f"- TitleChapters   is optional")
            print(f"- idFFmetadata   is optional, integer > 1\n\n")
    else:
        print(f"\nUsage of {argv[0]}, --help:")
        print(f"\n\t#  {argv[0]} file_Chapter.txt Title_Chapters idFFmetadata\n")
        print(f"- TitleChapters   is optional")
        print(f"- idFFmetadata   is optional, integer > 1\n\n")
