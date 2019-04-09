import React from 'react';
import ReactDOM from 'react-dom';
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
				<h4>{this.props.title}</h4>
				<hr class="w3-clear" />
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
	render () {
		return (
			<div>
				{this.renderEvent()}
				{this.renderEvent()}
				{this.renderEvent()}
			</div>
		);
	}

	renderEvent () {
		return (
			<Event
				title="Sean's Test Event"
				image_url="https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
				description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
				location="Sean's Location"
				date="10 April 2019"
				start_time="04:00pm"
				end_time="05:00pm"
			/>
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

ReactDOM.render(
	<div>
		<NavBar />
		<Feed />
	</div>,
	document.getElementById('root')
)