var Session = (function () {
	window.localStorage.setItem('state', 'default');
	window.localStorage.setItem('user', '');

	//--------------------------------------------------------------------------
	// MUTATORS
	//--------------------------------------------------------------------------

	var setDefault = function () {
		window.localStorage.setItem('state', 'default');
	};

	var setLoggedIn = function (user) {
		window.localStorage.setItem('state', 'logged_in');
		window.localStorage.setItem('user', user);
	};

	var setTryingToLogin = function () {
		window.localStorage.setItem('state', 'logging_in');
	};

	var setTryingToRegister = function () {
		window.localStorage.setItem('state', 'registering');
	}

	//--------------------------------------------------------------------------
	// ACCESSORS
	//--------------------------------------------------------------------------

	var isLoggedIn = function () {
		return window.localStorage.getItem('state') === 'logged_in';
	};

	var isTryingToLogin = function () {
		return window.localStorage.getItem('state') === 'logging_in';
	};

	var isTryingToRegister = function () {
		return window.localStorage.getItem('state') === 'registering';
	};

	var getUser = function () {
		return window.localStorage.getItem('user');
	};

	return {
		isLoggedIn: isLoggedIn,
		isTryingToLogin: isTryingToLogin,
		isTryingToRegister: isTryingToRegister,
		setTryingToLogin: setTryingToLogin,
		setTryingToRegister: setTryingToRegister,
		setDefault: setDefault,
		setLoggedIn: setLoggedIn,
		getUser: getUser,
	};
})();

export default Session;