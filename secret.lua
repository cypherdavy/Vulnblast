-- Write the secret code to a file
local secretCode = "This is a secret code!"
local file = io.open("secret.txt", "w")
file:write(secretCode)
file:close()

-- Read the secret code from the file
file = io.open("secret.txt", "r")
secretCode = file:read("*a")
file:close()

-- Print the secret code
print(secretCode)
