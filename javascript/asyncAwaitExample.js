function timeoutPromise(interval, msg) {
    return new Promise((resolve, reject) => {
        setTimeout(function () {
            console.log("Loop " + msg);
            resolve(msg);
        }, interval);
    });
};

console.log("----- async await example -----")
timeoutPromise(2000, '1')
    .then(val => timeoutPromise(1000, val + 1))
    .then(val => timeoutPromise(1000,val + 1));

console.log("************* Done *************")
