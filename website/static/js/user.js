document.write(
		'\
		<div id="login_dialog-form" title="Login" style="display:none">\
		<form>\
		<fieldset>\
		<label for="username" style="width:100px">Username</label>\
		<input type="text" name="username" id="username1" maxlength="20" class="text ui-widget-content ui-corner-all">\
		<label for="password" style="width:100px">Password</label>\
		<input type="password" name="password" id="password" maxlength="20" class="text ui-widget-content ui-corner-all">\
		<input type="submit" tabindex="-1" style="position:absolute; top:-1000px">\
		</fieldset>\
		</form>\
		</div>\
		<div id="newuser_dialog-form" title="NewUser" style="display:none">\
		<form>\
		<fieldset>\
		<label for="username" style="width:100px">Username</label>\
		<input type="text" name="username" id="username" maxlength="20" class="text ui-widget-content ui-corner-all">\
		<label for="password" style="width:100px">Password</label>\
		<input type="password" name="password1" id="password1" maxlength="20" class="text ui-widget-content ui-corner-all">\
		<label for="password" style="width:100px">Confirm Password</label>\
		<input type="password" name="password2" id="password2" maxlength="20" class="text ui-widget-content ui-corner-all">\
		<label for="password" style="width:100px">Name</label>\
		<input type="text" name="password2" id="name" maxlength="20" class="text ui-widget-content ui-corner-all">\
		<label for="password" style="width:100px">Birthday</label>\
		<input type="text" name="password2" id="birthday" maxlength="20" class="text ui-widget-content ui-corner-all">\
		<label for="password" style="width:100px">email</label>\
		<input type="text" name="password2" id="email" maxlength="20" class="text ui-widget-content ui-corner-all">\
		<!-- Allow form submission with keyboard without duplicating the dialog button -->\
		<input type="submit" tabindex="-1" style="position:absolute; top:-1000px">\
		</fieldset>\
		</form>\
		</div>\
		'
);

if (localStorage.getItem("username")) {
	var login = document.getElementById("nav-LOGIN");
	var prof = document.getElementById("profile");
	login.text = localStorage.getItem("username");
	login.onclick = user_logout;
	prof.style.display = 'block';
	prof.href = '/users/'+localStorage.getItem("username");
}
else{
	var login = document.getElementById("nav-LOGIN");
	login.text = "LOGIN";

}

var ipaddress = "http://localhost:5000/";

function ReloadUserInfo(username,json)
{
	alert("Success!");
	localStorage.setItem("username", username);
	location.reload();
}

function new_user(){

	var neuser_dialog;
/*
	function create() {
		var pwd1 = document.getElementById("password1");
		var pwd2 = document.getElementById("password2");
		var username = document.getElementById("username");
		if (pwd1.value == pwd2.value) {
			$.post(ipaddress+"UserServlet",{flag:"3",usern:username.value,pwd:pwd1.value},function(data,status){
				console.log(data.split('\n')[0]);
				if (data.split('\n')[0] == "yes") {

					//sending request to UserServlet
					var UserController = ipaddress + "/UserServlet";
					var user = "";
					var xhr = new XMLHttpRequest();
					console.log(username.value);
					UserController += "?username=" + encodeURIComponent(username.value) + "&password=" + encodeURIComponent(pwd1.value) + "&flag=" + "2";
					user = username.value;

					xhr.onreadystatechange = function() {
						console.log(username.value);
						if (xhr.readyState == 4 && xhr.status == 200) {
							//response
							response = this.responseText.trim();
							console.log(response);
							if (response.split('\n')[0] == "yes")
							{
								newuser_dialog.dialog( "close" )

								//username = document.getElementById('username');
								//console.log(user);
								ReloadUserInfo(user,response.split('\n')[1]);
								location.href = "?username=" + encodeURIComponent(username.value) + "&password=" + encodeURIComponent(password.value) + "&flag=" + "2";
							}


						}
					}

					xhr.open("post", UserController, true);
					//xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
					xhr.send();



				} else {	    				
					document.getElementById("alert1").innerHTML = "Account exists.";
				}
			});
		}
		else {
			alert("Two passwords different!");
		}
	}
*/
	function create() {
		var pwd1 = document.getElementById("password1");
		var pwd2 = document.getElementById("password2");
		var username = document.getElementById("username");
		var name = document.getElementById("name");
		var birthday = document.getElementById("birthday");
		var email = document.getElementById("email");
		if (pwd1.value == pwd2.value) {
			//basic validation of input
			re = /^[0-9]+$/;
			if(!re.test(username.value)) {
				alert("Error: Username must contain only numbers!");
				username.focus();
			}
			else if(pwd1.value.length<=5) {
				alert("Error: The length of password must be longer than 5!");
				pwd1.focus();
			}
			else
			{
				//sending request to UserServlet
				var url = ipaddress + "login?usnm="+username.value+"&pswd="+pwd1.value+"&n="+name.value+"&bd="+birthday.value+"&e="+email.value;
				var xhr = new XMLHttpRequest();
				user = username.value;

				xhr.onreadystatechange = function() {
					console.log(username.value);
					if (xhr.readyState == 4 && xhr.status == 200) {
						//response
						response = this.responseText.trim();
						if (response == "yes"){
							console.log(response);
							newuser_dialog.dialog( "close" )
							ReloadUserInfo(user,response.split('\n')[1]);
						}
						else
							alert("The Username is Already Exists!");
					}

				}
				xhr.open("POST", url, true);
    			xhr.send(null);
			}
		}
		else {
			alert("Two passwords different!");
		}
	}

	newuser_dialog = $( "#newuser_dialog-form" ).dialog({
		autoOpen: false,
		width: 320,
		modal: true,
		buttons: {
			"Create": create,
			Cancel: function() {
				newuser_dialog.dialog( "close" );
			}
		},
		close: function() {
			form[ 0 ].reset();
		}
	});

	form = newuser_dialog.find( "form" ).on( "submit", function( event ) {
		event.preventDefault();
	});

	newuser_dialog.dialog( "open" );
	var parent = document.getElementsByClassName('ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close')[1];
	var child = (document.getElementsByClassName('ui-button-text'))[3];
	//console.log(parent);
	//console.log(child);
	parent.removeChild(child);
}

function user_login(){
	var login = document.getElementById("nav-LOGIN");
	var login_dialog;

	function NewUser() {
		login_dialog.dialog( "close" );
		new_user();
	}

	function Login(){
		username = document.getElementById('username1');
		password = document.getElementById('password');

		if (username.value != "" && password.value != "")
		{
			//basic validation of input
			re = /^[0-9]+$/;
			if(!re.test(username.value)) {
				alert("Error: Username must contain only numbers!");
				username.focus();
			}
			else
			{
				//sending request to UserServlet
				var url = ipaddress + "login?usnm="+username.value+"&pswd="+password.value;
				var xhr = new XMLHttpRequest();
				user = username.value;

				xhr.onreadystatechange = function() {
					console.log(username.value);
					if (xhr.readyState == 4 && xhr.status == 200) {
						//response
						response = this.responseText.trim();
						if (response == "yes"){
							console.log(response);
							login_dialog.dialog( "close" )
							console.log(user);
							ReloadUserInfo(user,response.split('\n')[1]);
						}
						else
							alert("The Username or Password is incorrect!");
					}

				}
				xhr.open("GET", url, true);
    			xhr.send(null);
			}
		}
		else
			alert("The Username and Password cannot be empty!");
	}



	login_dialog = $( "#login_dialog-form" ).dialog({
		autoOpen: false,
		width: 350,
		modal: true,
		buttons: {
			"New User": NewUser,
			"Login": Login,
			Cancel: function() {
				login_dialog.dialog( "close" );
			}
		},
		close: function() {
			form[ 0 ].reset();
		}
	});

	form = login_dialog.find( "form" ).on( "submit", function( event ) {
		event.preventDefault();
	});

	login_dialog.dialog( "open" );
	var parent = (document.getElementsByClassName('ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close'))[0];
	var child = (document.getElementsByClassName('ui-button-text'))[0];
	parent.removeChild(child);
}

function user_logout(){
	string = 'Sure to log out ?'; 
	if (confirm(string) == true) {
		localStorage.clear();
		location.reload();
	}
}




