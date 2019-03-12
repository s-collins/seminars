-- -----------------------------------------------------------------------------
-- Location
-- -----------------------------------------------------------------------------
CREATE TABLE Location (
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100),
    postcode VARCHAR(50),
    PRIMARY KEY (name)
);

-- -----------------------------------------------------------------------------
-- Event
-- -----------------------------------------------------------------------------
CREATE TABLE Event (
    id_event INTEGER NOT NULL,
    title VARCHAR(500) NOT NULL,
    description TEXT,
    location VARCHAR(100),
    date DATE,
    start_time TIME,
    end_time TIME,
    url TEXT,
    PRIMARY KEY (id_event),
    FOREIGN KEY (location) REFERENCES Location(name)
);

-- -----------------------------------------------------------------------------
-- Rating
-- -----------------------------------------------------------------------------
CREATE TABLE Rating (
    id_rating INT NOT NULL,
    id_event INT NOT NULL,
    stars INT,
    PRIMARY KEY (id_rating),
    FOREIGN KEY (id_event) REFERENCES Event(id_event)
);

-- -----------------------------------------------------------------------------
-- Speaker
-- -----------------------------------------------------------------------------
CREATE TABLE Speaker (
    id_speaker INTEGER,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
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

