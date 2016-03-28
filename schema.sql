DROP TABLE Event_Locates, Favors, Has_Tickets, Nearby, Participates, Performers, Performs, Restaurants, Reviews, Users, Venues;

/* entity */

CREATE TABLE Users (
	uid int PRIMARY KEY,
	name text,
	password text,
	birthday text,
	email text,
	CHECK(char_length(password) > 5)
);

CREATE TABLE Venues (
	vid int PRIMARY KEY,
	name varchar(80),
	location text,
	coordinate point,
	url text,
	image text
);

CREATE TABLE Event_Locates (
	eid int PRIMARY KEY,
	vid int NOT NULL,
	name text,
	description text,
	category text,
	image text,
	FOREIGN KEY (vid) REFERENCES Venues
		ON DELETE CASCADE
);

CREATE TABLE Has_Tickets (
	eid int NOT NULL,
	tid int, 
	listing_count int,
	price real,
	happen_date timestamp,
	url text,
	CHECK(listing_count > 0),
	CHECK(price >=0 ),
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
	address text,
	image text,
	rating real,
	CHECK(rating >= 0 and rating <= 5)
);

/* relationship */

CREATE TABLE Participates (
	uid int REFERENCES Users,
	eid int REFERENCES Event_Locates,
	status int,
	CHECK (status = 0 or status = 1 or status = 2),
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
	CHECK(rating >= 0),
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
	CHECK(distance >= 0 and distance <= 5),
	PRIMARY KEY (vid, rid)
);

\copy venues from data/Venues.txt 
\copy event_locates from data/Event_Locates.txt
\copy performers from data/Performers.txt
\copy performs from data/Performs.txt
\copy has_tickets from data/Has_Tickets.txt
\copy users from data/Users.txt
\copy participates from data/Participates.txt
\copy favors from data/Favors.txt
\copy restaurants from data/Restaurants.txt
\copy nearby from data/Nearby.txt
\copy reviews from data/Reviews.txt
