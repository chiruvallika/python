function validate(){
    console.log("hiii")
    var name = document.getElementById("name").value;
    var contact = document.getElementById("contact").value;
    var gender = document.getElementsByName("gender");
    var isValid = true;
    if(name == "" || name == null){
        document.getElementById("name_err").innerHTML = "Name cannot be null."
        isValid = false
    }
    else if(name.match(/^\s*$/)){
        document.getElementById("name_err").innerHTML = "White spaces are not allowed."
        isValid = false;
    }
    else if(!(isNaN) && name!=""){
        document.getElementById("name_err").innerHTML = "Numericals are not allowed"
        isValid = false
    }
    else{
        document.getElementById("name_err").innerHTML = "";
    }
    var ischecked = false;
    console.log(gender)
    for(var i=0;i<gender.length;i++){
        console.log(gender[i].checked)
        if(gender[i].checked==true){
            ischecked=true;
            break;
        }
    }
    if(ischecked==false){
        document.getElementById("gender_err").innerHTML = "Select your gender."
        isValid=false;
    }
    else{
        document.getElementById("gender_err").innerHTML="";
    }
    if(contact == null || contact == ""){
        document.getElementById('contact_err').innerHTML = "Contact cannot be null."
        isValid = false
    }
    else if(contact.length!=10){
        document.getElementById('contact_err').innerHTML = 'Max length is 10.';
        isValid = false
    }
    else{
        document.getElementById('contact_err').innerHTML = '';
    }
    return isValid;
}