/**
 * @param {string} password
 * @return {boolean}
 */
var strongPasswordCheckerII = function(password) {
    
    if (password.length < 8) {
        console.log("returned from lenght: ", password);
        return false;
    }
    
    let checker = {
        'lowercase': false,
        'uppercase': false,
        'digit': false,
        'special': false,
    };
    const specials = "!@#$%^&*()-+".split("");
    let prev = '';
    for (let i=0; i<password.length; i++) {
        const ascii = password[i].charCodeAt();
        // console.log(ascii, password[i]);
        if (prev == password[i]) {
            console.log("returning from prev char: ", password);
            return false;
        }
        if (48 <= ascii && ascii <= 57) {
            // console.log("Entered");
            checker['digit'] = true;
        } else if (65 <= ascii && ascii <= 90) {
            checker['uppercase'] = true;
        } else if (97 <= ascii && ascii <= 122) {
            checker['lowercase'] = true;
        } else if (specials.includes(password[i])) {
            checker['special'] = true;
        } else {
            console.log('unknow char: ', password[i]);
        }
        prev = password[i];
    }
    
    for (const [key, value] of Object.entries(checker)) {
        // console.log(`${key}: ${value}`);
        if (value == false) {
            // console.log('returning from for loop: ', key, password)
            return false;
        }
    }
    return true;
};