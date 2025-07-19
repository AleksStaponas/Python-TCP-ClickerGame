# Game Screenshots
## Login Page
This game allows users to create an account with a username and password, and saves their score to a hashed file(hashing functions in progress). When the user logs in again, their data (username, password, score) is loaded from the file so they can continue where they left off. If the account doesn’t exist, a new one is created.

<p align="center">
  <img src="images/GameScreenshots/LoginPage.JPG" alt="Login Page" />
</p>

## Game Play
This is what the Cookie Clicker game looks like. The button has animations for looks, and the leaderboard updates based on the player's score.

<p align="center">
  <img src="images/GameScreenshots/Leaderboard.JPG" alt="Leaderboard" />
</p>

## Leaderboard update

<p align="center">
  <img src="images/GameScreenshots/LeaderboardUpdating.JPG" alt="Leaderboard Update Example" />
</p>

# Flowchart Depictions
This section contains flowcharts that explain how the game functions

## Leaderboard updating for added competitiveness
To increase competitiveness, bots have their scores updated by 1–3 clicks every 2 seconds.
<p align="center">
  <img src="images/Diagrams/BotLeaderboardUpdate.JPG" alt="Leaderboard Updating" />
</p>

## In Progress: Verification to Prevent Data Modification
To prevent cheating or file tampering, this game uses HMAC (Hash-based Message Authentication Code) to verify updated leaderboard data.
<p align="center">
  <img src="images/Diagrams/leaderboard_auth_function.JPG" alt="Leaderboard Authentication" />
</p>
