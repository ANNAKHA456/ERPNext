frappe.ready(function() {
    fetch('http://demo01.com:8003/api/method/frappe.auth.get_logged_user', {
        headers: {
            'Authorization': 'd1678c54ddcd0ca:b71946d24757534'
        }
    })
    .then(r => r.json())
    .then(r => {
        console.log(r);
    });
});
