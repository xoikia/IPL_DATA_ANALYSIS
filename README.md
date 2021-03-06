# IPL_DATA_ANALYSIS
<p align="center">
  <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/IPL.jfif" alt="IPL">
</p>


***Note: The dataset has data till the season 2019***


Two datasets have been use one is the macthes data which stores all the informations of all the match and the other is deliveries.csv file ,this files stores all the delivery ever bowled in the tournament.

The [mathces.csv](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/matches.csv) file consist of 17 columns. ***Season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2, umpire3. The file consists of 756 rows.***

Total 756 matches were played combining all the season

	* While most of the columns didn't have any null value expect city ,winner,player_of_match, umpire1,umpire2,umpire3

	* umpire3 has most number of missing values

The [deliveries.csv](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/deliveries.csv) file consist of 21 columns, The columns are ***match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder***    

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
As Batting side Opinion:- The more you hit in last couple of Over (15???20 in T20) the more the target to defend.

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
   
   |match_id  |	  Team	              |   Player       |        Opposition	      |Balls_for_50 |Total Runs Scored |Total Balls faced|
   |----------|-----------------------|----------------|------------------------------|-------------|------------------|-----------------|
   |7895      |Kings XI Punjab	      |KL Rahul	       |Delhi Capitals	              |     14	    |       51	       |      16         |
   |511       |Kolkata Knight Riders  |YK Pathan       |Sunrisers Hyderabad	      |     15	    |       72         |      22         |
   |45	      |Kolkata Knight Riders  |SP Narine       |Royal Challengers Bangalore   |     15	    |       54	       |      17         |
   |516	      |Chennai Super Kings    |SK Raina	       |Kings XI Punjab	              |     16	    |       87	       |      25         |
   |172	      |Deccan Chargers	      |AC Gilchrist    |Delhi Capitals	              |     17	    |       85	       |      35         |
      
      
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



So this was the overall statistics, apart from that I have created two new csv files after preprocessing , they are final [Players_data.csv](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Players_data.csv), [Final_Data.csv](https://github.com/xoikia/IPL_DATA_ANALYSIS#:~:text=3%20days%20ago-,Final_Data.csv,-Add%20files%20via). These two files will be used for further anlaysis. I have created a helper files called [Utility_Functions.py](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Utility_Functions.py) which contains all the necessary class and functions to obtain the various stats. I have build the statistics of each team separately. So I will describe the statistics of Chennai Super Kings only  as it is not possible to include all those statistics here.



## **Detail Analysis of  Chennai Super Kings**

### **Reading both the separate csv files**

***Final_Data.csv file contains all the necessary informations of each matches. Players_data.csv file contains informations of the players such as teams for which they played, runs scored, wickets taken etc.***

```
final_data = pd.read_csv('Final_Data.csv')
players_data = pd.read_csv('Players_data.csv')
```


### **Loading the data of Chennai Super Kings**
```
csk_data=get_data(final_data,'Chennai Super Kings')
csk_data.head(5)
```

### **Seasons Chennai played**
```
get_season(csk_data)
```
2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2018, 2019
   
Chennai Super kings didn't played in the season 2016,2017

### **Checking the result type**
```
csk_data['result'].value_counts()
```
|normal|163|
|------|---|
|tie   |1  |

1 match was tied between csk and the opponent.


### **checking the winner when the matched was tied**
```
check_winneron_tie(csk_data)
```
|winner	         |player_of_match|
|-----------------|---------------|
|Kings XI Punjab	|J Theron       |

The winning team was Kings XI Punjab and J Theron won the player of the match.

### **checking the stats on winning**
```
runs_wickets_stats_while_winning(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Winning%20stats%20CSK.png" alt="Winning Statistics of CSK">
</p>

|                |count    |   mean    |    std    |min   |50%   | 75%   |max |
|----------------|---------|-----------|-----------|------|------|-------|----|
|win_by_runs     |52.0     |34.192308  |28.075555  |1.0   |24.0  |49.75  |97.0|
|win_by_wickets  |48.0     |6.020833   |1.907316   |1.0   |6.0   |7.00   |10.0|

From the above table as well as the box plot given below we can say that:

	   * The highest win margin while batting first is 97.0 runs.
      
	   * While batting second is 10.0  wickets.
      
	   * Around 75% Chennai Super Kings defending a target won by less than 49.75runs and 25% more than 49.75runs.
      
	   * Around 75% Chennai Super Kings chasing a target won by less than 7 wickets and 25% more than 7.0 wickets.
   
### **while winning checking the stats of win_by_runs and win_by_wickets**
```
runs_wickets_stats_while_winning(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/Losing%20stats%20CSK.png" alt="Losing Statistics of CSK">
</p>

|                |count |mean       |std        |min  |50%  |75%   |max |
|----------------|------|-----------|-----------|-----|-----|------|----|
|win_by_runs     |52.0  |34.192308  |28.075555  |1.0  |24.0 |49.75 |97.0|
|win_by_wickets  |48.0  |6.020833   |1.907316   |1.0  |6.0  |7.00  |10.0|


From the above table as well as the box plot given below we can say that:

	   * The highest win margin while batting first is 97 runs.
   
	   * While batting second is 10  wickets.
      
	   * Around 75% Chennai Super Kings defending a target won by less than 49.75runs and 25% more than 49.75runs.
   
	   * Around 75% Chennai Super Kings chasing a target won by less than 7.0 wickets and 25% more than 7 wickets.
   
   
### **Teams against which highest win margin**
   ```
   max_runs_wickets_while_win(csk_data,'Chennai Super Kings')
   ```
   
      * Chennai has highest win_by_runs of 97 against Kings XI Punjab and BB McCullum was Player of Match.
      
      * Chennai has highest win_by_wickets of 10 against Kings XI Punjab and MEK Hussey was Player of Match.
      
### **Teams against which highest defeat margin**
   ```
   max_runs_wickets_while_loss(csk_data,'Chennai Super Kings')
   ```
   
      * Chennai has highest defeat in terms of run(60) against Mumbai Indians and MG Johnson was Player of Match.
      
      * Chennai has highest defeat in terms of wickets(9) against Mumbai Indians and ST Jayasuria.
   
### **Counting the total number of matches won on different seasons**
```
win_perseason=matched_won_perseason(csk_data,'Chennai Super Kings')
win_perseason
```

|season	                  |wins|
|--------------------------|----|
|2008, Chennai Super Kings	|9   |
|2009, Chennai Super Kings	|8   |
|2010, Chennai Super Kings	|9   |
|2011, Chennai Super Kings	|11  |
|2012, Chennai Super Kings	|10  |
|2013, Chennai Super Kings	|12  |
|2014, Chennai Super Kings	|10  |
|2015, Chennai Super Kings	|10  |
|2018, Chennai Super Kings	|11  |
|2019, Chennai Super Kings	|10  |


      * In season 2013 CSK played 12 games which is the highest number of matches played in any season.
      
      * In season 2009 CSK played 8 games which is the lowest number of matches palyed in any season.
      
      
### **Checking the venue on which most number of games are played**
```
venue_stats(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/CSK%20Venues.png" alt="CSK Venues">
</p>

In majority of venues less than 5 matches has been played, we will consider those venue where more than 5 matches were played.

      * CSK played 48 matches on  MA Chidambaram Stadium, Chepauk  won 34.0 lost 14.0 with a winning percentage of 70.83
      and loss percentage of 29.16%.
      
      * CSk has Highest winning % of 83.33 on Maharashtra Cricket Association Stadium.
      
      * CSK has highest lossing %  of 54.54 on  Eden Gardens.
      
      * In 28 stadiums less than 5 games were played by CSK.
      
      
### **Number of times toss won and loss**
```
toss_stats(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/csk_toss_stats.png" alt="CSK toss stats">
</p>

Chennai Super Kings won toss 89 times and loss toss 75 times


### **Stats of winning/lossing a match based on winning/lossing toss**
```
match_won_loss(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/match_won_loss_csk.png" alt="CSK macth won loss">
</p>

Chennai Super Kings won 57 matches and loss 32 matches winning the toss .Chennai Super Kings won 43 matches and loss 32 matches lossing the toss.


### **Stats of winning/lossing a match based on winning/lossing toss**
```
match_won_loss(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/opting_bat_field_csk.png" alt="stats on different ocassion of toss">
</p>


| Toss Decision | No.Matches won | No.Matches loss |
|---------------|----------------|-----------------|
|	bat	|      30        |       18        |
| 	field	|      27	 |       14        |


### **Stats when batted or fielded first(whether opted or ask)**
```
stats_battingfirst_and_fieldingfirst(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/stats_battingfirst_fieldinfgfirst_csk.png" alt="stats on batting and fielding">
</p>

	* Batting first Chennai Super Kings won 52 and loss 37 matches.
	
	* Fielding first Chennai Super Kings won 48 and loss 26 matches.
	
	
### **Cheking the highets and lowest targets set**	
Creating an object of team_score_set
```
csk_score=team_score_set('Chennai Super Kings', csk_data)
```
**Top 5 Highest Target Set**
```
csk_score.nhighestrunset(5)
```
|BF_Set	|BF_HScorer	|BF_PlayerScored  |	winner        |
|-------|---------------|-----------------|-------------------|
|246	|M Vijay	|     127	  |Chennai Super Kings|
|240	|MEK Hussey	|     116	  |Chennai Super Kings|
|223	|SK Raina	|      99	  |Chennai Super Kings|
|222	|M Vijay	|     113	  |Chennai Super Kings|
|218	|SR Watson	|      79	  |Chennai Super Kings|


**Top 5 Lowest Target Set**
```
csk_score.nlowsetrunset(5)
```
|BF_Set	|BF_HScorer	|BF_PlayerScored|	winner        |
|-------|---------------|---------------|---------------------|
|109	|JA Morkel	|      42	|Rajasthan Royals     |
|110	|DJ Bravo	|      22	|Delhi Capitals       |
|112	|S Badrinath	|      30	|Delhi Capitals       |
|112	|SK Raina	|      36	|Mumbai Indians       |
|114	|S Badrinath	|      54	|Kolkata Knight Riders|


### **Best Players of Chennai Super Kings**
Creating a object of the best_players class
```
csk_bplayers=best_players('Chennai Super Kings', players_data)
```

**Highest Rungetter of Chennai Super Kings**
```
csk_bplayers.nhighestrungetter(5)
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/CSK%20highest%20runs%20getter.png" alt="CSK highest Run scorer">
</p>


|Player	        |Team Batting           |Innings       |   Runs  |
|---------------|-----------------------|--------------|---------|
|SK Raina	|Chennai Super Kings	|160.0	       |   4566  |
|MS Dhoni	|Chennai Super Kings	|143.0	       |   3903  |
|MEK Hussey	|Chennai Super Kings	|49.0	       |   1768  |
|M Vijay	Chennai |Super Kings	|66.0	       |   1679  |
|F du Plessis	|Chennai Super Kings	|57.0	       |   1660  |


**Highest wickettakers of Chennai Super Kings
```
csk_bplayers.nhighestwickettakers(5)
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/CSK%20highestwickettakers.png" alt="CSK highest Wickettaker">
</p>


|Player	    |        Team	| Bowling Innings | Wickets |
|-----------|-------------------|-----------------|---------|
|DJ Bravo   |Chennai Super Kings|	86.0      |  104    |
|R Ashwin   |Chennai Super Kings|	94.0	  |   90    |
|RA Jadeja  |Chennai Super Kings|	90.0	  |   81    |
|JA Morkel  |Chennai Super Kings|	75.0	  |   76    |
|MM Sharma  |Chennai Super Kings|	48.0	  |   58    |



**Best Allrounder of Chennai Super Kings**
```
csk_bplayers.nbestallrounders()
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/CSK%20bestallrounders.png" alt="CSK Best All Rounder">
</p>


|Player	  |   Team Batting    |Innings	|Runs	|Bowling Innings| Wickets|
|---------|-------------------|---------|-------|---------------|--------|
|SK Raina |Chennai Super Kings|	160	|4566   |      59	|    24  |
|DJ Bravo |Chennai Super Kings|	 62	|942	|      86	|   104  |
|RA Jadeja|Chennai Super Kings|  66	|889	|      90	|    81  |
|JA Morkel|Chennai Super Kings|  58	|827	|      75	|    76  |



### **Most impactfull player for the club**
```
mv_player(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/CSK%20MVP.png" alt="CSK MVP">
</p>

	* MS Dhoni has 15 player of match award which is the highest by any player for the club.
	
	* Followed by Suresh Raina and M Hussey 12 and 10 respectively.
	
	
### **Most impactfull player while setting or chasing a target**
```
mvp_ondifferent_ocassions(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/CSK%20MVP%20while%20chasing.png" alt="CSK MVP on different ocassions">
</p>

**BATTING FIRST**

	* Dhoni and Raina has 9 player of match award each.
	
	* In second Hussey who have 6 plyer of match.
	
	* In third Jadeja and M Vijay has 4.

**CHASING TARGET**

	* Dhoni has 6 player of match.
	
	* Hussey ,Jadeja,F du Plessis has 4 each.
	
	* Raina,Watson , DR Smith has 3 each.


Dhoni is the most important player for the team whether it is runchase or setting a target. Raina is the second most important player for the team.


### **Players with most MVP award per season**
```
mvp_for_different_Seasons(csk_data,'Chennai Super Kings')
```
<p align="center">
   <img src="https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/readme_images/CSK%20MVP%20for%20different%20seasons.png" alt="Players with MVP awards each season">
</p>


|season| player_of_match |Count |
|------|-----------------|------|
|2008  |M Ntini	         |  2   |
|2008  |MS Dhoni	 |  2   |
|2009  |M Muralitharan	 |  2   |
|2009  |ML Hayden	 |  2   |
|2010  |M Vijay	         |  2   |
|2010  |MS Dhoni	 |  2   |
|2010  |SK Raina	 |  2   |
|2011  |MEK Hussey	 |  3   |
|2012  |BW Hilfenhaus	 |  2   |
|2012  |F du Plessis	 |  2   |
|2013  |MEK Hussey	 |  5   |
|2014  |DR Smith	 |  3   |
|2014  |RA Jadeja	 |  3   |
|2015  |A Nehra	         |  3   |
|2018  |SR Watson	 |  3   |
|2019  |MS Dhoni	 |  3   |



MEK Hussey holds the record of winning most POM Awards in a season for CSK, He has won 5 Awards in 2013. Apart from him MS Dhoni and Suresh Raina are most important players for their teams.
   
   
   
This was all the statistics relating to Chennai Super Kings , while rest of the teams statistics have been uploaded you can check it. The other files are

[Delhi Capitals Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Delhi_Capitals_Analysis_Report.ipynb)
[Deccan Chargers Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Deccan_Chargers_Analysis_Report.ipynb)
[Gujarat Lions Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Gujarat_Lions_Analysis_Report.ipynb)
[Kings XI PUnjab Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Kings_XI_Punjab_Analysis_Report.ipynb)
[Kochi Tuskers Kerala Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Kochi_Tuskers_Kerala_Analysis_Report.ipynb)
[Mumbai Indian Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Mumbai_Indians_Analysis_Report.ipynb)
[Pune Warriors Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Pune_Warriors_Analysis_Report.ipynb)
[Rajasthan Royals Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Rajasthan_Royals_Analysis_Report.ipynb)
[Rising Pune Super Giant Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Rising_Pune_Supergiant_Analysis_Report.ipynb)
[Royal Challenger Bangalore Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Royal_Challengers_Bangalore_Analysis_Report.ipynb)
[Sunrisers Hyderabad Analysis](https://github.com/xoikia/IPL_DATA_ANALYSIS/blob/master/Sunrisers_Hyderabad_Analysis_Report.ipynb)





