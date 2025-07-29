#runs inside client machine and their data is changed depending on their score

from os import write
DefaultData = {
    "LeaderBoardName" : "Null",
    "Score" : 0,
    "Client_IP" : "127.0.0.1"
}

with open("/PythonProject/FileHandlers/UpdateLeaderboard.txt", "w") as f:
    f.write(f"{DefaultData['LeaderBoardName']}, {DefaultData['Score']}, {DefaultData['Client_IP']}\n")
    f.close()
