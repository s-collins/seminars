import React from 'react';
import './form.css';

export default
class Form extends React.Component {
	render () {
		return (
			<div className="form_outer">
				<div className="form_middle">
					<div className="form_inner">
						<form>
							<label>
								{this.props.label_one}
								<input type="text" />
							</label>

							<br />
							
							<label>
								{this.props.label_two}
								<input type="text" />
							</label>

							<br />

							<input type="submit" value={this.props.button_text} />
						</form>
					</div>
				</div>
			</div>
		);
	}	
}