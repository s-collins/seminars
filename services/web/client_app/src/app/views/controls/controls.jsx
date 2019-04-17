import React from 'react';
import Dropdown from 'react-dropdown'
import 'react-dropdown/style.css';

export default
class Controls extends React.Component {
	constructor (props) {
		super(props);
		this.state = {
			selected_location: "Filter events by location",
		}

		this.onLocationSelect = this.onLocationSelect.bind(this);
	}

	onLocationSelect (selection) {
		this.setState({
			selected_location: selection.label,
		})
		this.props.filter_events_by_location(selection.label);
	}

	createLocationFilter () {
		if (this.props.locations == null) {
			return;
		}

		var options = [];
		const locations = this.props.locations.data;
		for (var i = 0; i < locations.length; i++) {
			options.push(locations[i].name);
		}

		return (
			<div className="w3-container w3-card w3-round w3-margin">
				<div style={{margin: "20px 0"}}>
					<Dropdown
						options={options}
						placeholder={this.state.selected_location}
						onChange={this.onLocationSelect}
					/>
				</div>
			</div>
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

