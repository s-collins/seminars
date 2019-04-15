import React from 'react';

export default
class LoginForm extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			username: null,
			password: null
		};

		this.submitLogin = this.submitLogin.bind(this);
		this.handleUsernameInputChange = this.handleUsernameInputChange.bind(this);
		this.handlePasswordInputChange = this.handlePasswordInputChange.bind(this);
	}

	render () {
		return (
			<form
				className="w3-bar-item"
				style={{display: "inline-block"}}
				onSubmit={this.submitLogin}
			>
				<label style={{marginLeft: "20px"}}>
					Username: 
					<input
						type="text"
						style={{marginLeft: "20px"}}
						onChange={this.handleUsernameInputChange}
					/>
				</label>

				<label style={{marginLeft: "20px"}}>
					Password: 
					<input
						type="text"
						style={{marginLeft: "20px"}}
						onChange={this.handlePasswordInputChange}
					/>
				</label>

				<input type="submit" value="login" style={{marginLeft: "20px"}}/>
			</form>	
		);
	}

	handleUsernameInputChange (event) {
		this.setState({
			username: event.target.value
		});
	}

	handlePasswordInputChange (event) {
		this.setState({
			password: event.target.value
		});	
	}

	submitLogin (event) {
		// TODO: something...
	}
}