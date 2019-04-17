import React from 'react';
import './navigation.css';


export
class NavigationButton extends React.Component {
	render () {
		return (
			<button className="NavigationButton" onClick={this.props.handler}>
				{ this.props.label }
			</button>
		);
	}
}


export
class NavigationBar extends React.Component {
	render () {
		return (
			<div className="NavigationBar">
				<a className="NavigationTitle" href="#">
					{ this.props.title }
				</a>
				{ this.props.buttons }
			</div>
		);
	}
}