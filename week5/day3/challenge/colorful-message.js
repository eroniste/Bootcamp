const chalk = require('chalk');
function showMessage() {
    console.log(chalk.green.bold('This is your colorful message for the day!'));
}
module.exports = showMessage;