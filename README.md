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

      * Most matches were played by Mumbai Indians followed by Royal challengers Banglore,Kolkata Knight Riders,
      Kings XI Punjab,While least number of matches were played by Kochi Tuskers Kerala, followed by Delhi Capitals.
      Rising Pune Supergiant and  Gujarat Lions played 30 match each.
      
      
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
