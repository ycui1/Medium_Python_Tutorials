function doOperation0(arg0, arg1) {
    if (condition0) {
        // some operation
        return calculatedValue0
    }
    if (condition1) {
        return calculatedValue1
    }
    // some complex operations
    return calculatedValue2
}

function doOperation1(arg0, arg1) {
    var calculatedValue = 0
    if (condition0) {
        // some operations here
        calculatedValue = 2
    } else if (condition1) {
        // some operations here
    } else {
        // some other operations here
        calculatedValue = 100
    }
    return calculatedValue
}

function returnEarly(arg0, arg1) {
    if (condition0) {
        return 5
    }
    if (condition1) {
        return 3
    }
    if (condition2) {
        return 2
    }
    // the big chunk of code
    return 10
}

function returnEnd(arg0, arg1) {
    var value = 0
    if (condition0) {
        // 10 lines of code
        value = 5
    } else if (condition1) {
        // 10 lines of code
        value = 3
    } else {
        // 10 lines of code
        value = 10
    }
    return value
}

var recodedValue
if (oldValue == "a") {
    recodedValue = 0
} else if (oldValue == "b") {
    recodedValue = 1
} else if (oldValue == "c") {
    recodedValue = 2
}



var recodedValue
if (oldValue == "a") {
    recodedValue = 0
} else if (oldValue == "b") {
    recodedValue = 1
} else if (oldValue == "c") {
    recodedValue = 2
} else {
    recodedValue = 999
}

var recodedValue = 999
if (oldValue == "a") {
    recodedValue = 0
} else if (oldValue == "b") {
    recodedValue = 1
} else if (oldValue == "c") {
    recodedValue = 2
}
