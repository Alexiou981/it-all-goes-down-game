# IT ALL GOES DOWN ADVENTURE GAME

It All Goes Down is a command-line based adventure game that allows the user to choose which turn of events the story will take, depending on the decisions made when asked at various points throughout the story. The game runs on Heroku at the mock Terminal created by Code Institute.

The user goal is to try and make it out alive and overcome all challenges that have to be faced whilts playing the game. As the story unfolds the player is asked to make various decisions, those need to be made wisely since some decision are fatal and lead to a game over.

In terms of UX, this game is designed to offer entertainment to whoever decides to play it. Also, it is a good practice for anyone who would like to improve in decision making since some decision either make you win the game or die. All fatal decisions offer the abillity to play again, which means that the user can try as many time as they want until they reach their objective which is to survive the adventure.

The live site can be found [here](https://it-all-goes-down-530830bd039b.herokuapp.com/)

![am-I-responsive](assets/images/am-i-responsive.png)

## **Features**
### *Existing Features*

- __Landing Page__

    - The landing page welcomes the user asking them if they would like to play the game or not.
    - If the user types in "Yes" then the game starts.
    - If the user types in "No" then a goodbye message appears and the game ends.

![Landing-Image](assets/images/landing-image.png)

- __Choose a Name Screen__

    - As soon as the game begins the user is being asked to input their name.

![Name-Screen](assets/images/name-screen.png)

- __Transportation Decision__

    - Once a name is type in the story begins to unfold.
    - This is the first decision making stop of the game.
    - The user is being asked to choose which means of transport they would like to travel with.

![Tansportation-Screen](assets/images/transportation-decision.png)

- __Stay or Jump Decision__

    - Both the ship and the plane path end up in the same outcome.
    - However, the ship paths offers the player with another moment of a necessity to make a decision.
    - Jump from the sinking ship or wait for guidance from the crew.

![Junp-Or-Stay](assets/images/jump-or-stay.png)

- __Beach or Explore Decision__

    - The next decision after which means of transport to choose, 
    is whethere to stay at the beach or explore the forest for resources?
    - Depending on the games decision the story unfolds differently.

![Beach-Or-Explore](assets/images/beach-or-explore.png)

- __Drink From Lake__

    - Depending on which decision the user has made, the story eventually come to that point in which the user finds a lake.
    - Whether they decide to drink or not the story takes different turns.

![Drink-From-Lake](assets/images/drink-from-lake.png)

- __Uphill Or Downhill__

    - The next decision the player comes accross is when the path after a while of walking splits in two opposite directions.
    - The player is being asked whether they want to go uphill or downhill.

![Uphill-Or-Downhill](assets/images/uphill-or-downhill.png)

- __West Or East__

    - Depending upon the previous decision the game at some point brings the player in need of making a decision.
    - Head West depending on what you can see or East.

![West-Or-East](assets/images/west-or-east.png)

- __Fight Or Flight__

    - Heading west leads to a life threatening situation and immediate danger.
    - It's up to the player to decide whether to fight or flight for their life.

![Fight-Or-Flight](assets/images/fight-or-flight.png)

- __Stop Or Help__

    - Heading east also leads to another life threatening scenario.
    - Again, it's the players decision whether to try and put out the fire and try and seek out for help.

![Stop-Or-Help](assets/images/stop-or-help.png)

- __Win Screen__

    - If you manage to make it out alive and your decision making for survival was effective then you come accross this screen.
    - It also let's the user decide whether to play again or exit.

![You-Win](assets/images/you-win.png)

- __Game Over__

    - If the wrong survival decisions have been made the user ends up on this screen.
    - It also let's the user decide whether to play again or exit.

![Game-Over](assets/images/game-over.png)

### *Potential Future Features*

- Add more twists and turns to the story.
- Offer more decision making to the user.
- Add difficulty modes, and depending on user choice make the story harder or easier to win.
- Implement the ability of being able to loot items and have limited storage depending on bag size.
- Implement ability to add or remove items depending on needs.
- Design the terminal even more.
- Design CSS and add custom game background.

## **Mockup**

- The planning before writing any code had been done using [Lucidcharts](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=354596043016&km_CPC_TargetID=kwd-33511936169&km_CPC_Country=9046553&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=CjwKCAiAuNGuBhAkEiwAGId4ak_DnJqkIQGh8_5ODViJ07z6jzUZbNnUYZEso-G56pdgrzHKGAynIRoCfnsQAvD_BwE).

- The planning was split in three different sections:

    - The functions map.

        ![Functions-Map](assets/images/functions-map.png)
    
    - The game workflow.

        ![Game-Workflow](assets/images/game-workflow.png)
    
    - The storyline.

        ![Storyline1](assets/images/storyline1.png)

        ![Storyline1](assets/images/storyline2.png)

        ![Storyline1](assets/images/storyline3.png)


## **Testing**

- All questions have been thoroughly tested for invalid or empty input.
    - Would you like to play the game? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - What's your characters name? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - How would you like to travel? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - Stay or Jump from ship? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - Remain at Beach or Explore forrest? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - Would you like to drink from lake? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - Uphill or Downhill? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - West or East? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - Fight or Flight? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - Stop Fire or Seek Help? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
    - Would you like to try/play again? (Empty and invalid values print out an error message to the user advising them which values are accepted. It does not matter what capitalisation is used as long as the words are written identically).
- All of them functioned as they should and only continued to run the game when either of the desired inputs was typed in.
    - Would you like to play the game? (Valid values have to be words only and as soon as the user types in a correct value the story begins).
    - What's your characters name? (Valid values have to be words only and as soon as the user types in a correct value the story begins).
    - How would you like to travel? (Valid values have to be words only and as soon as the user types in a correct value the game continues).
    - Stay or Jump from ship? (Valid values have to be words only and as soon as the user types in a correct value the game continues).
    - Remain at Beach or Explore forrest? (Valid values have to be words only and as soon as the user types in a correct value the game continues).
    - Would you like to drink from lake? (Valid values have to be words only and as soon as the user types in a correct value the game continues).
    - Uphill or Downhill? (Valid values have to be words only and as soon as the user types in a correct value the game continues).
    - West or East? (Valid values have to be words only and as soon as the user types in a correct value the game continues).
    - Fight or Flight? (Valid values have to be words only and as soon as the user types in a correct value the game continues).
    - Stop Fire or Seek Help? (Valid values have to be words only and as soon as the user types in a correct value the game continues).
    - Would you like to try/play again? (Valid values have to be words only and as soon as the user types in a correct value the game continues).

- Tested on Macbook Pro 13" on Google Chrome, game was functioning as expected.
- Tested on ASUS Zenbook 13" on Google Chrome, the game was functioning as expected on that laptop too.

### *Validator Testing*

- Run.py file passed through PEP8 linter without any errors.

![Run.py-Linter](assets/images/run.py-linter.png)

- Ascii.py file passed through PEP8 linter without any errors.

![Ascii.py-Linter](assets/images/ascii.py-linter.png)

- Settings.py file passed through PEP8 linter without any errors.

![Settings.py-Linter](assets/images/settings.py-linter.png)
 
### *Unfixed Bugs*
- Not applicable.

## **Creating GitHub Repository**

- Click on the Repositories tab.
- On the top right-hand corner there is a green button that says "New", click on that.
- Give the new repository a name, "it-all-goes-down-game" in this case.
- Ensure the repository is public by clicking on the Public button under the Description field.
- Click on the Add README file in order to have this file included automatically.
- Lastly, at the bottom right-hand corner click on "Create repository".
- The new repository should be now available on the repositories tab on GitHub.

## **Deployment on Heroku** 

- Login or Register on Heroku.
- At the top-right corner click on New.
- From the scroll down menu select Create New App.
- Give a name to your App and click on Create App.
- From the top scrollbar click on Settings.
- At the setting tab find the Buildpacks section.
- Click on Add buildpack, and install Python first and Node.js second.
- Click on the Deploy tab.
- On the deployment method section, select Github.
- Search for your repository, select it and click connect.
- You can enable automatic deploys for every time you push something on Github(I have selected to do this for this project)
- Or you can go to the Manual deploy section, search for the name of the branch and once you find it and select it click Deploy Branch.

    
## **Credits**

- Code Institute for offering the template for the mock terminal on Heroku.
- My mentor [Lauren-Nichole](https://github.com/CluelessBiker) for all the advice and guidance whilst working on this project.
- The ascii art was taken from [fsymbols](https://fsymbols.com/text-art/) and [asciiart](https://www.asciiart.eu/)
- The ascii compass (West/East decision) was taken from [here](https://emojicombos.com/compass-dot-art)
- The code used as a slowprint function was taken from [here](https://github.com/DebbieBergstrom/Russian-Roulette/blob/main/all_functions.py) by Debbie Bergstrom.

