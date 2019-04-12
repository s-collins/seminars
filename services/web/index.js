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
	db.query('SELECT * FROM Event', (err, results) => {
		if (err) {
			return response.send(err);
		}
		return response.json({ data: results });
	});
});

/*
app.get('/events', (request, response) => {
	return response.json({
		"events": [
			{
				"title": "Event From Server",
				"image_url": "https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
				"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
				"location": "Fake Location",
				"date": "Fake Date",
				"start_time": "Fake Start Time",
				"end_time": "Fake End Time"
			},
			{
				"title": "Event From Server",
				"image_url": "https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
				"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
				"location": "Fake Location",
				"date": "Fake Date",
				"start_time": "Fake Start Time",
				"end_time": "Fake End Time"
			}
		]
	})
});
*/
