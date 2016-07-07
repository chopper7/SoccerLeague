"""
Team Treehouse
Python Web Development Techdegree Program
Project 1: Build a Soccer League
"""

import random


league = [
 {'Name': 'Joe Smith',
  'Height (inches)': '42',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Jim and Jan Smith'},
 {'Name': 'Jill Tanner',
  'Height (inches)': '36',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Clara Tanner'},
 {'Name': 'Bill Bon',
  'Height (inches)': '43',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Sara and Jenny Bon'},
 {'Name': 'Eva Gordon',
  'Height (inches)': '45',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'Wendy and Mike Gordon'},
 {'Name': 'Matt Gill',
  'Height (inches)': '40',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'Charles and Sylvia Gill'},
 {'Name': 'Kimmy Stein',
  'Height (inches)': '41',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'Bill and Hillary Stein'},
 {'Name': 'Sammy Adams',
  'Height (inches)': '45',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'Jeff Adams'},
 {'Name': 'Karl Saygan',
  'Height (inches)': '42',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Heather Bledsoe'},
 {'Name': 'Suzane Greenberg',
  'Height (inches)': '44',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Henrietta Dumas'},
 {'Name': 'Sal Dali',
  'Height (inches)': '41',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'Gala Dali'},
 {'Name': 'Joe Kavalier',
  'Height (inches)': '39',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'Sam and Elaine Kavalier'},
 {'Name': 'Ben Finkelstein',
  'Height (inches)': '44',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'Aaron and Jill Finkelstein'},
 {'Name': 'Diego Soto',
  'Height (inches)': '41',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Robin and Sarika Soto'},
 {'Name': 'Chloe Alaska',
  'Height (inches)': '47',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'David and Jamie Alaska',},
 {'Name': 'Arnold Willis',
  'Height (inches)': '43',
  'Soccer Experience': 'NO',
  'Guardian Name(s)': 'Claire Willis'},
 {'Name': 'Phillip Helm',
  'Height (inches)': '44',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Thomas Helm and Eva Jones'},
 {'Name': 'Les Clay',
  'Height (inches)': '42',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Wynonna Brown'},
 {'Name': 'Herschel Krustofski',
  'Height (inches)': '45',
  'Soccer Experience': 'YES',
  'Guardian Name(s)': 'Hyman and Rachel Krustofski'}
]


def sort_experience(league):
    '''Separate league's players into two lists according to experience.
    Return the two lists of players.
    '''
    experienced, inexperienced= [], []
    for player in league:
        if player['Soccer Experience'] == 'YES':
            experienced.append(player)
        else:
            inexperienced.append(player)
    
    return experienced, inexperienced


def avg_height(team):
    '''Return average height, in inches, of players on team'''
    sum = 0
    for player in team:
        sum += float(player['Height (inches)'])
    return round(sum/len(team), 1)
    

def make_teams(exp_players, inexp_players):
    '''Randomly assign experienced and inexperienced players to 3 teams.
    If average heights of teams are not within 1 inch of each other, 
    redo the random assignment of players.
    Return the team lists.
    '''      
    team1, team2, team3 = [], [], []
    
    # Copy player lists to preserve originals for reuse if avg heights aren't
    # equivalent. Pop players from these destructable copies & add to teams.
    exp = exp_players[:]
    inexp = inexp_players[:]
    
    # Assign experienced players to teams at random till no players left
    while exp:
        for team in (team1, team2, team3):
            team.append(exp.pop(random.randint(0, len(exp)-1))) 
    
    # Assign inexperienced players to teams at random till no players left
    while inexp:
        for team in (team1, team2, team3):
            team.append(inexp.pop(random.randint(0, len(inexp)-1)))
            
    # Teams' average heights
    a1, a2, a3 = avg_height(team1), avg_height(team2), avg_height(team3)
    
    # Until avg team heights within 1 in. of each other, run team assignment
    while abs(a1-a2) >= 1.0 or abs(a1-a3) >= 1.0 or abs(a2-a3) >= 1.0:
        return make_teams(exp_players, inexp_players)
            
    return team1, team2, team3


def write_letter(player):
    '''Construct a form letter, filling in values from player dict.
    Return a string of the letter.
    '''
    # First practice date\time for each team
    if player['Team'] == 'Dragons':
        practice1 = "March 17, 1pm"
    elif player['Team'] == 'Sharks':
        practice1 = "March 17, 3pm"
    elif player['Team'] == 'Raptors':
        practice1 = "March 18, 1pm"
    else:
        practice1 = "Contact league office for date and time."
   
   # Text of letter
    lttr = (
        "Dear {0[Guardian Name(s)]},{sep}"
        "Congratulations! {0[Name]} has been chosen to play for the {0[Team]} "
        "soccer team!\n\nIn assigning players to the Dragons, Sharks, and "
        "Raptors, we strived for parity among the teams. The {0[Team]} are "
        "made up of both experienced and inexperienced players, as are the "
        "other two teams. The {0[Team]}\' average player height is roughly "
        "the same as the other two teams, so no team has a size or age "
        "advantage.{sep}"
        "The {0[Team]}\' first team practice will be on: {time}.{sep}"
        "We look forwarding to seeing {0[Name]} and you at that time.{sep}"
        "Thanks for signing up!{sep}"
        "Warmest regards,{sep}"
        "Your Youth Soccer League"
        ).format(player, time=practice1, sep=2*"\n")
    
    return lttr


if __name__ == "__main__":
    
    # Sort the players by experience
    exp_players, inexp_players = sort_experience(league)
    
    # Make three teams
    sharks, dragons, raptors = make_teams(exp_players, inexp_players)
    
    # Add Team names to players' keys, then update the league with them
    for player in sharks:
        player['Team'] = 'Sharks'
    for player in dragons:
        player['Team'] = 'Dragons'
    for player in raptors:
        player['Team'] = 'Raptors'
    
    league = sharks + dragons + raptors
    
    # Write a letter to each player's parent(s) or guardian(s)
    for player in league:
        letter = write_letter(player)
        # Save letter to text file on disk 
        filename = '{}.txt'.format(player['Name'].replace(' ', '_').lower())
        with open(filename, 'w') as f:
            f.write(letter)
