$(document).ready(function() {
  $(".xyz").change(function() {
    var month = $("#month").val();
    var day = $("#day").val();
    var year = $("#year").val();
      var dob = new Date(year+'-'+month+'-'+day);
      var today = new Date();
      var age = Math.floor((today-dob) / (365.25 * 24 * 60 * 60 * 1000));
      $('#age').val(age+' years old');
});
    $("#register").click(function() {
    var firstName = $("#firstname").val();
    var lastName = $("#lastname").val();
    var phoneNo = $("#phone").val();
    var officeNo = $("#officephone").val();
    var emailId = $("#email").val();
        var atPosition = emailId.indexOf("@");
        var dotPosition = emailId.lastIndexOf(".");
    var password = $("#password1").val();
    var cpassword = $("#password2").val();
    var aboutYou = $("#About_you").val();

    if (firstName == "" || firstName == null || lastName == "" || lastName == null ) {
      alert ("Please fill your firstname or lastname");
      return false;
    }else if (firstName == lastName) {
      alert ("First name and Last name must be different!");
      return false;
    }else if (isNaN(phoneNo)) {
      alert ("Enter numeric value only at Phone Number");
      return false;
    }else if (phoneNo == null || phoneNo == "") {
      alert("Phone number must be filled out at Phone Number");
      return false;
    }else if (phoneNo.length>10) {
      alert("Invalid Phone number!");
      return false;
    }else if (isNaN(officeNo) || officeNo == "" || officeNo == null) {
      alert("Office number must be filled correectly!");
      return false;
    }else if (atPosition<1 || dotPosition<atPosition+2 || dotPosition+2>=emailId.length) {
      alert("Please enter a valid e-mail address");
      return false;
    }else if (password.length<7 || password.length >= 12 || password == "") {
      alert("Password should be in the range of 8 to 12");
      return false;
    }else if (cpassword == "" || cpassword == null) {
      alert("Re-enter the Password!");
      return false;
    }else if (password != cpassword) {
       alert("Password must be same!");
      return false;
    }else if (!password.match(/^[0-9a-zA-Z]+$/)) {
      alert("Alphanumeric characters are only allowed at password");
      return false;
    }else if (password != cpassword) {
      alert("Password has to be same");
      return false;
    }else if (month == "select") {
      alert("Please enter the month!");
      return false;
    }else if (day == "select") {
      alert("Please enter the day!");
      return false;
    }else if (year == "") {
      alert("Please enter the year!");
      return false;
    }else if ($('input[name=gender]:checked').length<=0) {
      alert("Please select your gender!");
      return false;
    }else if ($('input[name=interests]:checked').length<=0) {
      alert("Please select any 1 of the interests!");
      return false;
    }else if (aboutYou == "" || aboutYou == null) {
      alert ("\"About you\" section must be filled");
      return false;
    }else {
      alert ("Form submitted successfully");
      return true;
    }
    });
});

