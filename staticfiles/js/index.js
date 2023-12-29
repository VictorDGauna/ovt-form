// TINY EDITOR SCRIPT
// tinymce.init({
//   selector: '#who',
//   branding:false,
//   menubar:false,
//   statusbar: false,
//   toolbar:
//     "forecolor | bold | italic |underline | fullscreen | media | image | emoticons",
//   plugins: "image, emoticons, media , fullscreen, autoresize",
//   max_height: 500,
//   max_width: 800,
//   min_height: 250,
//   min_width: 200, 
  
// });
// 
// ********************VARIABLES*******************
// 
const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

// 
// *******************LOGIC***********************
// 

let formStepsNum = 0;

nextBtns.forEach(btn =>{
    btn.addEventListener("click", ()=>{
        formStepsNum++;
        updateFormSteps();
        updateProgressbar();

    });
});

prevBtns.forEach(btn =>{
    btn.addEventListener("click", ()=>{
        formStepsNum--;
        updateFormSteps();

    });
});

function updateFormSteps(){
    formSteps.forEach((formStep) =>{
        formStep.classList.contains("form-step-active") &&
        formStep.classList.remove("form-step-active");
    });
    formSteps[formStepsNum].classList.add("form-step-active")
}
