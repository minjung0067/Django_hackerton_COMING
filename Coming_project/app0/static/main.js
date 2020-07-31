// alert( 'Lorem ipsum dolor' );

// Get the modal
var modal = document.querySelector('.modal');
        
 // Get the button that opens the modal
var Btn = document.querySelectorAll(".Btn");
console.log(Btn);

var button = document.getElementsByClassName("Btn");
console.log(button);


function show() {
    var id = $(this).getAttribute('id');
alert(id);
    console.log(id);

};

// for(var i = 0; i<Btn.length; i++ ){
//     Btn[i].onclick = function(){
//         Btn[i].nextElementSibling.classList.toggle('hide');
//     }
// }


var classNum = document.querySelectorAll("#myModal");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];                                          

 // When the user clicks on the button, open the modal 

 //  Btn.onclick = function() 
// { modal.style.display = "block";
// }

 // When the user clicks on <span> (x), close the modal
span.onclick = function() {
modal.style.display = "none";
}

 // When the user clicks anywhere outside of the modal, close it
 window.onclick = function(event) {
     if (event.target == modal) {
         modal.style.display = "none";
     }
 }