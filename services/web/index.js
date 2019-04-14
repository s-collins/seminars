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

app.get('/locations', (request, response) => {
	const SELECT_LOCATIONS = 'SELECT * FROM Location';
	db.query(SELECT_LOCATIONS, (err, results) => {
		if (err) {
			return response.send(err);
		}
		return response.json({ data: results });
	});
});
