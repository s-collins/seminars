import React from 'react';
import {NavigationBar, NavigationButton} from './navigation/navigation.jsx';
import Feed from './feed/feed.jsx';
import Controls from './controls/controls.jsx';

import Session from '../session.js';


export default
class AnonView extends React.Component {
	//--------------------------------------------------------------------------
	// initialization
	//--------------------------------------------------------------------------

	constructor (props) {
		super(props);
		this.state = {
			events: null,
			locations: null
		};

		this.fetchEventsByLocation = this.fetchEventsByLocation.bind(this);
		this.login = this.login.bind(this);
		this.register = this.register.bind(this);
	}

	//--------------------------------------------------------------------------
	// rendering
	//--------------------------------------------------------------------------

	render () {
		var nav_buttons = [
			<NavigationButton label='Login' handler={this.login} />,
			<NavigationButton label='Register' handler={this.register} />,
		];

		return (
			<div>
				<NavigationBar title={this.props.title} buttons={nav_buttons} />
				<div className="w3-container w3-content" style={{maxWidth: "1200px", marginTop: "60px"}}>
					<Controls
						locations={this.state.locations}
						filter_events_by_location={this.fetchEventsByLocation}
					/>
					<Feed events={this.state.events} />
				</div>
			</div>
		);
	}

	//--------------------------------------------------------------------------
	// server requests
	//--------------------------------------------------------------------------

	componentDidMount () {
		this.fetchAllEvents();
		this.fetchAllLocations();
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

	//--------------------------------------------------------------------------
	// callbacks
	//--------------------------------------------------------------------------

	login () {
		Session.setTryingToLogin();
		this.props.refresh();
	}

	register () {
		Session.setTryingToRegister();
		this.props.refresh();
	}
}