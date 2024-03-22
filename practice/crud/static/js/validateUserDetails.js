function validate(){
    console.log("hello");
    var isValid = true;
    var regx = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
    var email = document.getElementById("email").value;
    var contact = document.getElementById("contact").value;
    var name = document.getElementById("name").value;
    var contact = document.getElementById("contact").value;
    var gender = document.getElementsByName("gender");
    var language = document.querySelectorAll('input[name="language"]:checked');

    if(name == "" || name == null){
        document.getElementById("name_err").innerHTML = "Name cannot be null.";
        isValid = false;
    }
    else if(name.match(/^\s*$/)){
        document.getElementById("name_err").innerHTML = "White spaces are not allowed.";
        isValid = false;
    }
    else if(!(isNaN) && name!=""){
        document.getElementById("name_err").innerHTML = "Numericals are not allowed";
        isValid = false;
    }
    else{
        document.getElementById("name_err").innerHTML = "";
    };

    var isselect = false;
    console.log(gender);
    for(var i=0;i<gender.length;i++){
        console.log(gender[i].checked)
        if(gender[i].checked==true){
            isselect=true;
            break;
        };
    };
    if(isselect==false){
        document.getElementById("gender_err").innerHTML = "Select your gender."
        isValid=false;
    }
    else{
        document.getElementById("gender_err").innerHTML="";
    };
    
    if(contact == "" || contact == null){
        document.getElementById("contact_err").innerHTML = "Contact cannot be null."
        isValid = false;
    }
    else if(contact.length!=10){
        document.getElementById('contact_err').innerHTML = 'Max length is 10.';
        isValid = false;
    }
    else{
        document.getElementById("contact_err").innerHTML = "";
    };
    console.log(isValid)
    if(email=="" || email==null){
        document.getElementById("email_err").innerHTML = "Email cannot be null."
        isValid = false;
    }
    else if(!(email.match(regx))){
        document.getElementById("email_err").innerHTML = "Enter correct email format."
        isValid = false;
    }
    else{
        document.getElementById("email_err").innerHTML = "";
    };

    if (language.length === 0) {             
        document.getElementById("languages_err").innerHTML="Please select any value.";
        isValid = false;         
    }
    else{
        document.getElementById("languages_err").innerHTML = "";
    }

    // // var selected = []
    // var isChecked = false;
    // for(var i=0;i<languages.length;i++){
    //     if(languages[i].checked){
    //         isChecked = true;
    //         break;
    //         // selected.push(languages[i].value)
    //     };
    // };
    // if(isChecked == false){
    //     document.getElementById("languages_err").innerHTML="Please select any value.";
    //     isValid = false;
    // }
    // else{
    //     document.getElementById("languages_err").innerHTML = "";
    // };
    return isValid;

}