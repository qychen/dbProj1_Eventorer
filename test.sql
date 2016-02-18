SELECT * FROM users;
ALTER TABLE users ADD CHECK (char_length(password) > 3);