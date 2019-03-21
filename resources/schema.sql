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
    event_id INTEGER AUTO_INCREMENT,
    title VARCHAR(500) NOT NULL,
    description TEXT,
    location VARCHAR(100),
    date DATE,
    start_time TIME,
    end_time TIME,
    event_url TEXT,
    image_url TEXT,
    PRIMARY KEY (event_id),
    FOREIGN KEY (location) REFERENCES Location(name)
);

-- -----------------------------------------------------------------------------
-- Rating
-- -----------------------------------------------------------------------------
CREATE TABLE Rating (
    rating_id INT NOT NULL,
    event_id INT NOT NULL,
    stars INT,
    PRIMARY KEY (rating_id),
    FOREIGN KEY (event_id) REFERENCES Event(id_event)
);

-- -----------------------------------------------------------------------------
-- Speaker
-- -----------------------------------------------------------------------------
CREATE TABLE Speaker (
    speaker_id INTEGER,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    credentials VARCHAR(200),
    organization VARCHAR(200),
    PRIMARY KEY (speaker_id)
);

-- -----------------------------------------------------------------------------
-- Event_has_Speaker
-- -----------------------------------------------------------------------------
CREATE TABLE Event_has_Speaker (
    event_id INT NOT NULL,
    speaker_id INT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Event(event_id),
    FOREIGN KEY (speaker_id) REFERENCES Speaker(speaker_id),
    PRIMARY KEY (event_id, speaker_id)
);

