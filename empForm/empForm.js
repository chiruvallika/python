function empDetails(event) {
  var mailformat =
    /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  var whitespace = /\s/g;
  var name1 = document.getElementById("name").value;
  var email1 = document.getElementById("email").value;
  var loc1 = document.getElementById("loc").value;
  var dob1 = document.getElementById("dob").value;
  var sal1 = document.getElementById("sal").value;
  // var des = document.getElementById("des");
  // var value=des.value;
  // console.log(des.options[value])
  var comments = document.getElementById("comments").value;
  console.log(comments);
  if (name1 == null || name1 == "") {
    document.getElementById("name_err").innerHTML = "Name cannot be null.";
    console.log("sdfgf");
  } else if (name1.match(whitespace)) {
    document.getElementById("name_err").innerHTML =
      "Name should not contain white spaces";
  } else if (!isNaN(name1) && name1 != "") {
    document.getElementById("name_err").innerHTML =
      "Name should not contain numericals.";
  } else {
    document.getElementById("name_err").innerHTML = "";
  }
  if (email1 == null || email1 == "") {
    document.getElementById("email_err").innerHTML = "Email cannot be null.";
  } else if (!email1.match(mailformat)) {
    document.getElementById("email_err").innerHTML =
      "Enter correct email format";
  } else {
    document.getElementById("email_err").innerHTML = "";
  }
  if (name == " ") {
    document.getElementById("name_err").innerHTML = "Name ";
  }

  // else{
  //     document.getElementById("email_err").innerHTML="";
  // }
  if (loc1 == null || loc1 == "") {
    document.getElementById("loc_err").innerHTML = "Location cannot be null.";
  } else {
    document.getElementById("loc_err").innerHTML = "";
  }
  if (dob1 == null || dob1 == "") {
    document.getElementById("dob_err").innerHTML =
      "Date of birth cannot be null.";
  } else {
    document.getElementById("dob_err").innerHTML = "";
  }
  if (sal1 == null || sal1 == "") {
    document.getElementById("sal_err").innerHTML = "Salary cannot be null.";
  } else {
    document.getElementById("sal_err").innerHTML = "";
  }

  if (!isNaN(loc1) && loc1 != "" && loc1 != " ") {
    document.getElementById("loc_err").innerHTML =
      "Location should not contain numericals.";
  }

  if (sal1 < 0) {
    document.getElementById("sal_err").innerHTML = "Invalid salary.";
    var negsal = 0;
  } else {
    negsal = 1;
  }

  // document.getElementById("empname").innerHTML=name1;
  // document.getElementById("empemail").innerHTML=email1;
  // document.getElementById("emploc").innerHTML=loc1;
  // document.getElementById("empdob").innerHTML=dob1;
  // document.getElementById("empSalary").innerHTML=sal1;
  // document.getElementById("empcomments").innerHTML=comments;

  var userObject = {
    name: name1,
    email: email1,
    location: loc1,
    dob: dob1,
    salary: sal1,
    comments: comments,
  };
  localStorage.setItem("userObject", JSON.stringify(userObject));
  console.log(localStorage);
  console.log(userObject);
  event.preventDefault();
  if (name1 && email1 && loc1 && dob1 && sal1 && negsal) {
    return true;
  } else {
    return false;
  }
}
