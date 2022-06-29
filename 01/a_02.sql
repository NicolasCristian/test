SELECT
	`team`.`name`,
	SUM(
        CASE WHEN `match`.home_goals > `match`.visitor_goals
          THEN 3
        ELSE 0 END
        + CASE WHEN `match`.home_goals = `match`.visitor_goals
          THEN 1
          ELSE 0 END) AS points,
    COUNT(case when `match`.home_goals > `match`.visitor_goals then 1 end) wins,
    COUNT(case when `match`.home_goals = `match`.visitor_goals then 1 end) draws,
    COUNT(case when `match`.home_goals < `match`.visitor_goals then 1 end) losses,
    SUM(`match`.home_goals) AS goals_scored,
    SUM(`match`.visitor_goals) AS goals_taken,
    SUM(`match`.home_goals) - SUM(`match`.visitor_goals) AS goals_balance,
    SUM(`match`.home_red_cards) AS red_cards,
    SUM(`match`.home_yellow_cards) AS yellow_cards
FROM (
    SELECT `match`.home_team, `match`.home_goals, `match`.visitor_goals, `match`.home_red_cards, `match`.home_yellow_cards FROM `match`
  UNION ALL
    SELECT `match`.visitor_team, `match`.visitor_goals, `match`.home_goals, `match`.visitor_red_cards, `match`.visitor_yellow_cards FROM `match`
  ) AS `match`
INNER JOIN team
	ON `match`.home_team = `team`.id
GROUP BY home_team
ORDER BY points DESC, goals_balance DESC, wins DESC, red_cards, yellow_cards;