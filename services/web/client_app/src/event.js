import React from 'react';

export default
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
