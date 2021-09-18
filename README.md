# IPL_DATA_ANALYSIS
The dataset has data till the season 2019

Some of the modules need to be installed  plotly ,seaborn for visualization.
Two datasets have been use one is the macthes data which stores all the informations of all the match and the other is deliveries.csv file ,this files stores all the delivery ever bowled in the tournament.

The **mathces.csv** file consist of 17 columns. ***Season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2, umpire3. The file consists of 756 rows.***

Total 756 matches were played combining all the season
* While most of the columns didn't have any null value expect city ,winner,player_of_match, umpire1,umpire2,umpire3
* umpire3 has most number of missing values

The **deliveries.csv** file consist of 21 columns, The columns are ***match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder***    

There are 179078 entries in the deliveries.csv file.

# Some key statistics that were explored

### **Winning margin in runs, Winning margin in wickets**


    * The highest win margin by runs is 146.
    
    * 75% of the winning  team that batted first had a win margin of less than 19 runs and 25%  had more than 19 runs.
    
    * The highest win margin by wickets is 10.
    
    * 75% of the winning team that fielded first won by a margin of  less than 6 wickets and 25% more than 6 wickets.
    
### **Most games officiated by an Umpire**

    * S Ravi has officiated in 106 matches which is the highest number of matches officiated by any umpire, followed by 
    Dharmasena 87.
    
    * Subroto Das and Nand Ksihore has least number of matches officiated, 1 each.
    
    
### **Games Played per Season**

<p align="center">
  <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Matches%20Played%20per%20Season.png" alt="Matches per Season">
</p>
      
      
     * Total of 76 matches were played in the 2013 season which  is the highest number of matches played for a season.
     
     * In 2009 season 57 matches were played which is the minimum number of matches played in any season.


### **Games played per city**

<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Games%20Played%20Per%20City.png" alt="Games Played per City">
</p>
 
      * Mumbai holds the highest number 101 to host matches,followed by Kolkata 77 and Delhi 74.
      
      * Bloemfontein host least number of matches,i.e 2 , follwoed by Kimberley 3,Nagpur 3 and East London 3.
     
     
### **Games played per Venue**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Games%20Played%20Per%20Stadium.png" alt="Games Played per City">
</p>
 
 
      * A total of 40 stadiums were used from 2008-2019.
      
      * Eden Garden hosted 77 matches which is the highest number of matches hosted by any stadium followed 
      by Wankhede Stadium 73,M Chinnaswamy Stadium 73 ,Feroz Shah Kotla 67, Rajiv Gandhi International Stadium, Uppal 56.
      
      * ACA-VDCA Stadium hosted 2 matches which is the least number of matches played.
     
      
      
### **Most Succesfull Team**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Most%20Succesfull%20Team.png" alt="Most Succesfull Team">
</p>

|         Teams             |total_games	 |win	|winning_percentage|
|---------------------------|--------------------|------|------------------|
|Mumbai Indians	            |  187	         |109	|   58.288770      |
|Kings XI Punjab	    |  176	         |82	|   46.590909      |
|Chennai Super Kings	    |  164	         |100	|   60.975610      |
|Royal Challengers Bangalore|  180               |84	|   46.666667      |
|Kolkata Knight Riders	    |  178	         |92	|   51.685393      |
|Delhi Capitals	            |  177	         |77	|   43.502825      |
|Rajasthan Royals	    |  147	         |75	|   51.020408      |
|Sunrisers Hyderabad	    |  108	         |58	|   53.703704      |
|Deccan Chargers	    |  75	         |29	|   38.666667      |
|Pune Warriors	            |  46	         |12	|   26.086957      |
|Rising Pune Supergiant	    |  30	         |15	|   50.000000      |
|Gujarat Lions	            |  30	         |13	|   43.333333      |
|Kochi Tuskers Kerala	    |  14	         |6	|   42.857143      |

     *  Most matches were played by Mumbai Indians followed by Royal challengers Banglore,Kolkata Knight Riders,Kings XI Punjab,
     While least number of matches were played by Kochi Tuskers Kerala, followed by Delhi Capitals.Rising Pune Supergiant and 
     Gujarat Lions played 30 match each.

     * Most number of win is 109 for Mumbai Indians followed by Chennai Super Kings 100  and on third is Kolkata Knight Riders 
     with 92 wins .While mere 6 wins Kochi Tuskers Kerala has the least number of wins but they played only 1 season.

      * In terms of winning percentage Delhi capitals led with a winning percent of 62.5% ,they too had played only 1 season, 
      In second place with 60.97% is chennai Super Kings, and on third is Mumbai Indians with a winning percentage of 58.28%.

      
      
 ## **Most wins per Season**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Teams%20with%20most%20wins%20per%20Season.png" alt="Teams with most wins per season">
</p>

      * Most number of match won by any team in a particular season is 13. Rajasthan Royals and Mumbain Indian has achieved 
      these feat in the season 2008  and 2013 respectively.

      * Mumbai Indians has most number of wins in 4 seasons(2010, 2013, 2017, and 2019).

      
      
## **Bowler Statistics**

### **Highest Wicketakers in IPL history**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Highest%20Wickettakers.png" alt="Highest Wickettakers">
</p>

      * S Malinga has highest wickets to his name.He has taken 170 wickets in 122 matches
      * A Mishra is the second highets wicketakers with 156 wickets in 147 games.
      * In 3rd H Singh has 150 wickets in his name in 157 games.
      
      * Most number of win is 109 for Mumbai Indians followed by Chennai Super Kings 100  and on third is Kolkata Knight
      Riders with 92 wins .While mere 6 wins Kochi Tuskers Kerala has the least number of wins but they played only 1 season.
      
      * In terms of winning percentage Delhi capitals led with a winning percent of 62.5% ,they too had played only 1 season,
      In second place with 60.97% is chennai Super Kings, and on third is Mumbai Indians with a winning percentage of 58.28%.
      
 ### **Economical Bowler**
 Economy of a Bowler describes how many runs scored per ball  to the total number of balls bowled by the bowler.Considering only those bowlers who has played atleast 20 games and 20 overs.
 <p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Economical%20Bowler.png" alt="Economical Bowler">
 </p>
 
      * A kumble is the most economy bowler with a economy rate of 6.76
      
      * S Narine has the second lowest economy with 6.87
      
      * In 3rd its D Vettori with 6.88 economy rate

The top 5 economy bowlers are the Spinners.
D Steyn is the only fast bowler who is in the top 10 of lowest economy bowler with a economy rate of 6.95 


### **Bowler with Best Bowling Average**
The average number of runs conceded per wicket. (Ave = Runs/W). Considering only those bowlers who has played atleast 14 games and 20 overs.
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Bowlers%20with%20best%20Average.png" at="Bowlers with best Average">
</p>

         * BJ Hodge and  has the best bowling average of 18.24
         
         * K Rabada has the second best average of 19.32

         * D Bollinger has the third best bowling average of 19.35
         
         
### **Bowler with Best Bowling Strike Rate**
The average number of balls bowled per wicket taken. (SR = Balls/W). Considering only those bowlers who has played atleast 14 games and 20 overs.
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Bowler%20with%20Best%20Bowling%20Strike%20Rate.png" at="Bowlers with best Strike Rate">
</p>
    
      * BJ Hodge and K Rabada has the best Strike Rate of 14. He is expected to take wickets after every 14 balls bowled
      
      * A Reddy has the second best of 15.
      
      * S Gopal has the third best of 15.61.
      
      
### **Bowlers with most Maiden Overs bowled**
Maiden over is not pretty common in T20 matches as the bestman tries to hit from the very first ball faced. These are the following bowlers with most number of Maiden Overs bowled in IPL history.
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Bowlers%20with%20most%20Maiden%20Overs%20bowled.png" at="Bowlers with most maiden overs">
</p>


### **Bowlers with most number of Extra balls and Extra Runs conceeded**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Bowlers%20with%20most%20number%20of%20Extra%20balls%20and%20Extra%20Runs%20conceeded.png" at="Bowlers with Extra runs and balls bowled">
</p>

       * Malinga has bowled most number of Wide balls and he has conceeded most number of extra runs.
       
       * S Sreesanth has bowled most number of No balls.
       
       
### **Players with 5 wickets in a innings**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Players%20with%205%20wickets%20in%20a%20innings.png" at="Players with 5 wickets in a match">
</p>
      
      * There are 15 players with 5 wickets haul to their name.
      
      * J Unadkat and J Faulkner are the only players with 2 five wickets haul to their names.
      
### **Players with 4 wickets in a Innings**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Players%20with%204%20wickets%20in%20a%20Innings.png" at="Players with 4 wickets in a match">
</p>

      * Malinga and Sunil Narine are the only bolwers who has 4 wickets hawls in 6 matches.
      
### **Players with Hatricks**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Players%20with%20Hatricks.png" alt="players with hatricks">
</p>

There are 16 players who have taken hattricks. Among all the hatrick takers

      * A Mishra has 3 hatricks which is the highets by any players.
    
      * Yuvraj Singh has 2 hatricks to his name.
    
      * Rest all the hatrick takers has 1 each.
      

## **Best Bowlers at Death overs**
Death overs generally refer the last overs of the cricket match.. It is called so because those overs are the crucial overs of the match. 
As Batting side Opinion:- The more you hit in last couple of Over (15–20 in T20) the more the target to defend.

As Bowling side Opinion - The less you  concede, lesser the runs to chase to win the match.

### **Bowlers with most wickets in Death Overs**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Bowlers%20with%20most%20wickets%20in%20Death%20Overs.png" alt="players with most wickets in Death overs">
</p>

The following graph shows the number of wickets taken and number of overs bowled at death overs by a player 
       
       * Malinga has taken 120+ wickets in death overs which is the highest number of wickets taken at death overs.
       
       * DJ Bravo has taken 100+ wickets in death overs.
       
       * B Kumar has taken 80 wickets in depth overs
       
### **Top 10 Most Economical Bowlers at the Depth Overs**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Top%2010%20Most%20Economical%20Bowlers%20at%20the%20Depth%20Overs.png" alt="Economical bowler in Death overs">
</p>


      * S Gopal and Sohail Tanvir are the only bowlers who have economy rate less than 7.5

### **Bowlers with best Bowling Average at the death overs**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Bowlers%20with%20best%20Bowling%20Average%20at%20the%20death%20overs.png" alt="Bowler with best Average in  Death overs">
</p>

      * Adam Zampa and Sohail Tanvir are the only bowlers with average less than 7 
      
      
### **Bowlers with best Strike rate at the death overs**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Bowlers%20with%20best%20Strike%20rate%20at%20the%20death%20overs.png" alt="Bowler with best SR in Death overs">
</p>

      * Adam Zampa and VY Mahesh are the only bowlers with Strike Rate less than 5

## **WicketKeepers with most number of Dismissals**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/WicketKeepers%20with%20most%20number%20of%20Dismissals.png" alt="WK with most number of dismissals">
</p>

      * D Karthik has 109 numbers of caught behind which is the highest followed by MS DHoni 98.
      
      * In case of Stumpings it is lead by MS Dhoni 38 followed by Karthik Robin Uthappa 32.
      
      
## **Batsman Statistics**

### **Players with most Runs**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Players%20with%20most%20Runs.png" alt="Players with most runs scored">
</p>

      * V kohli has the highest number of runs scored. He has scored 5429 runs.
      
      * Suresh Raina has scored 5407 runs which is second highest run scored.
      
      * Kohli and Raina are the only players with more than 5000 runs.
      
      * The third highest run getter is Rohit Sharma with 4914 runs.
      
      
 ### **Fastest centuries in IPL**
 
 |match_id|      Team	               |  Player	|        Opposition	       |Balls for century |Total Runs scored |	Total Balls faced|
 |--------|----------------------------|----------------|------------------------------|------------------|------------------|-------------------|
 |411	  |Royal Challengers Bangalore |CH Gayle	|Pune Warriors		       |      30	  |      175	     |       66          |
 |176	  |Rajasthan Royals	       |YK Pathan	|Mumbai Indians	               |      37	  |      100	     |       37          |
 |448	  |Kings XI Punjab	       |DA Miller	|Royal Challengers Bangalore   |      38	  |      101	     |       38          |
 |72	  |Deccan Chargers	       |AC Gilchrist	|Mumbai Indians	               |      42	  |      109	     |       47          | 
 |36	  |Sunrisers Hyderabad	       |DA Warner	|Kolkata Knight Riders	       |      43	  |      126	     |       59          |
   
   
   ### **Fastest Fifties in IPL**
   
   |match_id  |	  Team	              |   Player	    |        Opposition	           |Balls_for_50 |Total Runs Scored |Total Balls faced|
   |----------|--------------------------|----------------|------------------------------|-------------|------------------|-----------------|
   |7895	     |Kings XI Punjab	        |KL Rahul	       |Delhi Capitals	              |     14	    |       51	        |      16         |
	|511	     |Kolkata Knight Riders	  |YK Pathan	    |Sunrisers Hyderabad	        |     15	    |       72         |	   22         |
	|45	     |Kolkata Knight Riders	  |SP Narine	    |Royal Challengers Bangalore	  |     15	    |       54	        |      17         |
	|516	     |Chennai Super Kings	     |SK Raina	       |Kings XI Punjab	              |     16	    |       87	        |      25         |
	|172	     |Deccan Chargers	        |AC Gilchrist	 |Delhi Capitals	              |     17	    |       85	        |      35         |
      
      
### **Players with most Half Centuries and Centuries**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Players%20with%20most%20Half%20Centuries%20and%20Centuries.png" alt="Players with most 50's and 100's scored">
</p>

**Most Half - Century scored**
 
       * DA Warner has 44 50's to his name which is the highest number of half century scored by any player.
       
       * S Raina has 38 half centuries to his name followed by Kohli 37 half centuries.
       
 **Most Centuries scored**
 
       * Chirs Gayle has scored 7 centuries.
       
       * Virat Kohli has scored  5 centuries.
       
       * David Warner and Shane Watson has scored 4 centuries each.
       
       
### **Player with Highest Strike rate**
Considering only those players who has scored atleast 500 runs
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Player%20with%20Highest%20Strike%20rate.png" alt="Players with highest Strike Rate">
</p>

      * A Russel has the highest Strike Rate of 179.95
      
      * Moen Ali has the next highest Strike Rate of 169.94
      
      * In third Sunil Narine with 166.94

### **Players with most number of Boundaries**
Selecting the top 10 players with most 4's and selecting the 10 player with most 6's hit ,Finally combining them to get a list of players who has hit either most 4's or 6's
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Players%20with%20most%20number%20of%20Boundaries.png" alt="Players with most boundaries scored">
</p>

**Most Six scored**

      * Chris Gayle has scored 326 sixes which is the highest number of sixes scored by a player.
      
      * AB de Villiers has scored  212 sixex.
      
      * MS Dhoni has scored 207 sixes.
      
**Most Fours scored**

      * S Dhawan has scored 526 fours which is the highest.
      
      * SK Raina has scored 495 fours.
      
      * Gautam Gambhir has scored 492 fours.
      
**Most Runs scored in Boundaries**

      * Chris Gayle has scored 3448 runs in boundaries which is the highest.
      
      * Virat Kohli has scored second highest run in boundaries, 3070 runs.
      
      * Rohit Sharma has scored 2888 runs which is the third highest.
      
      
      
### **Most Player of the Match**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Most%20Player%20of%20the%20Match.png" alt="Players with most Player of Match">
</p>
      
      * CH Gayle top the list in most number of Player of the Match in 21 ocassions.
      
      * AB de Villiers has the second most Player of the Match,20.
      
      * RG Sharma, Dhoni,Warner holds the third position with 17 Player of the Match.
      
      
### **Orange Cap Winner for each Season**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/orange%20Cap%20Winner%20each%20Season.png" alt="Orange Cap winners of each Season">
</p>

      * Among all the Orange Cap winners Virat Kohli has scored most runs in a season


### **Purple Cap Winner for each Season**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/orange%20Cap%20Winner%20each%20Season.png" alt="Purple Cap winners of each Season">
</p>

      * Among all the Purple Cap Winners , DJ Bravo has won in two different Seasons.
      
      * Among all the players who have won Purple cap in a particular season Lasith Malinga has taken highest wickets.
      
      
### **Highest Target Set**
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Top%2010%20Highest%20Target.png" alt="Top 10 Highest Target">
</p>

      * Royal Challengers Banglore has set the highest target of 263 and they have 3 top scores in Top 10 Highest Target

      * Kolkata Knight Riders have set the second highest target of 250.

## **Statistics related to the TOSS**
### **Elected Batting First**
      * Team won the toss and opting to bat first won 135 matches.
      
      * Team won the toss and opting to bat first lost  153 matches.
      
### **Elected Fielding First**
      * Team won the toss and opting to field  first won  253 matches.
      
      * Team won the toss and opting to field first lost 202 matches.
      
The number of times the team winning toss have won is  393 and the probability of winning if won the toss is  0.52

