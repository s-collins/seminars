import React from 'react';
import './form.css';

export default
class Form extends React.Component {

	constructor (props) {
		super(props);

		this.state = {
			input_one: null,
			input_two: null
		};

		// bind callbacks
		this.inputOneChange = this.inputOneChange.bind(this);
		this.inputTwoChange = this.inputTwoChange.bind(this);
		this.submit = this.submit.bind(this);
	}

	//--------------------------------------------------------------------------
	// rendering
	//--------------------------------------------------------------------------

	render () {
		return (
			<div className="form_middle">
			<div className="form_inner">
				<form onSubmit={this.submit}>
					<label>
						{this.props.label_one}
						<input
							type="text"
							value={this.state.input_one}
							onChange={this.inputOneChange}
						/>
					</label>

					<br />
					
					<label>
						{this.props.label_two}
						<input
							type="text"
							value={this.state.input_two}
							onChange={this.inputTwoChange}
						/>
					</label>

					<br />

					<button type="button" onClick={this.submit}>
						{this.props.button_text}
					</button>

					<br />

					<button type="button" onClick={this.props.onCancel}>
						Cancel
					</button>
				</form>
			</div>
			</div>
		);
	}

	//--------------------------------------------------------------------------
	// callbacks
	//--------------------------------------------------------------------------

	inputOneChange (event) {
		this.setState({input_one: event.target.value});
	}

	inputTwoChange (event) {
		this.setState({input_two: event.target.value});
	}

	submit () {
		this.props.onSubmit(this.state.input_one, this.state.input_two);
	}

}