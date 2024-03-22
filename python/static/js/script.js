function validate(){
    var isValid=true
    var name = document.getElementById("name").value
    var email = document.getElementById("email").value
    var password = document.getElementById("password").value
    var gender = document.getElementsByName("gender").value 
    var languages = document.querySelectorAll('input[type=checkbox]');   
    var courses = document.getElementById("courses").value
    var comments = document.getElementById("comments").value
    var image = document.getElementById("img").value

    if(name == "" || name == null){
        document.getElementById("name_err").innerHTML = "Name cannot be null."
        isValid = false
    }
    else if(name.match(/^\s*$/)){
        document.getElementById("name_err").innerHTML = "White spaces are not allowed."
    }
    else if(!(isNaN) && name!=""){
        document.getElementById("name_err").innerHTML = "Numericals are not allowed"
        isValid = false
    }
    else{
        document.getElementById("name_err").innerHTML = "";
    }
    if(email=="" || email==null){
        document.getElementById("email_err").innerHTML = "Email cannot be null."
        isValid = false
    }
    else if(!(email.match(regx))){
        document.getElementById("email_err").innerHTML = "Enter correct email format."
        isValid = false
    }
    else{
        document.getElementById("email_err").innerHTML = "";
    }
    if(password == "" || password == null){
        document.getElementById("password_err").innerHTML = "Password cannot be null."
        isValid = false
    }
    else if(password.length>10){
        document.getElementById("password_err").innerHTML = "Max length of password is 10."
        isValid = false
    }
    else{
        document.getElementById("password_err").innerHTML = "";
    }
    if(gender == null || gender == ""){
        document.getElementById("gender_err").innerHTML = "Gender cannot be null."
        isValid = false
    }
    else{
        document.getElementById("gender_err").innerHTML = "";
    }
    if(courses == "" || courses == null){
        document.getElementById("courses_err").innerHTML = "Please select any field."
        isValid = false
    }
    else{
        document.getElementById("courses_err").innerHTML = "";
    }
    var isChecked = false;
    for(var i=0;i<languages.length;i++){
        if(languages[i].checked){
            isChecked = true;
            break;
        }
    }
    if(isChecked == false){
        document.getElementById("languages_err").innerHTML="Please select any value.";
        isValid = false;
    }
    else{
        document.getElementById("languages_err").innerHTML = "";
    }
    if( image==""){
        document.getElementById("img_err").innerHTML = "Please upload image";
        isValid=false;
    }
    
    return isValid
}