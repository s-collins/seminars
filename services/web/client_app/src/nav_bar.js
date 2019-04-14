import React from 'react';

export default
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

