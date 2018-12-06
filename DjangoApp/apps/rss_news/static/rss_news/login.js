document.querySelector('#check_name_btn').addEventListener('click', _ => {
    fetch('check_user_name?' + `user_name=${document.querySelector('#user_name_input').value.trim()}`, {
    method: "get",
})
    .then(res => res.text())
    .then(res => {
        console.log(res);
        if (res === 'yes') {

        } else if (res === 'no') {

        }
    });
})