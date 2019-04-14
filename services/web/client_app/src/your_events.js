import React from 'react';

class SavedEvent extends React.Component {
	render () {
		return (
			<a href={this.props.event_url}>
				<div
					className="w3-card w3-round w3-theme-dark"
					style={{padding: "5%", marginBottom: "10px"}}
				>
						<p style={{margin: "0px", marginBottom: "5px"}}>
							{this.props.title}
						</p>
				</div>
			</a>
		);
	}
}

export default
class YourEvents extends React.Component {
	render () {
		return (
			<div>
				<h4>Your Events</h4>
				{this.createEventDisplays()}
			</div>
		);
	}

	createEventDisplays () {
		// return early if no events were passed
		if (this.props.events == null) {
			return;
		}

		var event_displays = [];

		// push the event displays
		const events = this.props.events.data;
		for (var i = 0; i < events.length; i++) {
			const event = events[i];
			event_displays.push(
				<SavedEvent
					title={event.title}
					event_url={event.event_url}
					image_url={event.image_url}
					description={event.description}
					location={event.location_name}
					date={event.date}
					start_time={event.start_time}
					end_time={event.end_time}				
				/>
			);
		}

		return event_displays;
	}
}