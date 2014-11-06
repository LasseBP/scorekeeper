--Total score for user
SELECT sum(Change) as TotalScore FROM User
INNER JOIN ScoreChange
ON User.Name = ScoreChange.UserName
WHERE User.Name = 'Ivan';


--Aggregate scores for a bet
SELECT UserName,sum(change) FROM Bet
INNER JOIN ScoreChangeSet
ON ScoreChangeSet.BetID = Bet.ID
INNER JOIN ScoreChange
ON ScoreChangeSet.ID = ScoreChange.ChangeSetID
WHERE Bet.ID = 1
GROUP BY UserName;