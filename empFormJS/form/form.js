function validate(e) {
  //   e.preventDefault();
  console.log("hello");
  //   return false;
  //   debugger;
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var phone = document.getElementById("phone").value;
  var password = document.getElementById("password").value;
  var confirmpassword = document.getElementById("confirmpassword").value;
  var f = 0;
  if (name == null || name == "") {
    document.getElementById("name_error").innerHTML = "Name cannot be null";
  } else if (name.length > 10) {
    f = 1;
    document.getElementById("name_error").innerHTML = "Max length is 10";
  } else if (!isNaN(name) && name != "") {
    document.getElementById("name_error").innerHTML =
      "Name should not contain number";
  } else {
    document.getElementById("name_error").innerHTML = "";
  }
  if (email == null || email == "") {
    document.getElementById("email_error").innerHTML = "Email cannot be null";
  } else if (email.length > 20) {
    f = 1;
    document.getElementById("email_error").innerHTML =
      "Max length of email is 20";
  } else {
    document.getElementById("email_error").innerHTML = "";
  }
  if (phone == null || phone == "") {
    document.getElementById("phone_error").innerHTML =
      "Phone number cannot be null";
  } else if (phone.length != 10) {
    document.getElementById("phone_error").innerHTML = "Not a valid number";
  } else {
    document.getElementById("phone_error").innerHTML = "";
  }
  if (password == null || password == "") {
    document.getElementById("password_error").innerHTML =
      "Password cannot be null";
  } else if (password.length < 10 || confirmpassword.length < 10) {
    f = 1;
    document.getElementById("mismatch_error").innerHTML =
      "Min length of password is 10";
  } else {
    document.getElementById("password_error").innerHTML = "";
  }
  if (confirmpassword == null || confirmpassword == "") {
    document.getElementById("confpassword_error").innerHTML =
      "Password cannot be null";
  } else {
    document.getElementById("confpassword_error").innerHTML = "";
  }

  if (password != confirmpassword) {
    console.log("mismatch");
    document.getElementById("mismatch_error").innerHTML = "Password mismatched";
  } else {
    document.getElementById("mismatch_error").innerHTML = "";
  }

  if (name && email && phone && password && confirmpassword && f == 0) {
    console.log("if");
    document.getElementById("user_name").innerHTML = name;
    document.getElementById("user_email").innerHTML = email;
    document.getElementById("user_phone").innerHTML = phone;
  } else {
    return false;
  }
  //   else {
  //     return false;
  //   }

  console.log("hi");

  console.log(name);
}

function resetClick(e) {
  console.log("hello hii");
  document.getElementById("name").value = "";
  document.getElementById("email").value = "";
  document.getElementById("number").value = "";
  document.getElementById("password").value = "";
  document.getElementById("conformpassword").value = "";
  e.preventDefault();
}
