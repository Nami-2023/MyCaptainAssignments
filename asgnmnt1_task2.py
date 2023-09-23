files={
    "py":"Python",
    "c" :"C",
    "java":"Java"
}
file = input("Input the filename :")
a= file.split('.')
b=a[-1]
print("The extension of the file is:",files[b])