import React from 'react';
import {NavigationBar, NavigationButton} from './navigation/navigation.jsx';
import Form from './forms/form.jsx';
import Session from '../session.js';


export default
class RegisterView extends React.Component {

	//--------------------------------------------------------------------------
	// initialization
	//--------------------------------------------------------------------------

	constructor (props) {
		super(props);

		// bind callbacks
		this.register = this.register.bind(this);
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
					button_text='Register'
					onSubmit={this.register}
					onCancel={this.cancel}
				/>
			</div>
		);
	}

	register (username, password) {
		fetch('http://localhost:4000/register?username=' + username + '&password=' + password)
			.then(response => response.json())
			.then(response => {
				// check for failures
				if (!response.success) {
					if (response.username_is_taken) {
						alert("Failure. Username is taken.");
					}

					if (response.invalid_password) {
						alert("Failure. Wrong password.");
					}
				}

				// success
				if (response.success) {
					alert("Success! New account was created.");
				}

				Session.setDefault();
				this.props.refresh();				
			});
	}

	cancel () {
		Session.setDefault();
		this.props.refresh();
	}
}