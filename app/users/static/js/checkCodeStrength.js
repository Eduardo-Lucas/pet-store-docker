function checkCodeStrength() {
  const codeInput = document.getElementById("code");
  const code = codeInput.value.trim();

  const lengthMessage = document.getElementById("lengthMessage");
  const lowercaseMessage = document.getElementById("lowercaseMessage");
  const uppercaseMessage = document.getElementById("uppercaseMessage");
  const specialCharMessage = document.getElementById("specialCharMessage");

  lengthMessage.textContent =
    code.length === 8
      ? "Code length is valid."
      : "Code must be exactly 8 characters long.";
  lengthMessage.style.color = code.length === 8 ? "green" : "red";

  lowercaseMessage.textContent = code.match(/[a-z]/)
    ? "Contains at least one lowercase letter."
    : "Code must contain at least one lowercase letter.";
  lowercaseMessage.style.color = code.match(/[a-z]/) ? "green" : "red";

  uppercaseMessage.textContent = code.match(/[A-Z]/)
    ? "Contains at least one uppercase letter."
    : "Code must contain at least one uppercase letter.";
  uppercaseMessage.style.color = code.match(/[A-Z]/) ? "green" : "red";

  specialCharMessage.textContent = code.match(/[!@#$%^&*()_+{}\[\]:;<>,.?~]/)
    ? "Contains at least one special character."
    : "Code must contain at least one special character (!@#$%^&*()_+{}[]:;<>,.?~)";
  specialCharMessage.style.color = code.match(/[!@#$%^&*()_+{}\[\]:;<>,.?~]/)
    ? "green"
    : "red";
}
