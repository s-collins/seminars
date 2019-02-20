-- -----------------------------------------------------------------------------
-- Event
-- -----------------------------------------------------------------------------
CREATE TABLE Event (
    id_event INTEGER NOT NULL,
    title VARCHAR(500) NOT NULL,
    description TEXT,
    location VARCHAR(200),
    date DATE,
    startTime TIME,
    endTime TIME,
    url TEXT,
    PRIMARY KEY (id_event),
    FOREIGN KEY (location) REFERENCES Location(name)
);

-- -----------------------------------------------------------------------------
-- Location
-- -----------------------------------------------------------------------------
CREATE TABLE Location (
    name VARCHAR(200) NOT NULL,
    details VARCHAR(400),
    address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100),
    postcode VARCHAR(50),
    PRIMARY KEY (name)
);

-- -----------------------------------------------------------------------------
-- Rating
-- -----------------------------------------------------------------------------
CREATE TABLE Rating (
    id_rating INT NOT NULL,
    id_event INT NOT NULL,
    stars INT,
    PRIMARY KEY (id_rating),
    FOREIGN KEY (id_event) REFERENCES Event(idEvent)
);

-- -----------------------------------------------------------------------------
-- Speaker
-- -----------------------------------------------------------------------------
CREATE TABLE Speaker (
    id_speaker INTEGER,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    credentials VARCHAR(200),
    organization VARCHAR(200),
    PRIMARY KEY (id_speaker)
);

-- -----------------------------------------------------------------------------
-- Event_has_Speaker
-- -----------------------------------------------------------------------------
CREATE TABLE Event_has_Speaker (
    id_event INT NOT NULL,
    id_speaker INT NOT NULL,
    FOREIGN KEY (id_event) REFERENCES Event(id_event),
    FOREIGN KEY (id_speaker) REFERENCES Speaker(id_speaker),
    PRIMARY KEY (id_event, id_speaker)
);

