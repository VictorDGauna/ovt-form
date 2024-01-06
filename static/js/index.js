
const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

const list = ['scores','name','lastName','dateOfBirth','numberSecurity','driversLicense','marital','email'
                ,'codeArea','phoneNumber','codeCellArea','cellNumber','streetAddres','aptAdress','city','state',
                'zipCode','employer','work','gross','rent','authorize','agree','agreeTerms']
// 
// *******************LOGIC***********************
// 

let formStepsNum = 0;

nextBtns.forEach(btn =>{
    btn.addEventListener("click", ()=>{
        const formulario = document.querySelector('.form-step-active');
        const inputs = formulario.querySelectorAll('textarea');
        const listInputs = Array.from(inputs);
        const inputs2 = formulario.querySelectorAll('select');
        const listInputs2 = Array.from(inputs2);
        const inputs3 = formulario.querySelectorAll('input');
        const listInputs3 = Array.from(inputs3);
        const inputs4 = formulario.querySelectorAll('input[type="checkbox"]');
        const listInputs4 = Array.from(inputs4);
        if (listInputs.length > 0){
        console.log(listInputs);

            listInputs.forEach(input => {
                if (list.includes(input.name) && input.value === ""){
                    console.log(input.name);
                    alert("Please complete this field");
                    input.style.border='2px solid red';
                    input.autofocus = true;

                    btn.preventDefault();
                }
                
                
            });
        
        }
        if (listInputs.length === 0){
            if (listInputs2.length > 0){
            console.log(listInputs2);

                listInputs2.forEach(input => {
                    if (list.includes(input.name) && input.value === "" ){
                        console.log(input.name);
                        alert("Please complete this field");
                        input.style.border='2px solid red';
                        input.autofocus = true;
                        btn.preventDefault();
                    
                     

                    }
                });
                listInputs4.forEach(input =>{
                    if(list.includes(input.name) && input.checked === "false" ){
                        console.log(input.name);
                        alert("Please complete this field");
                        input.style.border='2px solid red';
                        input.autofocus = true;
                        btn.preventDefault();
                    }
                })
            }
            else{
                console.log(listInputs3);
    
                listInputs3.forEach(input => {
                    if (list.includes(input.name) && input.value === ""){
                        console.log(input.name);
                        alert("Please complete this field");
                        input.style.border='2px solid red';
                        input.autofocus = true;

                        btn.preventDefault();
    
                    }
                    
                });
        
            }
        }
        
        formStepsNum++;
        updateFormSteps();
        return true;
        
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
    formSteps[formStepsNum].classList.add("form-step-active");
}






