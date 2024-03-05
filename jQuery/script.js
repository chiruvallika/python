$(document).ready(function () {
  var employeeData = [];
  $("#employeeForm").submit(function (event) {
    event.preventDefault();
    if (validateForm()) {
      var formData = $(this).serializeArray();
      var employeeDetails = {};
      formData.forEach(function (input) {
        employeeDetails[input.name] = input.value;
      });
      employeeData.push(employeeDetails);
      updateTotalPages();
      displayEmployeeDetails();
      // resetForm();
    }
  });

  function validateForm() {
    var isValid = true;
    $('#employeeForm input[type="text"]').each(function () {
      $(this).next(".error-message").remove();
      if ($(this).val() === "") {
        isValid = false;
        $(this).addClass("error");
        $(this).after(
          '<div class="error-message">This field is required</div>'
        );
      } else {
        $(this).removeClass("error");
      }
    });

    var email = $("#empEmail").val();
    if (email !== "") {
      var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        isValid = false;
        $("#empEmail").addClass("error");
        $("#empEmail").after(
          '<div class="error-message">Invalid email format</div>'
        );
      } else {
        $("#empEmail").removeClass("error");
      }
    }

    var phone = $("#empPhone").val();
    if (phone !== "") {
      var phonePattern = /^\d{10}$/;
      if (!phonePattern.test(phone)) {
        isValid = false;
        $("#empPhone").addClass("error");
        $("#empPhone").after(
          '<div class="error-message">Phone number must be 10 digits</div>'
        );
      } else {
        $("#empPhone").removeClass("error");
      }
    }

    var dob = $("#empDOB").val();
    if (dob !== "") {
      var dobPattern = /^\d{4}-\d{2}-\d{2}$/;
      if (!dobPattern.test(dob)) {
        isValid = false;
        $("#empDOB").addClass("error");
        $("#empDOB").after(
          '<div class="error-message">Invalid date format (YYYY-MM-DD)</div>'
        );
      } else {
        $("#empDOB").removeClass("error");
      }
    }

    var salary = $("#empSalary").val();
    if (salary !== "") {
      var salaryPattern = /^\d+(\.\d{1,2})?$/;
      if (!salaryPattern.test(salary)) {
        isValid = false;
        $("#empSalary").addClass("error");
        $("#empSalary").after(
          '<div class="error-message">Invalid salary format</div>'
        );
      } else {
        $("#empSalary").removeClass("error");
      }
    }

    return isValid;
  }

  $("#resetBtn").click(function () {
    console.log("resert click");
    $("#employeeForm")[0].reset();
    $(".error-message").remove();
    $("#employeeForm input").removeClass("error");
  });

  var page_number = 1;
  var records_per_page;
  var total_pages;
  var e = document.getElementById("table-size").value;
  console.log(e);
  records_per_page = parseInt(e);

  function updateTotalPages() {
    total_pages = Math.ceil(employeeData.length / records_per_page);
  }

  function displayPagination() {
    console.log("total pahes" + total_pages);
    console.log("pagination");
    var pagination = $("#pagination");
    pagination.empty();
    var prevBtn = '<button id="prevBtn">Prev</button>';
    pagination.append(prevBtn);
    for (var i = 1; i <= total_pages; i++) {
      var pageBtn = '<button class="pageBtn">' + i + "</button>";
      pagination.append(pageBtn);
    }
    var nextBtn = '<button id="nextBtn">Next</button>';
    pagination.append(nextBtn);

    $("#prevBtn").click(function () {
      console.log("prev");
      if (page_number > 1) {
        page_number--;
        displayEmployeeDetails();
      }
    });

    $(".pageBtn").click(function () {
      page_number = parseInt($(this).text());
      displayEmployeeDetails();
    });

    $("#nextBtn").click(function () {
      if (page_number < total_pages) {
        page_number++;
        displayEmployeeDetails();
      }
    });
  }

  function displayEmployeeDetails() {
    console.log("hello");
    var tableBody = $("#employeeTableBody");
    var start_index = (page_number - 1) * records_per_page;
    var end_index = start_index + records_per_page;
    end_index = Math.min(end_index, employeeData.length);
    tableBody.empty();
    for (var i = start_index; i < end_index; i++) {
      var row = "<tr>";
      row += "<td>" + employeeData[i].empID + "</td>";
      row += "<td>" + employeeData[i].empName + "</td>";
      row += "<td>" + employeeData[i].empPosition + "</td>";
      row += "<td>" + employeeData[i].empDepartment + "</td>";
      row += "<td>" + employeeData[i].empEmail + "</td>";
      row += "<td>" + employeeData[i].empPhone + "</td>";
      row += "<td>" + employeeData[i].empAddress + "</td>";
      row += "<td>" + employeeData[i].empDOB + "</td>";
      row += "<td>" + employeeData[i].empSalary + "</td>";
      row += "</tr>";
      tableBody.append(row);
    }

    displayPagination();
  }
});
