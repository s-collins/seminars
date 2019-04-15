import React from 'react';
import LoginForm from './login.js'

export default
class NavBar extends React.Component {
	constructor (props) {
		super(props);

		// bind callbacks
		this.registerUser = this.registerUser.bind(this);
		this.loginUser = this.loginUser.bind(this);
	}

	render () {
		return (
			<div className="w3-top">
				<div className="w3-theme-d2 w3-left-align w3-large">
					{this.title()}
					{this.props.logged_in ? this.user_info() : this.buttons()}
				</div>
			</div>
		);
	}

	registerUser () {
		// dispatch to registration callback...
		this.props.register_user_callback();
	}

	loginUser () {
		// dispatch to login callback
		this.props.login_callback();
	}

	title () {
		return (
			<a className="w3-bar-item w3-button w3-padding-large w3-theme-d4" href="#">
				NEOH Seminars
			</a>
		);
	}

	user_info () {
		return (
			<a className="w3-bar-item w3-padding-large w3-right w3-hover-white">
				{this.props.username}
			</a>
		);
	}

	buttons () {
		return (
			<div className="w3-bar-item w3-right">
				<button className="w3-bar-item w3-right" style={{border: "0", padding: "0"}} onClick={this.loginUser}>
					<a className="w3-bar-item w3-button w3-right w3-padding-large w3-hover-white">
						login
					</a>
				</button>

				<button className="w3-bar-item w3-right" style={{border: "0", padding: "0"}} onClick={this.registerUser}>
					<a className="w3-bar-item w3-button w3-right w3-padding-large w3-hover-white">
						register
					</a>
				</button>
			</div>
		);
	}
}

