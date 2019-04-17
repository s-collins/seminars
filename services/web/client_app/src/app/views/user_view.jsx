import React from 'react';
import {NavigationBar, NavigationButton} from './navigation/navigation.jsx';
import Feed from './feed/feed.jsx';
import Controls from './controls/controls.jsx';
import YourEvents from './saved_events/saved_events.jsx';


export default
class UserView extends React.Component {
	//--------------------------------------------------------------------------
	// initialization
	//--------------------------------------------------------------------------

	constructor (props) {
		super(props);
		this.state = {
			events: null,
			locations: null,
			saved_events: null
		};
		this.fetchEventsByLocation = this.fetchEventsByLocation.bind(this);
		this.refresh = this.refresh.bind(this);
	}

	//--------------------------------------------------------------------------
	// rendering
	//--------------------------------------------------------------------------

	render () {
		var nav_buttons = [
			<NavigationButton label={this.props.user} handler={null} />,
		];

		console.log(this.state.saved_events);

		return (
			<div>
				<NavigationBar title={this.props.title} buttons={nav_buttons} />
				<div className="w3-container w3-content" style={{maxWidth: "1200px", marginTop: "60px"}}>
					<div className="w3-col" style={{width: "70%"}}>
						<Controls
							locations={this.state.locations}
							filter_events_by_location={this.fetchEventsByLocation}
						/>
						<Feed
							events={this.state.events}
							refresh={this.refresh}
						/>
					</div>

					<div className="w3-col" style={{width: "30%"}}>
						<YourEvents events = {this.state.saved_events} />
					</div>
				</div>
			</div>
		);
	}

	refresh () {
		this.fetchSavedEvents();
		this.forceUpdate();
	}

	//--------------------------------------------------------------------------
	// server requests
	//--------------------------------------------------------------------------

	componentDidMount () {
		this.fetchAllEvents();
		this.fetchAllLocations();
		this.fetchSavedEvents();
	}

	fetchAllEvents () {
		fetch('http://localhost:4000/events')
			.then(response => response.json())
			.then(events => this.setState({events}));
	}

	fetchAllLocations () {
		fetch('http://localhost:4000/locations')
			.then(response => response.json())
			.then(locations => this.setState({locations}));
	}

	fetchEventsByLocation (location_name) {
		fetch('http://localhost:4000/events/by_location?location_name=' + location_name)
			.then(response => response.json())
			.then(events => this.setState({events}));
	}

	fetchSavedEvents () {
		fetch(`http://localhost:4000/events/by_user?username='${this.props.user}'`)
			.then(response => response.json())
			.then(saved_events => this.setState({saved_events}));
	}
}