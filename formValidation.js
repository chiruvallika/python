function accountPopupValidation(){
    var acc_name = document.getElementById('acc_name').value;
    var isValid = true;
    if(acc_name==null || acc_name==""){
        document.getElementById('acc_name_err').innerHTML = "Please enter name of the account";
        isValid = false;
    }
    else{
        document.getElementById('acc_name_err').innerHTML = "";
    }
    return isValid;
}

// function mainFormValidation() {
//     var selectedAccount = $('#accounts_dropdown').val();
//     if (selectedAccount === '') {
//         document.getElementById('accounts_dropdown_err').innerHTML = 'Select any account if not present then add an account.';
//         return false; 
//     }
//     return true; 
// }

function empFormValidation(){
    var empname = document.getElementById('empname').value;
    var phone = document.getElementById('phone').value;
    var des = $('#designation_dropdown').val();
    var isValid = true;
    if(empname == null || empname == ""){
        document.getElementById('emp_name_err').innerHTML = "Please enter tour name.";
        isValid = false;
    }
    else if(!(isNaN(empname))){
        document.getElementById('emp_name_err').innerHTML = "Numericals are not allowed.";
        isValid = false;
    }
    else{
        document.getElementById('emp_name_err').innerHTML = "";
    }
    if(phone==null || phone==""){
        document.getElementById('emp_phone_err').innerHTML = "Please enter your number.";
        isValid = false;
    }
    else if(phone.length!=10){
        document.getElementById('emp_phone_err').innerHTML = "Max length is 10.";
        isValid = false;
    }
    else{
        document.getElementById('emp_phone_err').innerHTML = "";
    }
    if(des == ""){
        document.getElementById('designation_dropdown_err').innerHTML = "Please select any designation if not present in list then create one.";
        isValid = false;
    }
    else{
        document.getElementById('designation_dropdown_err').innerHTML = "";
    }
    
    return isValid;
}

function desPopupValidation(){
    var des = document.getElementById('designation').value;
    if(des == null || des == ""){
        document.getElementById('des_err').innerHTML = "Designation cannot be null.";
        return false;
    }
    return true;
}