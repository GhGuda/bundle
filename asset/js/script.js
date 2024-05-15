const typed = new Typed('.multiple-text', {
    strings: ['MTN','Telecel(Vodaphone)', "AirtelTigo"],
    typeSpeed: 120, // Adjust speed as needed
    loop: true
  });

  


  var toggler = document.querySelector('.toggler');
  var main = document.querySelector('.navLinks');
  toggler.addEventListener('click', function(event) {
      event.stopPropagation(); // Prevent body click event from being triggered
      main.classList.toggle('navLinks-active');
  });

  // Add event listener to the body element to close the menu when clicked outside of it
  document.body.addEventListener('click', function() {
      main.classList.remove('navLinks-active');
  });

  // Prevent the body click event from being triggered when clicking inside the navigation menu
  main.addEventListener('click', function(event) {
      event.stopPropagation();
  });







   // Get references to the input elements
   var amountInput = document.getElementById('amountInput');
   var bundleInput = document.getElementById('bundleInput');
   var bundleDiv = document.querySelector('.bundle');

   // Add event listener to the amount input
   amountInput.addEventListener('input', function() {
       // Calculate the bundle amount (input value multiplied by 3)
       var bundleAmount = parseInt(amountInput.value) * 3;

       // Check if bundle amount is less than 1000 or not
        if (bundleAmount <= 99) {
        // If less than 1000, attach "GB"
        bundleInput.value = "Please enter amount above GH₵ 99";
        }
         else if (bundleAmount < 1000) {
           // If less than 1000, attach "GB"
           bundleInput.value = bundleAmount + " GB (Non-Expire)";
        }
        else if (bundleAmount > 1000) {
           // If less than 1000, attach "GB"
           bundleInput.value = (bundleAmount / 1000) + " TB (Valid for 3 months)";
        } else {
           // If more than or equal to 1000, attach "TB"
           bundleInput.value = "Please enter amount above GH₵ 99";
        }

       // Show the bundle div if the input value is above 100
       if (parseInt(amountInput.value) > 99) {
           bundleDiv.style.display = 'initial';
       }else {
           bundleDiv.style.display = 'none';
       }
   });