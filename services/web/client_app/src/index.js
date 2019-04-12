import React from 'react';
import ReactDOM from 'react-dom';
import Dropdown from 'react-dropdown'
import 'react-dropdown/style.css'
import './w3-theme-blue-grey.css';
import './css-stars.css';
import './w3.css';

class Event extends React.Component {
	render () {
		return (
			<div className="w3-container w3-card w3-white w3-round w3-margin"><br />
				{this.render_title_row()}
				{this.render_summary_row()}
				{this.render_details_row()}
				{this.render_buttons()}
			</div>
		);
	}

	render_title_row () {
		return (
			<div>
				<img
					src={this.props.image_url}
					alt="icon"
					className="w3-left w3-circle w3-margin-right"
					style={{width: "60px"}}
				/>
				<a href={this.props.event_url}>
					<h4>{this.props.title}</h4>
				</a>
				<hr className="w3-clear" />
			</div>
		);
	}

	render_summary_row () {
		return (
			<p>{this.props.description}</p>
		);
	}

	render_details_row () {
		return (
			<div className="w3-row-padding" style={{margin: "0 -16px"}}>
				<div className="w3-half">
					<img
						alt=""
						src={this.props.image_url}
						className="w3-margin-bottom"
						style={{width: "100%"}}
					/>
				</div>			

				<div className="w3-half">
					<p style={{margin: "0 0 10px 0"}}>
						<strong>Location: </strong> {this.props.location}  <br />
						<strong>Date: </strong>     {this.props.date}      <br />
						<strong>Starts at: </strong>{this.props.start_time}<br />
						<strong>Ends at: </strong>  {this.props.end_time}  <br />
					</p>		
				</div>
			</div>
		);
	}

	render_location () {
		return (
			<p>
				{this.props.location}
				<br />
				{this.props.date}
				<br />
				{this.props.start_time} to {this.props.end_time}
			</p>		
		);
	}

	render_image () {
		return (
			<div className="w3-row-padding" style={{margin: "0 -16px"}}>
				<div className="w3-half">
					<img
						alt=""
						src={this.props.image_url}
						className="w3-margin-bottom"
						style={{width: "100%"}}
					/>
				</div>
			</div>
		);
	}

	render_buttons () {
		return (
			<button type="button" className="w3-button w3-theme-d1 w3-margin-bottom">
				Comment
			</button>	
		);
	}
}

class Feed extends React.Component {
	constructor (props) {
		super(props);
		this.state = {
			data: null,
		}
	}

	componentDidMount () {
		fetch('http://localhost:4000/events')
			.then(response => response.json())
			.then(data => this.setState({data}));
	}

	createEventDisplays () {
		// return early if data has not been loaded
		if (this.state.data == null) {
			return;
		}

		// create the events
		const events = this.state.data.data
		var event_displays = []
		for (var i = 0; i < events.length; i++) {
			const event = events[i];
			event_displays.push(
				<Event
					title={event.title}
					event_url={event.event_url}
					image_url={event.image_url}
					description={event.description}
					location={event.location_name}
					date={event.date}
					start_time={event.start_time}
					end_time={event.end_time}				
				/>
			)
		}
		return event_displays
	}

	render () {
		return (
			<div>
				{this.createEventDisplays()}
			</div>
		);
	}
}

class NavBar extends React.Component {
	render () {
		return (
			<div className="w3-top">
				<div className="w3-bar w3-theme-d2 w3-left-align w3-large">
					<a className="w3-bar-item w3-button w3-padding-large w3-theme-d4" href="#">
						NEOH Seminars
					</a>
				</div>
			</div>
		);
	}
}

class Controls extends React.Component {
	constructor (props) {
		super(props);
		this.state = {
			data: null
		};
	}

	componentDidMount () {
		fetch('http://localhost:4000/locations')
			.then(response => response.json())
			.then(data => this.setState({data}));
	}

	createLocationFilter () {
		if (this.state.data == null) {
			return;
		}

		var options = []
		const locations = this.state.data.data
		for (var i = 0; i < locations.length; i++) {
			options.push(locations[i].name);
		}

		return (
			<Dropdown
				options={options}
				placeholder="Filter events by location..."
				onChange={this.props.loc_filter_callback}
			/>
		);
	}

	render () {
		return (
			<div>
				{this.createLocationFilter()}
			</div>
		);
	}
}

class PageContainer extends React.Component {
	render () {
		return (
			<div
				className="w3-container w3-content"
				style={{
					"maxWidth": "800px",
					"marginTop": "80px"
			}}>
				<Controls />
				<Feed />
			</div>
		);
	}
}

ReactDOM.render(
	<div>
		<NavBar />
		<PageContainer />
	</div>,
	document.getElementById('root')
)