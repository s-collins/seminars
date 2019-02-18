CREATE SCHEMA IF NOT EXISTS Seminars;
USE Seminars;

-- -----------------------------------------------------------------------------
-- Event
-- -----------------------------------------------------------------------------
CREATE TABLE Event (
    idEvent INT,
    title VARCHAR(500),
    description TEXT,
    location VARCHAR(200),
    date DATE,
    startTime TIME,
    endTime TIME,
    url TEXT,
    PRIMARY KEY (idEvent)
);

-- -----------------------------------------------------------------------------
-- Location
-- -----------------------------------------------------------------------------
CREATE TABLE Location (
    venueName VARCHAR(200),
    details VARCHAR(400),
    address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100),
    postcode VARCHAR(50),
    PRIMARY KEY (venueName)
);

-- -----------------------------------------------------------------------------
-- Rating
-- -----------------------------------------------------------------------------
CREATE TABLE Rating (
    idRating INT,
    idEvent INT,
    stars ENUM('one', 'two', 'three', 'four', 'five'),
    PRIMARY KEY (idRating)
);

-- -----------------------------------------------------------------------------
-- Speaker
-- -----------------------------------------------------------------------------
CREATE TABLE Speaker (
    idSpeaker INT,
    firstName VARCHAR(100),
    lastName VARCHAR(100),
    credentials VARCHAR(200),
    organization VARCHAR(200),
    PRIMARY KEY (idSpeaker)
);

-- -----------------------------------------------------------------------------
-- Event_has_Speaker
-- -----------------------------------------------------------------------------
CREATE TABLE Event_has_Speaker (
    idEvent INT,
    idSpeaker INT
);

