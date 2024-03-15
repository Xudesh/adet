const ProfileBtn = document.getElementById('profile');
const ChevronDown = document.getElementById('chevron-down');
const DropDownMenu = document.getElementById('dropdown-menu');
const ToggleMenuBtn = document.getElementById('toggle-btn');
const HeaderMenu = document.querySelector('#header-menu');


let password = document.querySelector('.password');
let password1 = document.querySelector('.password1');
let password2 = document.querySelector('.password2');

let eye = document.getElementById('login-eye')
let eye1 = document.getElementById('eye1');
let eye2 = document.getElementById('eye2');


eye?.addEventListener('click', () => {
    if(password.type == 'password'){
        
        password.type = 'text'

    }
    else{
        password.type = 'password'

    }

    eye.classList.toggle('hide')

})



eye1?.addEventListener('click', () => {
    if(password1.type == 'password'){
        
        password1.type = 'text'

    }
    else{
        password1.type = 'password'

    }

    eye1.classList.toggle('hide')

})

eye2?.addEventListener('click', () => {
    if(password2.type == 'password'){
        
        password2.type = 'text'

    }
    else{
        password2.type = 'password'

    }
    
    eye2.classList.toggle('hide')

})



ProfileBtn?.addEventListener('click', () => {
    ChevronDown.classList.toggle('active');

    DropDownMenu.classList.toggle('active')
})



ToggleMenuBtn?.addEventListener('click', ()=> {
    HeaderMenu.classList.toggle('active')
})