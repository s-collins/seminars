const express = require('express');
const cors = require('cors');
const mysql = require('mysql');
const path = require('path');

//------------------------------------------------------------------------------
// setup server application
//------------------------------------------------------------------------------

const app = express();
app.use(cors());
app.listen(4000, () => {
	console.log('Server listening on port 4000.');
});

// Get the production react app
app.use(express.static(path.join(__dirname, 'client_app/build')));
app.get('/', (request, response) => {
	response.sendFile(path.join(__dirname, 'client_app/build/index.html'));
});

//------------------------------------------------------------------------------
// setup MySQL connection
//------------------------------------------------------------------------------

const db = mysql.createConnection({
	host: 'db',
	port: '3306',
	user: 'root',
	password: 'root',
	database: 'events'
});

db.connect(err => {
	if (err) {
		return err;
	}	
});

//------------------------------------------------------------------------------
// API
//------------------------------------------------------------------------------

app.get('/register', (request, response) => {
	const { username, password } = request.query;

	SELECT_USERS_BY_USERNAME = 'SELECT * FROM User WHERE username= \"' + username + '\"';
	db.query(SELECT_USERS_BY_USERNAME, (err, results) => {
		if (err) {
			return response.send(err);
		}

		if (results.length != 0) {
			return response.json({
				username_is_taken: true,
				invalid_password: false,
				success: false
			});
		}

		if (!password.length) {
			return response.json({
				username_is_taken: false,
				invalid_password: true,
				success: false
			});
		}

		// insert the user
		INSERT_NEW_USER = 'INSERT INTO User VALUES (\"' + username + '\", \"' + password + '\")';
		db.query(INSERT_NEW_USER, (err, results) => {
			if (err) {
				return response.send(err);
			}
			return response.json({
				username_is_taken: false,
				invalid_password: false,
				success: true
			});		
		});
	});
});

app.get('/login', (request, response) => {
	const { username } = request.query;

	SELECT_USERS_BY_USERNAME = 'SELECT * FROM User WHERE username= \"' + username + '\"';
	db.query(SELECT_USERS_BY_USERNAME, (err, results) => {
		if (err) {
			return response.send(err);
		}
		if (results.length == 1) {
			return response.json({success: true, password: results[0].password});
		}
		return response.json({success: false});
	});
});

app.get('/events', (request, response) => {
	const SELECT_EVENTS = 'SELECT * FROM Event ORDER BY date, start_time'
	db.query(SELECT_EVENTS, (err, results) => {
		if (err) {
			return response.send(err);
		}
		return response.json({ data: results });
	});
});

app.get('/events/by_location', (request, response) => {
	const { location_name } = request.query;
	const SELECT_EVENTS_BY_LOCATION = 
		'SELECT * FROM Event WHERE location_name= \"' +
		location_name +
		'\" ORDER BY date, start_time'
	db.query(SELECT_EVENTS_BY_LOCATION, (err, results) => {
		if (err) {
			return response.send(err);
		}
		return response.json({ data: results });
	});
});

app.get('/events/by_user', (request, response) => {
	const { username } = request.query;
	const SELECT_EVENTS_BY_USER = `
		SELECT *
		FROM Event, User_has_Event
		WHERE
			User_has_Event.username = ${username}
		AND
			Event.event_id = User_has_Event.event_id`;
	db.query(SELECT_EVENTS_BY_USER, (err, results) => {
		if (err) {
			return response.send(err);
		}
		return response.json({ data: results })
	});
});

app.get('/locations', (request, response) => {
	const SELECT_LOCATIONS = 'SELECT * FROM Location';
	db.query(SELECT_LOCATIONS, (err, results) => {
		if (err) {
			return response.send(err);
		}
		return response.json({ data: results });
	});
});

app.get('/save_event', (request, response) => {
	const { username, event_id } = request.query;
	const INSERT_SAVED_EVENT = `
		INSERT INTO User_has_Event(username, event_id) VALUES ('${username}', ${event_id})
	`;
	db.query(INSERT_SAVED_EVENT, (err, results) => {
		if (err) {
			return response.send(err);
		}
	})
});

app.get('/save_tag', (request, response) => {
	const { event_id, tag_text } = request.query;
	const INSERT_TAG = `
		INSERT INTO Tag(tag_text)
		VALUES ('${tag_text}')
	`;
	const INSERT_EVENT_HAS_TAG = `
		INSERT INTO Event_has_Tag(event_id, tag_text)
		VALUES (${event_id}, '${tag_text}')
	`;
	db.query(INSERT_TAG, (err, results) => {});
	db.query(INSERT_EVENT_HAS_TAG, (err, results) => {});
});

app.get('/load_tags', (request, response) => {
	const { event_id } = request.query;
	const SELECT_TAGS_BY_EVENT_ID = `
		SELECT *
		FROM Event_has_Tag
		WHERE Event_has_Tag.event_id = ${event_id}
	`;
	db.query(SELECT_TAGS_BY_EVENT_ID, (err, results) => {
		if (err) {
			return response.send(err);
		}
		return response.json({ data: results })
	});
})