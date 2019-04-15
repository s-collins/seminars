// React components
import React from 'react';
import ReactDOM from 'react-dom';
import NavBar from './nav_bar.js';
import PageContainer from './page_container.js';
import Form from './form.js';

// CSS styles
import './w3-theme-blue-grey.css';
import './css-stars.css';
import './w3.css';

ReactDOM.render(
	<div>
		<NavBar
			logged_in = {true}
			username = "sean"
		/>
		<Form
			label_one = "Username: "
			label_two = "Password: "
			button_text = "Login"
		/>

		{/*
		<PageContainer />
		*/}
	</div>,
	document.getElementById('root')
)