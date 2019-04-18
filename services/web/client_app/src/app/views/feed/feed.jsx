import React from 'react';
import Event from './event.jsx';


export default
class Feed extends React.Component {

	render () {
		return (
			<div>
				{this.createEventDisplays()}
			</div>
		);
	}

	createEventDisplays () {
		// return early if data has not been loaded
		if (this.props.events == null) {
			return;
		}

		// create the events
		const events = this.props.events.data;
		var event_displays = [];
		for (var i = 0; i < events.length; i++) {
			const event = events[i];
			event_displays.push(
				<Event
					event_id={event.event_id}
					title={event.title}
					event_url={event.event_url}
					image_url={event.image_url}
					description={event.description}
					location={event.location_name}
					date={event.date}
					start_time={event.start_time}
					end_time={event.end_time}
					refresh={this.props.refresh}
				/>
			);
		}
		return event_displays;
	}
}