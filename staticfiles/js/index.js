
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
    btn.addEventListener("click", (event)=>{
        const formulario = document.querySelector('.form-step-active');
        const inputs = formulario.querySelectorAll('textarea');
        const listInputs = Array.from(inputs);
        const inputs2 = formulario.querySelectorAll('input');
        const listInputs2 = Array.from(inputs2);
        
        
        if (listInputs.length > 0){
            console.log(listInputs);
            listInputs.forEach(input => {
                if (list.includes(input.name) && input.value === ""){
                    console.log(input.name);
                    alert("Please complete this field");
                    input.style.border='2px solid red';
                    input.focus();
                    btn.stopImmediatePropagation();


                }

            });

        }

        if (listInputs.length === 0){
            if (listInputs2.length > 0){
                console.log(listInputs2)
                listInputs2.forEach(input => {
                    
                    if (list.includes(input.name) && input.value === "" ){
                        console.log(input.name);
                        alert("Please complete this field");
                        input.style.border='2px solid red';
                        input.autofocus = true;
                        btn.stopImmediatePropagation()

                    }
                    if (!input.checked && list.includes(input.name) && input.type === 'checkbox'){
                        console.log(input)
                        alert('Please Confirm')
                        btn.stopImmediatePropagation()


                    };
                    if (!input.checked && list.includes(input.name) && input.type === 'radio'){
                        console.log(input)
                        let checkedList = []

                        for (let i = 0; i < listInputs2.length; i++) {
                            if (listInputs2[i].checked) {
                                console.log(listInputs2[i])
                                checkedList.push(listInputs2 [i])
                            }


                        }
                        if (checkedList.length < 1 ){

                            alert('Please Check one Option')
                            btn.stopImmediatePropagation()
                        
                        };


                    };
                    
                return false;    
                });
            }
            
           
        };
        
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





// let isChecked = false;

//             listInputs4.forEach(checkbox => {
//             if (!checkbox.checked && list.includes(checkbox.name)) {
//                 alert("Por favor, completa este campo");
//                 checkbox.style.border = '2px solid red';
//                 checkbox.focus();
//                 isChecked = true;
//             }
//             });

//             // Si no se ha marcado ningún checkbox, muestra la alerta
//             if (!isChecked) {
//                 alert("Por favor, selecciona al menos un checkbox.");
//                 checkbox.preventDefault()
//             }
