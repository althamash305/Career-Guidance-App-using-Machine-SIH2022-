function getInputValue() {
  let exam = document.getElementById("exam").value;
  let marks = document.getElementById("marks").value;
  let result;

  switch (exam) {
    case "JEE":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 75000;
        else if(marks < 150) result = 75000;
        else if(marks < 150) result = 75000;
        else if(marks < 150) result = 75000;
        else if(marks < 150) result = 75000;
        break;

    case "NEET":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;

    case "UPSC":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;

    case "BITS":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;

    case "CET":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;

    case "COMED-K":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;

    case "IBPS":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;

    case "SBI":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;

      case "AIEEE":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;
  
      case "AIMS":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;
  
      case "CMC":
        if (marks < 100) result = 70000;
        else if(marks < 150) result = 65000;
        else if(marks < 200) result = 60000;
        else if(marks < 250) result = 55000;
        else if(marks < 300) result = 50000;
        else if(marks < 350) result = 45000;
        break;
  }

  document.getElementById("result").innerHTML = result;
}
