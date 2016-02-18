/* entity */

CREATE TABLE Users (
	uid int PRIMARY KEY,
	password varchar(30),
	birthday date,
	image text,
	email varchar(20)
);

CREATE TABLE Event_Locates (
	vid int NOT NULL,
	eid int PRIMARY KEY,
	name varchar(80),
	description text,
	category varchar(30),
	image text,
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
	name varchar(50),
	birthday date,
	specialty varchar(30),
	image text
);

CREATE TABLE Venues (
	vid int PRIMARY KEY,
	location text,
	name varchar(80),
	coordinate point,
	image text
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
	pid int REFERENCES Performers,
	eid int REFERENCES Event_Locates,
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


