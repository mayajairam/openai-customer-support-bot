# Import necessary libraries
import openai
import os

# go to "https://platform.openai.com/api-keys" to get your api key

# Define OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Handling FAQs for Product Information
def product_information_faq(user_input, conversation):
    product_keywords = ["product", "item", "details", "features", "specifications", "capabilities", "specs", "model"]

    if any(keyword in user_input.lower() for keyword in product_keywords):
        print("Chatbot: Sure! Which smartphone model would you like information about?")
        product_name = input("Product name: ").strip()
        clarified_question = f"Can you provide the key features and technical specifications of the {product_name} smartphone?"
        conversation.append({"role": "user", "content": clarified_question})
        return True

    return False

# Handling FAQs for Shipping and Returns
def shipping_and_returns_faq(user_input, conversation):
    shipping_keywords = ["shipping", "delivery", "courier", "timeline", "track"]
    returns_keywords = ["return", "refund", "exchange", "policy", "cancel"]

    lower_input = user_input.lower()

    if any(word in lower_input for word in shipping_keywords):
        print("Chatbot: I can help with that. What would you like to know about shipping?")
        details = input("Details: ").strip()
        clarified = f"I have a question about shipping: {details}"
        conversation.append({"role": "user", "content": clarified})
        return True

    if any(word in lower_input for word in returns_keywords):
        print("Chatbot: Sure, what would you like to know about our returns or refund policy?")
        details = input("Details: ").strip()
        clarified = f"I have a question about returns: {details}"
        conversation.append({"role": "user", "content": clarified})
        return True

    return False

# Handling FAQs for Customer Support
def customer_support_faq(user_input, conversation):
    keywords = ["help", "issue", "problem", "support", "trouble", "assistance"]

    if any(k in user_input.lower() for k in keywords):
        print("Chatbot: I'd be happy to help! Could you describe your issue in a bit more detail?")
        issue_description = input("Description of issue: ").strip()
        clarified = f"I'm having a problem with my smartphone. {issue_description}"
        conversation.append({"role": "user", "content": clarified})
        return True

    return False

# Build a Customized Chatbot and Chat with It
print("Welcome to our smartphone customer service chatbot. How can I assist you with your smartphone queries today?")

conversation = [
    {"role": "system", "content": "You are a customer service AI knowledgeable about smartphones. Only respond to smartphone-related questions."}
]

while True:
    user_input = input("User: ")

    if user_input.lower() in ["bye", "quit", "exit"]:
        print("Thank you for using our chatbot. Have a great day!")
        break

    # Run clarification functions
    clarification_triggered = False
    clarification_triggered |= customer_support_faq(user_input, conversation)
    clarification_triggered |= shipping_and_returns_faq(user_input, conversation)
    clarification_triggered |= product_information_faq(user_input, conversation)

    # Only add the user's message if no clarification was added
    if not clarification_triggered:
        conversation.append({"role": "user", "content": user_input})

    # 🔥 Now call GPT with the updated conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=150
    )

    chatbot_response = response.choices[0].message.content.strip()

    # Optional off-topic check
    if "smartphone" not in user_input.lower() and "phone" not in user_input.lower() and any(
        phrase in chatbot_response.lower() for phrase in ["sorry", "don't know", "not sure"]):
        print("Chatbot: I'm sorry, I specialize in smartphones. Could you please ask something related to that topic?")
    else:
        print("Chatbot:", chatbot_response)

    conversation.append({"role": "assistant", "content": chatbot_response})