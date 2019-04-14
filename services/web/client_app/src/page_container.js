import Controls from './controls.js';
import Feed from './feed.js';
import React from 'react';
import YourEvents from './your_events.js'

export default
class PageContainer extends React.Component {
	constructor (props) {
		super(props);
		this.state = {
			events: null,
			locations: null
		};

		this.filterEventsByLocation = this.filterEventsByLocation.bind(this);
	}

	componentDidMount () {
		// get events
		fetch('http://localhost:4000/events')
			.then(response => response.json())
			.then(events => this.setState({events}));

		// get locations
		fetch('http://localhost:4000/locations')
			.then(response => response.json())
			.then(locations => this.setState({locations}));
	}

	filterEventsByLocation (location_name) {
		fetch('http://localhost:4000/events/by_location?location_name=' + location_name)
			.then(response => response.json())
			.then(events => this.setState({events}));
	}

	render () {
		return (
			<div
				className="w3-container w3-content"
				style={{
					"maxWidth": "1200px",
					"marginTop": "60px"
			}}>
				<div className="w3-col" style={{"width": "70%"}}>
					<Controls
						locations={this.state.locations}
						filter_events_by_location={this.filterEventsByLocation}
					/>
					<Feed
						events={this.state.events}
					/>
				</div>
				<div className="w3-col" style={{"width": "30%"}}>
					<YourEvents
						events = {this.state.events}
					/>
				</div>
			</div>
		);
	}
}