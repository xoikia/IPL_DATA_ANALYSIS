import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf
import functools
import warnings
warnings.filterwarnings('ignore')
from wordcloud import WordCloud
#%matplotlib inline
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot
import plotly.graph_objects as go
# For Notebooks
init_notebook_mode(connected=True)
# For offline use
cf.go_offline()
import plotly.io as pio
pio.renderers.default = "notebook+pdf"


class team_score_set():

    def __init__(self, teamname, database):
        self.database = database
        self.teamname = teamname

    def nhighestrunset(self, n):
        # self.teamname=teamname
        self.n = n
        self.output = self.database[(self.database['Batting_first'] == self.teamname)][
            ['BF_Set', 'BF_HScorer', 'BF_PlayerScored', 'winner']].nlargest(n=self.n, columns=['BF_Set'])
        # self.output.iplot(kind='bar',x=['Player'],y=['Runs'],xTitle='Player',yTitle='Runs',title=str(self.n)+" Players with Highest Runs")
        return self.output

    def nlowsetrunset(self, n):
        self.n = n
        self.output = self.database[(self.database['Batting_first'] == self.teamname)][
            ['BF_Set', 'BF_HScorer', 'BF_PlayerScored', 'winner']].nsmallest(n=self.n, columns=['BF_Set'])
        return self.output


class best_players():
    def __init__(self, teamname, database):
        self.database = database
        self.teamname = teamname

    def nhighestrungetter(self, n):
        self.n = n
        self.output = self.database[self.database['Team'] == self.teamname].nlargest(n=self.n, columns=['Runs'])
        self.output.iplot(kind='bar', x=['Player'], y=['Runs', 'Batting Innings'], xTitle='Player',
                          yTitle='Runs and Innings',
                          color=['darksalmon', 'lightblue'], title=str(self.n) + " Players with Highest Runs")
        return self.output[['Player', 'Team', 'Batting Innings', 'Runs']]

    def nhighestwickettakers(self, n):
        self.n = n
        self.output = self.database[self.database['Team'] == self.teamname].nlargest(n=self.n, columns=['Wickets'])
        self.output.iplot(kind='bar', x=['Player'], y=['Wickets', 'Bowling Innings'], xTitle='Player',
                          yTitle='Wickets and Innings',
                          color=['mediumorchid', 'darkseagreen'], title=str(self.n) + " Players with Highest Wickets")
        return self.output[['Player', 'Team', 'Bowling Innings', 'Wickets']]

    def nbestallrounders(self):
        '''
        Considering only those who have atleast scored 500 runs and atleast dismissed 25 wickets
         '''
        self.output = self.database[(self.database['Team'] == self.teamname) & (self.database['Runs'] >= 250) & (
                    self.database['Wickets'] >= 20)]
        if len(self.output) > 0:
            self.output.iplot(kind='bar', x=['Player'], y=['Wickets', 'Bowling Innings', 'Runs', 'Batting Innings'],
                              xTitle='Player', yTitle='Stats',
                              title=str(len(self.output)) + " Best All-Rounders")
            return self.output
        else:
            return "There are no Allrounders with atleast 25 dismissals and 250 runs " + self.teamname





# To get data based on the names of different teams
def get_data(data, x):
    '''data=name of Dataframe
    x=team name'''
    return data[(data['team1'] == x) | (data['team2'] == x)]


# finding the seasons a team played
def get_season(data):
    '''data=name of Dataframe'''
    return list(data['season'].unique())


# checking the winner when the match is tied
def check_winneron_tie(data):
    '''
    data=name of Dataframe
    '''
    winner=data[data['result']=='tie'][['winner','player_of_match']]
    if len(winner)>0:
        return winner
    else:
        return "No matches were tied"


# stats on winning
def runs_wickets_stats_while_winning(data, value):
    '''data=name of Dataframe
    value=winning team name(here our team on which analysis is made)'''
    x = data[(data['winner'] == value) & (data['win_by_runs'] != 0)][['win_by_runs']].describe(percentiles=[.5, .75])
    x['win_by_wickets'] = data[(data['winner'] == value) & (data['win_by_wickets'] != 0)][['win_by_wickets']].describe(
        percentiles=[.5, .75])

    # visualization
    color = {"boxes": "DarkGreen", "whiskers": "DarkOrange", "medians": "DarkBlue", "caps": "Gray"}
    fig, axes = plt.subplots(nrows=1, ncols=2)
    data[(data['winner'] == value) & (data['win_by_runs'] != 0)][['win_by_runs']].plot(kind='box', figsize=(8, 6),
                                                                                       ax=axes[0], color=color)
    data[(data['winner'] == value) & (data['win_by_wickets'] != 0)][['win_by_wickets']].plot(kind='box', figsize=(8, 6),
                                                                                             ax=axes[1], color=color)
    x = x.T

    print(x)
    print('\nFrom the above table as well as the box plot given below we can say that:')
    print("\n\tThe highest win margin while batting first is {} runs \n\tWhile batting second is {}  wickets".format(
        x.iloc[0]['max'], x.iloc[1]['max']))
    print(
        "\tAround 75% {0} defending a target won by less than {1}runs and 25% more than {1}runs.\n\tAround 75% {0} chasing a target won by less than {2} wickets and 25% more than {2} wickets.".format(
            value, x.iloc[0]['75%'], x.iloc[1]['75%']))


# stats on lossing
def runs_wickets_stats_while_lossing(data, value):
    '''data=name of Dataframe
    value= here our team on which analysis is made (condition is opposite to winning)'''
    ren_data = data.copy()
    ren_data.rename(columns={'win_by_runs': 'lose_by_runs', 'win_by_wickets': 'lose_by_wickets'}, inplace=True)

    x = ren_data[(ren_data['winner'] != value) & (ren_data['lose_by_runs'] != 0)][['lose_by_runs']].describe(
        percentiles=[.5, .75])
    x['lose_by_wickets'] = ren_data[(ren_data['winner'] != value) & (ren_data['lose_by_wickets'] != 0)][
        ['lose_by_wickets']].describe(percentiles=[.5, .75])

    # visualization
    color = {"boxes": "DarkGreen", "whiskers": "DarkOrange", "medians": "DarkBlue", "caps": "Gray"}
    fig, axes = plt.subplots(nrows=1, ncols=2)
    ren_data[(ren_data['winner'] != value) & (ren_data['lose_by_runs'] != 0)][['lose_by_runs']].plot(kind='box',
                                                                                                     figsize=(8, 6),
                                                                                                     ax=axes[0],
                                                                                                     color=color)
    ren_data[(ren_data['winner'] != value) & (ren_data['lose_by_wickets'] != 0)][['lose_by_wickets']].plot(kind='box',
                                                                                                           figsize=(
                                                                                                           8, 6)
                                                                                                           , ax=axes[1],
                                                                                                           color=color)

    x = x.T

    print(x)
    print('\nFrom the above table as well as the box plot we can say that:')
    print("\n\tThe highest losing margin while batting first is {} wickets\n\tWhile batting second is {} runs".format(
        x.iloc[1]['max'], x.iloc[0]['max']))
    print(
        "\tAround 75% {0} defending a target lost by less than {2} wickets and 25% more than {2} wickets.\n\tAround 75% {0} chasing a target lost by less than {1}runs and 25% more than {1}runs.".format(
            value, x.iloc[0]['75%'], x.iloc[1]['75%']))


# teams against which highest win in terms of margin
def max_runs_wickets_while_win(data, value):
    '''data=name of Dataframe
    value=winning team name(here our team on which analysis is made)'''

    team1 = data[data['winner'] == value]
    runs_team = team1[team1['win_by_runs'] == team1['win_by_runs'].max()]
    wickets_team = team1[team1['win_by_wickets'] == team1['win_by_wickets'].max()]
    run_wick_team_stats = pd.concat([runs_team, wickets_team])
    return run_wick_team_stats[
        ['season', 'id', 'city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'player_of_match',
         'win_by_wickets', 'win_by_runs']]


# teams against which highest defeat in terms of margin
def max_runs_wickets_while_loss(data, value):
    '''data=name of Dataframe
    value= team on which analysis is made (condition is opposite to winning)'''

    team1 = data[data['winner'] != value]
    runs_team = team1[team1['win_by_runs'] == team1['win_by_runs'].max()]
    wickets_team = team1[team1['win_by_wickets'] == team1['win_by_wickets'].max()]
    run_wick_team_stats = pd.concat([runs_team, wickets_team])
    return run_wick_team_stats[
        ['season', 'id', 'city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'player_of_match',
         'win_by_wickets', 'win_by_runs', ]]


# wins_perseason for a team
def matched_won_perseason(data, value):
    '''data=name of Dataframe
    value=team name on which analysis is made'''

    x = dict(data[data['winner'] == value].groupby(['season'])['winner'].value_counts())
    return pd.DataFrame(list(x.items()), columns=['season', 'wins'])


# different stats for teams on different venues
def venue_stats(data, team):
    '''data=name of Dataframe
    team=team name on which analysis is made'''
    match = dict(data['venue'].value_counts())
    venues = pd.DataFrame(list(match.items()), columns=['Venue', 'Matches_Played'])

    wins = dict(data[data['winner'] == team]['venue'].value_counts())
    mostwins_onvenue = pd.DataFrame(list(wins.items()), columns=['Venue', 'wins'])

    lose = dict(data[data['winner'] != team]['venue'].value_counts())
    mostlose_onvenue = pd.DataFrame(list(lose.items()), columns=['Venue', 'loss'])

    data_frames = [venues, mostwins_onvenue, mostlose_onvenue]

    stats_onvenue = functools.reduce(lambda left, right: pd.merge(left, right, how='outer', on=['Venue']),
                                     data_frames).fillna(0)
    stats_onvenue['win %',] = stats_onvenue['wins'] / stats_onvenue['Matches_Played'] * 100
    stats_onvenue['loss %'] = stats_onvenue['loss'] / stats_onvenue['Matches_Played'] * 100

    stats_onvenue.iplot(kind='bar', x=['Venue'], y=['Matches_Played', 'wins', 'loss'], xTitle='Venue', theme='pearl')
    return stats_onvenue


# number of times toss won and loss
def toss_stats(data, value):
    '''data=name of Dataframe
    value=team name on which analysis is made'''
    toss = data['toss_winner'].value_counts()
    toss_win = toss[value]
    toss_loss = sum(toss.drop(labels=[value]))

    # visualization
    plt.pie(np.array([toss_win, toss_loss]), labels=['toss win', 'toss loss'], shadow=True, autopct='%1.1f%%')
    plt.show()

    return f"{value} won toss {toss_win} times and loss toss {toss_loss} times"


# Match won and loss based on winning the toss and lossing the toss

def match_won_loss(data, value):
    '''data=name of Dataframe
    value=team name on which analysis is made'''

    # matches won and loss when toss is won
    won1 = data[(data['toss_winner'] == value)]['winner'].value_counts()
    victory1 = won1[value]
    defeat1 = sum(won1.drop(labels=[value]))

    # matches won and loss when toss is loss
    won2 = data[data['toss_winner'] != value]['winner'].value_counts()
    victory2 = won2[value]
    defeat2 = sum(won2.drop(labels=[value]))

    # visualization
    fig = plt.figure(figsize=(14, 10), dpi=1600)
    explode = (0, 0.1)

    axes1 = plt.subplot2grid((1, 3), (0, 0))
    plt.pie(np.array([victory1, defeat1]), labels=['won match', 'loss match'], explode=explode, autopct='%1.1f%%')
    axes1.axis('equal')
    plt.title('Toss won')

    axes2 = plt.subplot2grid((1, 3), (0, 2))
    plt.pie(np.array([victory2, defeat2]), labels=['won match', 'loss match'], explode=explode, autopct='%1.1f%%')
    axes2.axis('equal')
    plt.title('Toss loss')

    return (
        "{0} won {1} matches and loss {2} matches winning the toss .{0} won {3} matches and loss {4} matches lossing the toss"
        .format(value, victory1, defeat1, victory2, defeat2))


# stats whenever a team decided to bat first after winnig the toss  or field first after winning the toss
def opting_bat_or_field(data, value):
    toss_d = ['bat', 'field']
    stats = pd.DataFrame()
    # a=[0,0]
    for toss in toss_d:

        x = data[(data['toss_winner'] == value) & (data['toss_decision'] == toss)]['winner'].value_counts()
        if value in x.index:
            won_stat = x[value]
            loss_stat = sum(x.drop(value))
            y = pd.DataFrame(columns=['Toss Decision', 'No.Matches won', 'No.Matches loss'], index=[value])
            y['Toss Decision'] = toss
            y['No.Matches won'] = won_stat
            y['No.Matches loss'] = loss_stat

            stats = stats.append(y)
        else:
            print(value + f" has never opted to {toss} first after winning the toss")

    # visualization
    if len(stats) == 2:
        fig = plt.figure(figsize=(14, 10), dpi=1600)
        axes1 = plt.subplot2grid((1, 3), (0, 0))
        plt.pie(x=[stats.iloc[0][[1]].values, stats.iloc[0][[2]].values], labels=['Matches Won', 'Matches Loss'],
                autopct='%1.1f%%')
        plt.title(f"When toss decision is {stats.iloc[0][[0]].values[0]}")

        axes2 = plt.subplot2grid((1, 3), (0, 2))
        plt.pie(x=[stats.iloc[1][[1]].values, stats.iloc[1][[2]].values], labels=['Matches Won', 'Matches Loss'],
                autopct='%1.1f%%')
        plt.title(f"When toss decision is {stats.iloc[1][[0]].values[0]}")
    elif len(stats) == 1:

        plt.pie(x=[stats.iloc[0][[1]].values, stats.iloc[0][[2]].values], labels=['Matches Won', 'Matches Loss'],
                autopct='%1.1f%%')
        plt.title(f"When toss decision is {stats.iloc[0][[0]].values[0]}")
    else:
        pass
    return stats


# stats whenever a team decided to bat first after winnig the toss  or field first after winning the toss
def opting_bat_or_field(data, value):
    toss_d = ['bat', 'field']
    stats = pd.DataFrame()
    # a=[0,0]
    for toss in toss_d:

        x = data[(data['toss_winner'] == value) & (data['toss_decision'] == toss)]['winner'].value_counts()
        if value in x.index:
            won_stat = x[value]
            loss_stat = sum(x.drop(value))
            y = pd.DataFrame(columns=['Toss Decision', 'No.Matches won', 'No.Matches loss'], index=[value])
            y['Toss Decision'] = toss
            y['No.Matches won'] = won_stat
            y['No.Matches loss'] = loss_stat

            stats = stats.append(y)
        else:
            print(value + f" has never opted to {toss} first after winning the toss")

    # visualization
    if len(stats) == 2:
        fig = plt.figure(figsize=(14, 10), dpi=1600)
        axes1 = plt.subplot2grid((1, 3), (0, 0))
        plt.pie(x=[stats.iloc[0][[1]].values, stats.iloc[0][[2]].values], labels=['Matches Won', 'Matches Loss'],
                autopct='%1.1f%%')
        plt.title(f"When toss decision is {stats.iloc[0][[0]].values[0]}")

        axes2 = plt.subplot2grid((1, 3), (0, 2))
        plt.pie(x=[stats.iloc[1][[1]].values, stats.iloc[1][[2]].values], labels=['Matches Won', 'Matches Loss'],
                autopct='%1.1f%%')
        plt.title(f"When toss decision is {stats.iloc[1][[0]].values[0]}")
    elif len(stats) == 1:

        plt.pie(x=[stats.iloc[0][[1]].values, stats.iloc[0][[2]].values], labels=['Matches Won', 'Matches Loss'],
                autopct='%1.1f%%')
        plt.title(f"When toss decision is {stats.iloc[0][[0]].values[0]}")
    else:
        pass
    return stats


# stats on batting first/fielding first  whether they opted or ask to bat and opted to field or ask to field
def stats_battingfirst_and_fieldingfirst(data, value):
    '''data=name of Dataframe
    value=team name on which analysis is made
    '''

    # winning while batting first
    won1 = data[(data['winner'] == value) & (data['win_by_runs'] != 0)]['winner'].count()

    # loss while batting first
    loss1 = data[(data['winner'] != value) & (data['win_by_wickets'] != 0)]['winner'].count()

    'While Fielding'
    # condition for won when fielding
    won2 = data[(data['winner'] == value) & (data['win_by_wickets'] != 0)]['winner'].count()

    # condtion for loss when fielding

    loss2 = data[(data['winner'] != value) & (data['win_by_runs'] != 0)]['winner'].count()

    # visualization
    fig = plt.figure(figsize=(14, 10), dpi=1600)
    colors = ['#ff9999', '#66b3ff']
    explode = (0, 0.1)
    axes1 = plt.subplot2grid((1, 3), (0, 0))
    plt.pie(np.array([won1, loss1]), labels=['win record', 'loss record'], explode=explode, colors=colors,
            autopct='%1.1f%%')
    plt.title('Stats on setting Target')

    axes2 = plt.subplot2grid((1, 3), (0, 2))
    plt.pie(np.array([won2, loss2]), labels=['win record', 'loss record'], explode=explode, colors=colors,
            autopct='%1.1f%%')
    plt.title('Stats on Chasing Target')

    print(
        f"Batting first {value} won {won1} and loss {loss1} matches \nFielding first {value} won {won2} and loss {loss2} matches")


# Most valuable Player for the team
def mv_player(data,value):
    '''data=name of Dataframe
    value=team name on which analysis is made
    '''
    x=dict(data[data['winner']== value]['player_of_match'].value_counts())
    mv_player= pd.DataFrame(list(x.items()),columns=['Player','Number of Player of Match Award'])
    mv_player.iplot(kind='bar',x=['Player'],xTitle='Player',yTitle='Number of Player of the Match',
                    title='MV Players of '+value,color='green')

    return mv_player


#Most valueable player while setting and chasing a target
def mvp_ondifferent_ocassions(data,value):
    '''data=name of Dataframe
    value=team name on which analysis is made
    '''
    x=dict(data[(data['winner']==value)&(data['win_by_runs']!=0)]['player_of_match'].value_counts())
    y=dict(data[(data['winner']==value)&(data['win_by_wickets']!=0)]['player_of_match'].value_counts())
    stats1=pd.DataFrame(list(x.items()),columns=['Player','Setting Target'])
    stats2=pd.DataFrame(list(y.items()),columns=['Player','Chasing Target'])
    stats=pd.merge(stats1,stats2,how='outer',on='Player').fillna(0)
    stats.iplot(kind='bar',x=['Player'],xTitle='Player',yTitle='Number of Player of the Match',
                title='MVP while Chasing and Setting a Target',theme='solar')
    return stats


# most valuable players for different seasonss
def mvp_for_different_Seasons(data, value):
    '''data=name of Dataframe
    value=team name on which analysis is made
    '''
    stats = data[data['winner'] == value].groupby('season')['player_of_match'].value_counts(
        ascending=False).to_frame().set_axis(['Count'], axis='columns')
    stats.reset_index(inplace=True)

    max_pom = stats.groupby(['season'])['Count'].max().reset_index()
    df_stats = pd.merge(stats, max_pom, how='inner', on=['season', 'Count'])
    df_stats.iplot(kind='bar', x=['season', 'player_of_match'], y=['Count'],
                   xTitle='Players and Season', yTitle='Numbfer of POM', title='Players with most MVP for each Season')

    return df_stats




