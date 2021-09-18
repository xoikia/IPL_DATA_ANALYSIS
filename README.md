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

#### Winning margin in runs, Winning margin in wickets


    * The highest win margin by runs is 146.
    * 75% of the winning  team that batted first had a win margin of less than 19 runs and 25%  had more than 19 runs
    * The highest win margin by wickets is 10
    * 75% of the winning team that fielded first won by a margin of  less than 6 wickets and 25% more than 6 wickets
    
#### Most games officiated by an Umpire

    * S Ravi has officiated in 106 matches which is the highest number of matches officiated by any umpire, followed by Dharmasena 87.
    * Subroto Das and Nand Ksihore has least number of matches officiated, 1 each.
    
    
#### Games Played per Season
