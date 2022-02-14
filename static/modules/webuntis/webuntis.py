from static.modules.module import *
from datetime import datetime
from bs4 import BeautifulSoup
import requests


class Webuntis(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        self.type = "webuntis"

    def get_module_html(self):
        return self.generate_module_html({
            ":::REPLACEMARKER:::": self.fetch_timetable()
        })

    def get_config_html(self):
        return self.generate_config_html({})

    def handle(self, data):
        pass

    def fetch_timetable(self):
        jsonTable = self.get_table()
        border = "border-bottom border-white"
        longestDay = sorted(list(map(lambda d: d["subjects"], jsonTable["days"])), key=lambda d: len(d))[-1]
        htmlOutput = "<table><tr><th></th>"
        for day in jsonTable["days"]:
            htmlOutput += f"<th><div>{day['day']}</div><div>{day['date']}</div></th>"
        htmlOutput += "</tr>"
        for y in range(10):
            htmlOutput += "<tr>"
            if len(longestDay) > y:
                htmlOutput += f"<td>{str(longestDay[y]['time']).replace('-', '<br>')}</td>"
            for x in range(5):
                if len(jsonTable["days"][x]["subjects"]) > y:
                    subject = jsonTable["days"][x]["subjects"][y]
                    htmlOutput += f"<td><div>{subject['subject']}</div><div>{subject['teacher']}</div><div>{subject['room']}</div></td>"
            htmlOutput += "</tr>"
        htmlOutput += "</table>"
        return htmlOutput

    def get_table(self):
        jsonOutput = {"days": []}

        date = datetime.now().strftime("%Y%m%d")
        response = requests.get(
            "https://poly.webuntis.com/WebUntis/api/public/printpreview/timetable?type=1&id=263&date=%s&formatId=7" % date,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            }, cookies={
                "schoolname": "_aGFrLWtpdHo=",
                "JSESSIONID": "FAD32C7B12CA95616863809CEE3DF41B"
            })

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("div", {"id": "timetable"}).table
        rows = table.find_all("tr", recursive=False)

        ths = rows[0].find_all("th", recursive=False)[1:]
        for th in ths:
            text = str(th.decode_contents())
            parts = text.split("<br/>")
            if len(parts) == 2:
                date = parts[1].replace(".21", ".2021")
                day = parts[0]
                special = ""
            elif len(parts) == 3:
                date = parts[1].replace(".21", ".2021")
                day = parts[0]
                special = parts[2]
            else:
                print("You fucked up")
                return
            jsonOutput["days"].append({"date": date, "day": day, "special": special, "subjects": []})

        for row in rows[1:]:
            time_parts = row.find("th", recursive=False).decode_contents().split("<br/>")
            time = f"{time_parts[0]}-{time_parts[2]}"
            tds = row.find_all("td", recursive=False)
            tds = list(filter(lambda td: "rowspan" not in td.attrs, tds))
            currentDay = 0
            for td in tds:
                if len(list(td.children)) > 0:
                    # teacher = td.find_all("td", {"class": "Z_0_0"})[0].text
                    # subject = td.find_all("td", {"class": "Z_1_0"})[0].text
                    # room = td.find_all("td", {"class": "Z_2_0"})[0].text
                    table = td.find_all("table", {"class": "et"})[0]
                    dataTds = table.find_all("td")
                    teacher = dataTds[0].text
                    subject = dataTds[1].text
                    room = dataTds[2].text

                    jsonOutput["days"][currentDay]["subjects"].append(
                        {"time": time, "teacher": teacher, "subject": subject, "room": room})

                    currentDay += 1
                else:
                    if "class" in td.attrs and "bl" in td["class"]:
                        currentDay += 1
        return jsonOutput
