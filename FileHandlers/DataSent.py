from os import write
DefaultData = {
    "LeaderBoardName" : "Null",
    "Score" : 0,
    "Client_IP" : "127.0.0.1"
}

with open("/home/bob/PycharmProjects/PythonProject/FileHandlers/UpdateLeaderboard.txt", "w") as f:
    f.write(f"{DefaultData['LeaderBoardName']}, {DefaultData['Score']}, {DefaultData['Client_IP']}\n")
    f.close()