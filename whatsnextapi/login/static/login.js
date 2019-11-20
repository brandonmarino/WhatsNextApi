function login() {
    const usernameElement = document.getElementById('username');
    const passwordElement = document.getElementById('password');
    
    const username = usernameElement.value;
    const password = passwordElement.value;

    // get basePath of current site
    const basePath = window.location.href.split('auth')[0];
    const loginUrl = `${basePath}auth/token/`;

    const url = new URL(window.location.href);
    const redirectUrl = url.searchParams.get('redirect_url');

    postCredentials(loginUrl, username, password).then((response) => {
        // navigate to the post login redirect url
        if (redirectUrl != null && typeof redirectUrl == 'string') {
            window.location.href = redirectUrl + `#access_token=${response['access']},refresh_token=${response['refresh']}`;
        }
    }, error => {
        console.error(error);
        alert('Username or password is incorrect');
        passwordElement.value = '';
    });
}

function postCredentials(loginUrl, username, password) {
    return new Promise((resolve, reject) => {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", loginUrl, true);
        
        var formData = new FormData();
        formData.append("username", username);
        formData.append("password", password);

        xhr.onreadystatechange = function () {
            if (this.readyState != 4) return;
        
            if (this.status == 200) {
                var data = JSON.parse(this.responseText);
                resolve(data);
            } else {
                reject(this);
            }
        };

        xhr.send(formData);
    });
}