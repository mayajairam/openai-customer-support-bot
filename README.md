# 📱 openai-customer-support-bot

A modular, interactive customer service chatbot built in Python using the OpenAI GPT-3.5 API. This bot handles product inquiries, customer support issues, and shipping/returns questions — all focused on smartphones. It's a clean example of conversational AI using prompt engineering, keyword-based routing, and natural clarification flow.

---

## 💡 Features

- 🤖 **Conversational AI** using OpenAI's `gpt-3.5-turbo` model  
- 🔍 **Intent detection** via keyword matching for smart routing  
- 🔁 **Clarification flow** for vague or incomplete user questions  
- 🧠 **Prompt engineering** to guide assistant tone and scope  
- 🧩 **Modular FAQ functions** for product, support, and shipping  
- 📚 **Expandable** architecture — easy to add new topics or use cases

---

## 🛠️ How It Works

1. The user enters a query.
2. The bot checks if the query relates to:
   - 📦 Shipping or returns  
   - 📞 Support issues  
   - 📱 Product specifications  
3. If clarification is needed (e.g., "I need help"), the bot collects more info.
4. The refined question is passed to the OpenAI Chat API for a full response.
5. The chatbot responds in a friendly, smartphone-specialist tone.

---