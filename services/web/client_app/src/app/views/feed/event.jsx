import React from 'react';
import Session from '../../session.js';
import './tag.css'


class TagList extends React.Component {
	render () {
		return (
			<ul style={{listStyle: 'none', padding: '0px'}}>
				{this.render_tags()}
			</ul>
		);
	}

	render_tags () {
		if (this.props.tags == null) {
			return;
		}
		var tags = [];
		for (var i = 0; i < this.props.tags.data.length; i++) {
			tags.push(
				<li className="tag">
					{this.props.tags.data[i].tag_text}
				</li>
			);
		}
		return tags;
	}
}


export default
class Event extends React.Component {

	//--------------------------------------------------------------------------
	// initialization
	//--------------------------------------------------------------------------

	constructor (props) {
		super(props);

		this.state = {
			taggingFlag: false,
			candidate_tag: '',
			tags: null
		};

		// callbacks
		this.save_event = this.save_event.bind(this);
		this.show_tag_ui = this.show_tag_ui.bind(this);
		this.tag_input_update = this.tag_input_update.bind(this);
		this.save_tag = this.save_tag.bind(this);
	}

	//--------------------------------------------------------------------------
	// rendering
	//--------------------------------------------------------------------------

	render () {
		this.fetch_tags();

		if (this.state.taggingFlag) {
			return (
				<div className="w3-container w3-card w3-white w3-round w3-margin"><br />
					{this.render_title_row()}
					{this.render_summary_row()}
					{this.render_details_row()}
					{this.render_buttons()}
					{this.render_tagging_ui()}
				</div>
			);
		}

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
				<TagList tags={this.state.tags} />
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
		if (this.props.image_url == null) {
			return (
				<div className="w3-row-padding" style={{margin: "0 -16px"}}>
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
			<div>
				{/* Interested */}
				<button
					type="button"
					className="w3-button w3-theme-d1"
					style={{marginRight: "10px", marginBottom: "10px"}}
					onClick={this.save_event}
				>
					Interested
				</button>	

				{/* Add Tag */}
				<button
					type = "button"
					className = "w3-button w3-theme-d1"
					style={{marginRight: "10px", marginBottom: "10px"}}
					onClick={this.show_tag_ui}
				>
					Add Tag	
				</button>
			</div>
		);
	}

	render_tagging_ui () {
		return (
			<div className="w3-margin-bottom">
				<input type="text" onChange={this.tag_input_update} />
				<button type="button" onClick={this.save_tag}>
					Submit
				</button>
			</div>
		);
	}

	//--------------------------------------------------------------------------
	// server requests
	//--------------------------------------------------------------------------

	fetch_tags () {
		fetch('http://localhost:4000/load_tags?event_id=' + this.props.event_id)
			.then(response => response.json())
			.then(tags => this.setState({tags}));
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

	save_tag () {
		fetch('http://localhost:4000/save_tag?event_id=' + this.props.event_id + '&tag_text=' + this.state.candidate_tag);

		// hide the tagging UI
		this.setState({
			candidate_tag: '',
			taggingFlag: false
		});
	}

	show_tag_ui () {
		this.setState({
			taggingFlag: true
		});
	}

	tag_input_update (event) {
		this.setState({
			candidate_tag: event.target.value
		});
	}
}
