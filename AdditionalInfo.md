# Game Screenshots & Diagrams
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

## NEW added username customisation
Users can now select a custom color for their username. This preference is saved and automatically applied each time the account is accessed, enhancing personalization. Below is the color selection.
The leaderboard displays their usernames with the selected colors, creating a more personalised experience.

<div> 
  <img src="images/GameScreenshots/ColorOptions.JPG" alt="Username color selection" style="max-width: 200px; height: auto;"/>
  <img src="images/GameScreenshots/UsernameColor.JPG" alt="Colored username" style="max-width: 200px; height: auto;"/>
</div>



# Flowchart Depictions
This section contains flowcharts that explain how the game functions

## Leaderboard updating for added competitiveness
To increase competitiveness, bots have their scores updated by 1–3 clicks every 2 seconds.
<p align="center">
  <img src="images/Diagrams/BotLeaderboardUpdate.JPG" alt="Leaderboard Updating" />
</p>

## In Progress: Verification to Prevent Data Modification concept (user side hash verification has been added)
To prevent cheating or file tampering, this game uses HMAC (Hash-based Message Authentication Code) to verify updated leaderboard data.
<p align="center">
  <img src="images/Diagrams/leaderboard_auth_function.JPG" alt="Leaderboard Authentication" />
</p>
