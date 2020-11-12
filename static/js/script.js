const student_dob = document.getElementById('sdate_of_birth')
const form = document.getElementById('student_form')
const errormsg = document.getElementById('error_message')

form.addEventListener('submit'), (e) => {
    let messages = []
    if (student_dob.value.length <= 8) {
        messages.push('Please type correct value - DDMMYYYY')
    }

    if (student_dob.value.length >= 8) {
        messages.push('Invalid birthdate. Please type correct value - DDMMYYYY')
    }

    if (message.length > 0) {
        e.preventDefault()
        errormsg.innerText = messages.join(', ')  
    }
}