CREATE SCHEMA IF NOT EXISTS Seminars;
USE Seminars;

-- -----------------------------------------------------------------------------
-- Event
-- -----------------------------------------------------------------------------
CREATE TABLE Event (
    idEvent INT NOT NULL,
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
    venueName VARCHAR(200) NOT NULL,
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
    idRating INT NOT NULL,
    idEvent INT NOT NULL,
    stars ENUM('one', 'two', 'three', 'four', 'five') NOT NULL,
    PRIMARY KEY (idRating),
    FOREIGN KEY (idEvent) REFERENCES Event(idEvent)
);

-- -----------------------------------------------------------------------------
-- Speaker
-- -----------------------------------------------------------------------------
CREATE TABLE Speaker (
    idSpeaker INT NOT NULL,
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
    idEvent INT NOT NULL,
    idSpeaker INT NOT NULL,
    FOREIGN KEY (idEvent) REFERENCES Event(idEvent),
    FOREIGN KEY (idSpeaker) REFERENCES Speaker(idSpeaker)
);

