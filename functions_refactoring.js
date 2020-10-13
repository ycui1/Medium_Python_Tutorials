function sayHello(name) {
    // Apply some formatting operations
    let name0 = name;
    let name1 = name0;
    let name2 = name1;
    let formattedName = name2;
    console.log("Hello,", formattedName);
}

function sayHi(name) {
    // Apply some formatting operations
    let name0 = name;
    let name1 = name0;
    let name2 = name1;
    let formattedName = name2;
    console.log("Hi,", formattedName);
}

function sayHelloV1(name) {
    let formattedName = formatName(name);
    console.log("Hello,", formattedName);
}

function sayHiV1(name) {
    let formattedName = formatName(name);
    console.log("Hi,", formattedName);
}

function formatName(name) {
    // Apply some formatting operations
    let name0 = name;
    let name1 = name0;
    let name2 = name1;
    return name2;
}

function greet(greetingWord, name) {
    let formattedName = formatName(name);
    console.log(greetingWord + ", " + formattedName);
}

function processData(filename) {
    // 3 lines of code: read the data from the filename
    // 5 lines of code: verify the data structure
    // 10 lines of code: recode some columns
    // 5 lines of code: remove outliers
    // 10 lines of code: do some calculations with the groups
    let results = [];
    return results;
}

function processDataRefactored(filename) {
    let data = readData(filename);
    verifyData(data);
    recodeData(data);
    removeOutliers(data);
    let processedData = summarizeData(data);
    return processedData;
}

function readData(filename) {
    // just a simple list for demonstration purposes
    let data = [1, 2, 3, 4];
    return data;
}

function verifyData(data) {
    // verify the data
}

function recodeData(data) {
    // recode the data
}

function removeOutliers(data) {
    // remove outliers
}

function summarizeData(data) {
    let results = [];
    return results;
}

// This function gets the account information for a user using his/her user id number
function getData(id) {
    // the operations
}

function getUserAccountInfo(userIdNumber) {
    // the operations
}

function createNewUserAccount(username, email, password, phoneNumber, address) {
    let user = {
        "username": username,
        "email": email,
        "password": password,
        "phoneNumber": phoneNumber,
        "address": address
    }
    // create the new user in the database
}

function createNewUserAccount(newUserInfoDict) {
    // create the new user in the database
}

let userInfo = {
    "username": username,
    "email": email,
    "password": password,
    "phoneNumber": phoneNumber,
    "address": address
}
createNewUserAccount(userInfo);

class User {
    constructor(username, email, password) {
        this.username = username;
        this.email = email;
        this.password = password;
    }
}

function createNewUserAccount(newUser) {
    // create the new user in the database
}

let user = new User("username", "email@email.com", "12345678");
user.phoneNumber = "1234567890";
user.address = "123 Main Street";
createNewUserAccount(user);




