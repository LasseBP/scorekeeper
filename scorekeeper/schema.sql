DROP TABLE IF EXISTS User;
CREATE TABLE User (
  Name TEXT PRIMARY KEY NOT NULL,
  PassHash TEXT NOT NULL,
  Email TEXT,
  Notifications INT NOT NULL
);

DROP TABLE IF EXISTS Bet;
CREATE TABLE Bet (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Name TEXT NOT NULL,
  Description TEXT NOT NULL,
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS BetUser;
CREATE TABLE BetUser (
  UserName TEXT NOT NULL,
  BetID INTEGER NOT NULL,
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  Notifications INTEGER NOT NULL,

  --Constraints
  PRIMARY KEY(UserName,BetID),
  FOREIGN KEY(USERNAME) REFERENCES User(Name),
  FOREIGN KEY(BetID) REFERENCES Bet(ID)
);

DROP TABLE IF EXISTS ScoreChangeSet;
CREATE TABLE ScoreChangeSet (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
	BetID INTEGER NOT NULL,
	Description TEXT, --May be null
	Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

  --Constraints
  FOREIGN KEY(BetID) REFERENCES Bet(ID)
);

DROP TABLE IF EXISTS ScoreChange;
CREATE TABLE ScoreChange (
  ChangeSetID INTEGER NOT NULL,
  UserName TEXT NOT NULL,
  Change INTEGER NOT NULL,

  --Constraints
  PRIMARY KEY(ChangeSetID, UserName),
  FOREIGN KEY(ChangeSetID) REFERENCES ScoreChangeSet(ID),
  FOREIGN KEY(USERNAME) REFERENCES User(Name)
);