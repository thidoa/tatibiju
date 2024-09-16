function showPassword() {
    const password_input = document.getElementById('password')
    const password_button = document.getElementById('button_password')
    const type = password_input.getAttribute('type') === 'password' ? 'text' : 'password'

    const type_icone = type === 'password' ? 'visibility' : 'visibility_off'
    password_button.textContent = type_icone

    password_input.setAttribute('type', type)
}