import React from 'react';
import Session from '../../session.js';


export default
class Event extends React.Component {

	//--------------------------------------------------------------------------
	// initialization
	//--------------------------------------------------------------------------

	constructor (props) {
		super(props);
		this.save_event = this.save_event.bind(this);
	}

	//--------------------------------------------------------------------------
	// rendering
	//--------------------------------------------------------------------------

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
				<a href={this.props.event_url}>
					<h4>{this.props.title}</h4>
				</a>
				<hr className="w3-clear" />
			</div>
		);

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

	render_buttons () {
		return (
			<button
				type="button"
				className="w3-button w3-theme-d1 w3-margin-bottom"
				onClick={this.save_event}
			>
				Interested
			</button>	
		);
	}

	//--------------------------------------------------------------------------
	// callbacks
	//--------------------------------------------------------------------------

	save_event () {
		if (Session.isLoggedIn()) {
			const username = Session.getUser();
			fetch('http://localhost:4000/save_event?username=' + username + '&event_id=' + this.props.event_id);
			this.props.refresh();
		}
	}
}
