function showPassword(e) {
    const field_password = e.parentNode

    const password_input = field_password.querySelector('input')
    const password_button = field_password.querySelector('.visibility')

    const type = password_input.getAttribute('type') === 'password' ? 'text' : 'password'

    const type_icone = type === 'password' ? 'visibility' : 'visibility_off'
    password_button.textContent = type_icone

    password_input.setAttribute('type', type)
}