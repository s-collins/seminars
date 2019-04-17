import React from 'react';
import {NavigationBar, NavigationButton} from './navigation/navigation.jsx';
import Form from './forms/form.jsx';
import Session from '../session.js';


export default
class LoginView extends React.Component {
	//--------------------------------------------------------------------------
	// initialization
	//--------------------------------------------------------------------------

	constructor (props) {
		super(props);

		// bind callbacks
		this.login = this.login.bind(this);
		this.cancel = this.cancel.bind(this);
	}

	//--------------------------------------------------------------------------
	// rendering
	//--------------------------------------------------------------------------

	render () {
		return (
			<div className="form_outer">
				<NavigationBar
					title={this.props.title}
					buttons={[]}
				/>
				<Form
					label_one='Username'
					label_two='Password'
					button_text='Login'
					onSubmit={this.login}
					onCancel={this.cancel}
				/>
			</div>
		);
	}

	login (username, password) {
		fetch('http://localhost:4000/login?username=' + username)
			.then(response => response.json())
			.then(response => {
				if (response.success && response.password === password) {
					alert("Success! You have logged on.");
					Session.setLoggedIn(username);
					this.props.refresh();
				}
				else {
					alert("Failure!!!")
					Session.setDefault();
					this.props.refresh();
				}
			});
	}

	cancel () {
		Session.setDefault();
		this.props.refresh();
	}
}