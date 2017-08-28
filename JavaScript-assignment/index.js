
function calculateAge() {
    var month = document.getElementById("month").value;
    var day = document.getElementById("day").value;
    var year = document.getElementById("year").value;
  if(month != "" && day != "" && year != "") {
    var dob = new Date(year+'-'+month+'-'+day);
    var todayDate =new Date();
    var age = (todayDate-dob)/31536000000;
    document.getElementById("age").value = age;
    console.log(age)
  }else {
    alert("Please fill the remaining fields");
  }
}

function validateForm() {
    var firstName = document.myForm.firstname.value;
    var lastName= document.myForm.lastname.value;
    var phoneNumber = document.myForm.phone.value;
    var officeNumber = document.myForm.office.value;
    var emailId = document.myForm.email.value;
      var atPosition = emailId.indexOf("@");
      var dotPosition = emailId.lastIndexOf(".");

    var firstPassword = document.myForm.password1.value;
    var secondPassword = document.myForm.password2.value;
    var month = document.getElementById("month").value;
    var day = document.getElementById("day").value;
    var year =  document.getElementById("year").value;

    if (firstName == "" || firstName == null) {
        alert("First Name must be filled out");
        return false;
    }else if (lastName == "" || lastName == null) {
      alert("Last Name must be filled out");
      return false;
    }else if (firstName == lastName) {
      alert("First Name and Last Name should be different!");
      return false;
    }else if (isNaN(phoneNumber)) {
      alert("Enter numeric value only at Phone Number");
      return false;
    }else if (phoneNumber == null || phoneNumber == "") {
      alert("Phone number must be filled out at Phone Number");
      return false;
    }else if (phoneNumber.length>10) {
      alert("Invalid Phone number!");
      return false;
    }else if (isNaN(officeNumber)) {
      alert("Enter numeric value only at office Number");
      return false;
    }else if (atPosition<1 || dotPosition<atPosition+2 || dotPosition+2>=emailId.length) {
      alert("Please enter a valid e-mail address \n atpostion:"+atPosition+"\n dotposition:"+dotPosition);
      return false;
    }else if (firstPassword.length<7 || firstPassword.length >= 12 || firstPassword == "") {
      alert("Password should be in the range of 8 to 12");
      return false;
    }else if (firstPassword != secondPassword) {
       alert("Password must be same!");
      return false;
    }else if (!firstPassword.match(/^[0-9a-zA-Z]+$/)) {
      alert("Alphanumeric characters are only allowed at password");
      return false;
    }else if (firstPassword != secondPassword) {
      alert("Password has to be same")
      return false;
    }else if (month == "select") {
      alert("Please enter the month!");
      return false;
    }else if (day == "select") {
      alert("Please enter the day!");
      return false;
    }else if (year == "select") {
      alert("Please enter the year!");
      return false;
    }else if ((document.myForm.gender1.checked == false) && (document.myForm.gender2.checked == false)) {
      alert("Pleae select your gender!");
      return false;
    }else if ((document.getElementById("checkbox_sample18").checked == false) && (document.getElementById("checkbox_sample19").checked == false) && (document.getElementById("checkbox_sample20").checked == false)) {
      alert("Please Select any 1 interest");
      return false;
    }else if ((document.myForm.About_you.value == "") || (document.myForm.About_you.value == null)){
      alert("Compulsary Fill the About you section!");
      return false;
    }else {
      alert("Form is successfully submitted!");
      return true;
    }
    }