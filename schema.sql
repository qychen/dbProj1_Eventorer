DROP TABLE Event_Locates, Favors, Has_Tickets, Nearby, Participates, Performers, Performs, Restaurants, Reviews, Users, Venues;

/* entity */

CREATE TABLE Users (
	uid int PRIMARY KEY,
	password varchar(30),
	birthday date,
	image text,
	email varchar(20)
);

CREATE TABLE Venues (
	vid int PRIMARY KEY,
	name varchar(80),
	location text,
	coordinate point,
	url text
);

CREATE TABLE Event_Locates (
	eid int PRIMARY KEY,
	vid int NOT NULL,
	name text,
	description text,
	category text,
	FOREIGN KEY (vid) REFERENCES Venues
		ON DELETE CASCADE
);

CREATE TABLE Has_Tickets (
	eid int NOT NULL,
	tid int, 
	price real,
	happen_date date,
	seat varchar(30),
	seller varchar(100),
	PRIMARY KEY (tid),
	FOREIGN KEY (eid) REFERENCES Event_Locates
		ON DELETE CASCADE
);


CREATE TABLE Performers (
	pid int PRIMARY KEY,
	name text,
	type text,
	image text,
	url text
);

CREATE TABLE Restaurants (
	rid int PRIMARY KEY,
	name varchar(80),
	cuisine varchar(30),
	image text
);

/* relationship */

CREATE TABLE Participates (
	uid int REFERENCES Users,
	eid int REFERENCES Event_Locates,
	status int,
	PRIMARY KEY (uid, eid)
);

CREATE TABLE Favors (
	uid int REFERENCES Users,
	tid int REFERENCES Has_Tickets,
	time timestamp,
	PRIMARY KEY (uid, tid)
);


CREATE TABLE Performs (
	eid int REFERENCES Event_Locates,
	pid int REFERENCES Performers,
	PRIMARY KEY (pid, eid)
);

CREATE TABLE Reviews (
	cid int,
	vid int,
	uid int,
	content text,
	rating int,
	PRIMARY KEY (cid, vid, uid),
	FOREIGN KEY (vid) REFERENCES Venues
		ON DELETE CASCADE,
	FOREIGN KEY (uid) REFERENCES Users
		ON DELETE CASCADE
);


CREATE TABLE Nearby (
	vid int REFERENCES Venues,
	rid int REFERENCES Restaurants,
	distance real, 
	PRIMARY KEY (vid, rid)
);

\copy venues from data/Venues.txt 
\copy event_locates from data/Event_Locates.txt
\copy performers from data/Performers.txt
\copy performs from data/Performs.txt

