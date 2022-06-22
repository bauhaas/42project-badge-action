import requests, json, sys, time

data=json.loads(sys.argv[1])
token=data['access_token']

headers = {
    "Authorization": "Bearer " + token,
}


def getProjectTeam(t, pid):
    #print(t, pid)
    time.sleep(1)
    readUrl = "https://api.intra.42.fr/v2/users/" + str(t) + "/projects/" + str(pid) + "/teams"  #all info about projects_user

    res = requests.request("GET", readUrl, headers=headers)

    data2 = res.json()
    # print(data2.get(name))

    logins = []
    if data2 and data2[-1]:
        for login in data2[-1]["scale_teams"]:
            if login["corrector"] == "invisible":
                continue
            if login["corrector"]["login"]:
                logins.append(login["corrector"]["login"])
    for i in logins:
        print(i, end=' ')
    print()

    # with open('teams.json', 'w', encoding='utf-8') as f:
    #      json.dump(data2, f, ensure_ascii=False)

def getUserProjectsUsersData(headers, user, page):
    time.sleep(1)
    readUrl = "https://api.intra.42.fr/v2/users/" + user + "/projects_users?page=" + str(page)  #all info about projects_user
    global limit
    res = requests.request("GET", readUrl, headers=headers)
    data = res.json()
    t = 0
    pid = 0
    for i in data:
        t = i.get("user").get("id")
        limit+= 1
        pName = i.get("project").get("name")
        pGrade = i.get("final_mark")
        #print(pGrade, pName)
        pid = i.get("project").get("id")
        if pName.startswith("Exam") == 0 and pName.startswith("C Piscine") == 0:
             print(str(pName) + ":" + str(pGrade), end=":")
             getProjectTeam(t, pid)



    #GET /v2/users/:user_id/projects/:project_id/teams



    # readUrl = "https://api.intra.42.fr/v2/users/%s/scale_teams/as_corrected" %t  #all info about projects_user

    # res = requests.request("GET", readUrl, headers=headers)
    # data2 = res.json()
    # with open('test.json', 'w', encoding='utf-8') as f:
    #     json.dump(data2, f, ensure_ascii=False)
    # # for i in data2:
    # #     # pName = i.get("project").get("name")
    # #     # pGrade = i.get("final_mark")
    # #     print(i)

    # readUrl = "https://api.intra.42.fr/v2/users/%s/projects_users" %user  #all info about projects_user

    # res = requests.request("GET", readUrl, headers=headers)
    # data = res.json()
    # # for i in data:
    # #     pName = i.get("project").get("name")
    # #     pGrade = i.get("final_mark")
    # #     print(pName,pGrade)
    # with open('all.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False)

limit = 0
page = 1
user = str(sys.argv[2])
while page == 1 or limit % 30 == 0:
    getUserProjectsUsersData(headers, user, page)
    page += 1