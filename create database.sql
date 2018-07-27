-- Tutorial de como medir batimentos cardíacos com Arduino http://www.instructables.com/id/Heart-rate-measuring-device-using-arduino/

CREATE TABLE pacients(
   pacientId  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   name       TEXT    NOT NULL,
   birthday   DATE    NOT NULL,
   gender     CHAR(1) NOT NULL,
   obs        TEXT
);

CREATE TABLE records(
   recordId    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   pacientId   INTEGER NOT NULL,
   accX        REAL,
   accY        REAL,
   accZ        REAL,
   angX        REAL,
   angY        REAL,
   angZ        REAL,
   temperature REAL,
   pulse       INTEGER,
   height      REAL,
   FOREIGN KEY(pacientId) REFERENCES pacients(pacientId)
);
