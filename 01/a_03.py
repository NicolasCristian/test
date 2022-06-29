class Match:
  number, home, away, home_goals, away_goals = 0, "", "", 0, 0
  
  def __init__(self, number, home, away, home_goals, away_goals):
    self.number = number
    self.home = home
    self.away = away
    self.home_goals = home_goals
    self.away_goals = away_goals

  def details(self):
    print(f'Match nº {self.number}: {self.home} {self.home_goals} X {self.away_goals} {self.away}')

  def get_home(self):
    return(self.home)

  def get_goals_home(self):
    return(self.home_goals)


class Standings:
  matches = {}
  matches_total = 0

  def __init__(self, matches):
    for i, m in enumerate(matches):
      self.matches[i] = Match(number = m[0], home = m[1], away = m[2], home_goals = m[3], away_goals = m[4])
    self.matches_total = len(matches)

  def all_matches(self):
    for i, m in enumerate(self.matches):
      self.matches[i].details()

  def most_home_losses():
    print('todo')

  def most_wins():
    print('todo')

  def home_matches(self):
    hms = {}
    for i, match in self.matches.items():
      # print(match.details())
      # Matches count by team
      if ( match.home not in hms):
        hms[match.home] = {'matches': 1, 'goals': match.home_goals}
      else:
        hms[match.home] = {'matches': hms[match.home]['matches'] + 1, 'goals': hms[match.home]['goals'] + match.home_goals}
    return hms

  def average_home_goals(self):
    averages = {}
    for team, match in self.home_matches().items():
      averages[team] = round(match['goals'] / match['matches'], 2)
    return averages

  def average_matches_goals(self):
    goals_total = 0
    for i, ma in enumerate(self.matches):
      goals_total += self.matches[i].home_goals + self.matches[i].away_goals
    goals_average = goals_total / self.matches_total
    print(f'On the {self.matches_total} matches, {goals_total} were scored. The average goals count per match was: {goals_average:.1f}.')

  def most_goals_match(self):
    match_num, goal_record = 0, 0
    for i, ma in enumerate(self.matches):
      goals_total = self.matches[i].home_goals + self.matches[i].away_goals
      if goal_record <= goals_total:
        goal_record = goals_total
        match_num = self.matches[i].number
    print(f'\nThe match with most goals ({goal_record}) was:')
    self.matches[match_num - 1].details()


# Match list
# Match number, Home team, Away team, Home team goals, Away team goals
matches = [
  [1, "Corinthians", "Gremio", 1, 0],
  [2, "Corinthians", "Flamengo", 7, 1],
  [3, "Corinthians", "Bahia", 2, 1],
  [4, "Gremio", "Corinthians", 0, 3],
  [5, "Gremio", "Flamengo", 2, 0],
  [6, "Gremio", "Bahia", 2, 2],
  [7, "Flamengo", "Corinthians", 2, 8],
  [8, "Flamengo", "Gremio", 0, 0],
  [9, "Flamengo", "Bahia", 1, 0],
  [10, "Bahia", "Corinthians", 0, 0],
  [11, "Bahia", "Gremio", 1, 0],
  [12, "Bahia", "Flamengo", 1, 0]
]

standings = Standings(matches)

# To list every match and it's details
# standings.all_matches()


print('\nAverage goals by home team:')
print(standings.average_home_goals())

print('\nAverage goals by match:')
standings.average_matches_goals()

standings.most_goals_match()
