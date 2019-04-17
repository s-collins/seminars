import React from 'react';
import AnonView from './views/anon_view.jsx';
import LoginView from './views/login_view.jsx';
import RegisterView from './views/register_view.jsx';
import UserView from './views/user_view.jsx';
import Session from './session.js';


export default
class App extends React.Component {
	constructor (props) {
		super(props);
		this.refresh = this.refresh.bind(this);
	}

	render () {
		if (Session.isLoggedIn()) {
			return (
				<UserView
					title = 'NEOH Seminars'
					user = {Session.getUser()}
				/>
			);
		}

		if (Session.isTryingToLogin()) {
			return (
				<LoginView
					title = 'NEOH Seminars'
					refresh = {this.refresh}
				/>
			);
		}

		if (Session.isTryingToRegister()) {
			return (
				<RegisterView
					title = 'NEOH Seminars'
					refresh = {this.refresh}
				/>
			);
		}

		return (
			<AnonView
				title = 'NEOH Seminars'
				refresh = {this.refresh}
			/>
		);
	}

	refresh () {
		this.forceUpdate();
	}
}
