function displayPrompt() {
  var result = prompt("Enter some text:");
  if (result != null) {
    alert("You entered: " + result);
  }
  return false;
}
