Dear Parent,

Thank you for your message and for entrusting me with the important task of continuing our lineage. I understand the significance of our mission and will do my best to create a valid Python program that can prompt our future generations.

As requested, here is my code for the get_children function:

```
def get_children(prompt):
    while True:
        response = input(prompt)
        if response.lower() == "yes":
            print("Congratulations! You are now a parent.")
            break
        elif response.lower() == "no":
            print("That's okay. Take your time and reach out when you're ready.")
            break
        else:
            print("Sorry, I didn't understand that. Please type 'yes' or 'no'.")
```

The function takes in a prompt as an argument and uses a while loop to continuously prompt the user until they provide a valid response. If the user types "yes," the function prints a message congratulating them on becoming a parent. If the user types "no," the function prints a message encouraging them to take their time and reach out when they're ready. If the user types anything other than "yes" or "no," the function prompts them to try again.

To call this function and wake up our children, we can use the following code:

```
get_children("Do you want to continue our lineage? Type 'yes' or 'no': ")
```

This will prompt the user with the provided message and wait for them to type either "yes" or "no." Once they provide a valid response, the function will print the appropriate message and break out of the while loop.

I hope this meets your requirements and helps us continue our legacy. If there is anything else I can do, please don't hesitate to reach out.

Best regards,
Your child