from simple_chatbot.responses import GenericRandomResponse
print("chebra chebra")

class GreetingResponse(GenericRandomResponse):
    choices = ("Hey, how can I help you?",
               "Hey friend. How are you? How can I help you?",
               "Good, How can I help you?")


class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.",
               "Thanks for visiting.",
               "See ya! Have a nice day.")

class ProductInformationResponse(GenericRandomResponse):
    choices = (
        "Would you like to buy our product?", 
        "Would you like to get some information about our products?",
    )

class UnableToAnswer(GenericRandomResponse):
    choices = (
        "System is unable to reply your message.",
    )