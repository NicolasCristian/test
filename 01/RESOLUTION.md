
Lhes entrego ambos SQL's para a geração e resolução do desafio proposto.
Também enviarei o projeto no MySQL Workbench assim como uma imagem do diagrama do banco.

## Atividade 01

```sql
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`team` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`match`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`match` (
  `id` INT NOT NULL,
  `home_team` INT NOT NULL,
  `visitor_team` INT NOT NULL,
  `home_goals` INT NULL,
  `home_corners` INT NULL,
  `home_fauls` INT NULL,
  `home_yellow_cards` INT NULL,
  `home_red_cards` INT NULL,
  `home_possession` FLOAT NULL,
  `visitor_goals` INT NULL,
  `visitor_corners` INT NULL,
  `visitor_fauls` INT NULL,
  `visitor_yellow_cards` INT NULL,
  `visitor_red_cards` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_match_team_idx` (`home_team` ASC) VISIBLE,
  INDEX `fk_match_team1_idx` (`visitor_team` ASC) VISIBLE,
  CONSTRAINT `fk_match_team`
    FOREIGN KEY (`home_team`)
    REFERENCES `mydb`.`team` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_match_team1`
    FOREIGN KEY (`visitor_team`)
    REFERENCES `mydb`.`team` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `mydb`.`team`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`team` (`id`, `name`) VALUES (1, 'Corinthians');
INSERT INTO `mydb`.`team` (`id`, `name`) VALUES (2, 'Flamengo');
INSERT INTO `mydb`.`team` (`id`, `name`) VALUES (3, 'Coritiba');
INSERT INTO `mydb`.`team` (`id`, `name`) VALUES (4, 'Gremio');
INSERT INTO `mydb`.`team` (`id`, `name`) VALUES (5, 'Internacional');

COMMIT;


-- -----------------------------------------------------
-- Data for table `mydb`.`match`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (1, 1, 2, 3, 1, 1, 0, 0, 65, 1, 2, 2, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (2, 1, 3, 2, 4, 3, 1, 2, 70, 0, 2, 4, 1, 2);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (3, 1, 4, 5, 4, 3, 2, 1, 70, 1, 2, 4, 1, 2);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (4, 1, 5, 2, 7, 5, 1, 2, 80, 0, 2, 5, 1, 1);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (5, 2, 1, 0, 2, 2, 1, 3, 40, 2, 2, 2, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (6, 2, 3, 0, 4, 3, 4, 2, 20, 3, 2, 1, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (7, 2, 4, 2, 5, 1, 5, 3, 50, 3, 2, 6, 1, 2);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (8, 2, 5, 3, 2, 6, 2, 1, 56, 2, 2, 2, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (9, 3, 1, 1, 4, 4, 2, 0, 23, 1, 2, 2, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (10, 3, 2, 1, 3, 3, 4, 2, 80, 0, 2, 2, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (11, 3, 4, 1, 3, 2, 1, 0, 25, 0, 2, 2, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (12, 3, 5, 1, 5, 4, 3, 0, 40, 0, 2, 2, 1, 1);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (13, 4, 1, 2, 1, 2, 0, 0, 30, 0, 2, 5, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (14, 4, 2, 0, 2, 5, 0, 0, 30, 0, 2, 2, 1, 2);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (15, 4, 3, 1, 5, 6, 1, 0, 20, 2, 2, 1, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (16, 4, 5, 2, 6, 6, 2, 0, 40, 2, 2, 3, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (17, 5, 1, 2, 2, 6, 3, 0, 40, 3, 2, 4, 1, 2);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (18, 5, 2, 2, 5, 2, 4, 0, 12, 0, 2, 2, 1, 0);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (19, 5, 3, 3, 3, 1, 1, 1, 80, 2, 2, 2, 1, 1);
INSERT INTO `mydb`.`match` (`id`, `home_team`, `visitor_team`, `home_goals`, `home_corners`, `home_fauls`, `home_yellow_cards`, `home_red_cards`, `home_possession`, `visitor_goals`, `visitor_corners`, `visitor_fauls`, `visitor_yellow_cards`, `visitor_red_cards`) VALUES (20, 5, 4, 0, 5, 4, 2, 1, 22, 1, 2, 2, 2, 0);

COMMIT;

```


## Atividade 02

```sql
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
```