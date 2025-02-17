<h1>🌟 AI Fashion Assistant - Personal Online Shopping Agent 👗🛍️</h1>

<p>Welcome to the AI Fashion Assistant repository! This project demonstrates an intelligent assistant capable of helping users with their online shopping experience across various e-commerce platforms. By utilizing agentic reasoning and tool use, this assistant provides personalized assistance for fashion shopping, helping users find products, compare prices, calculate shipping, and even apply discount codes. ✨</p>

<hr>

<h2>📑 Table of Contents</h2>

<ul>
  <li>
    🌟 Overview
🔧 Features
⚙️ Installation
🖥️ Usage
🤖 Agent Workflow
🛠️ Tools Implementation
🚧 Challenges and Improvements
🔮 Future Work
📝 License
  </li>
</ul>

<hr>


<h2>🌟 Overview</h2>

<p>The AI Fashion Assistant is built to help users find fashion items across multiple online e-commerce platforms, compare prices, and validate shipping deadlines. It also checks for available discount codes and evaluates return policies to ensure users make well-informed decisions. 💡

This assistant is driven by a language model, allowing it to reason and make decisions on which external tools to use in different scenarios. The assistant integrates the following features:

E-Commerce Search Aggregator: Finds fashion items from multiple platforms.
Shipping Time Estimator: Evaluates shipping feasibility and cost.
Discount / Promo Code Checker: Validates promo codes and applies them.
Competitor Price Comparison: Compares prices of the same product across different e-commerce sites.
Return Policy Checker: Checks return policies for different platforms.</p>

<h2>🔧 Features</h2>

<ul>
  <li>
    🔍 Item Search: Search for fashion items based on criteria like color, size, price, and more.
📦 Shipping Deadlines: Get estimates for shipping feasibility and time based on user location.
💸 Price Comparison: Compare the prices of fashion items across different online stores.
🎟️ Discount Codes: Validate and apply discount codes to get the best price.
🔄 Return Policies: Check return policies of e-commerce websites before making purchases.
🤯 Multi-Step Reasoning: The agent uses a combination of tools to provide accurate answers to complex queries.
  </li>
</ul>

<hr>

<h2>
  ⚙️ Installation
</h2>

<h3>📋 Requirements</h3>

<p>Before running the app, make sure to have the following installed:

Python 3.x 🔑
pip (Python package manager) 📦</p>


<h2>🛠️ Step-by-Step Installation</h2>

<p>Clone the repository:</p>

<p>git clone https://github.com/your-username/your-repo-name.git
</p>

<p>Navigate into the project directory:</p>
<p>cd your-repo-name
</p>

<p>Install the required dependencies:</p>
<p>pip install -r requirements.txt
</p>

<p>Download the spaCy model:</p>
<p>python -m spacy download en_core_web_sm
</p>

<hr>

<h2>🖥️ Usage</h2>

<p>To run the AI Fashion Assistant, use the following command in your terminal:</p>
<p>streamlit run streamlit_app.py
</p>

<hr>

<h2>
  🤖 Agent Workflow
</h2>

<p>Here’s how the AI Fashion Assistant works:

Reasoning: When a user submits a query, the agent determines which tools to invoke based on the task. 🧠
Tool Calls: The agent makes API calls to external tools (e-commerce search, shipping estimator, etc.). ⚙️
Integration: The agent combines data from the tools to generate a coherent response for the user. 🔄</p>

<hr>

<h2>🛠️ Tools Implementation</h2>

<p>The tools that power the assistant include:

1. E-Commerce Search Aggregator 🔍
Function: Searches across multiple e-commerce sites based on user criteria (e.g., name, price, size).
Mock Implementation: Returns a list of products with details such as name, price, and availability.
2. Shipping Time Estimator 📦
Function: Estimates shipping feasibility, cost, and delivery date based on the user's location.
Mock Implementation: Returns shipping details for the product.
3. Discount / Promo Code Checker 🎟️
Function: Validates discount codes and adjusts the final price.
Mock Implementation: Applies promo codes to the product price.
4. Competitor Price Comparison 💸
Function: Compares the price of a product across different stores.
Mock Implementation: Returns price comparisons from different online platforms.
5. Return Policy Checker 🔄
Function: Checks return policies for various e-commerce sites.
Mock Implementation: Returns the return policy for a specified site.
</p>

<hr>

<h2>🚧 Challenges and Improvements</h2>

<p>Challenges:
Data Integration: Combining results from different tools seamlessly is a challenge.
Mock Data: Creating realistic mock implementations for external tools proved difficult.
Deployment: Facing challenges related to external dependencies and platform limitations.
Improvements:
Scalability: Future improvements could involve integrating real e-commerce APIs for better accuracy. 🌱
Advanced AI Models: We can enhance the reasoning capabilities of the assistant with more sophisticated models. 🤖</p>


<hr>

<h2>🔮 Future Work</h2>

<p>Real E-Commerce Integration: Replace mock tools with actual API calls to e-commerce platforms for real-time data. 💻
Enhanced User Interface: Improving the UI to be more interactive and user-friendly. 💡
Multi-Platform Support: Adding support for more e-commerce platforms and payment gateways. 💳</p>

<hr>

<h2>📝 License</h2>

<p>This project is licensed under the MIT License - see the LICENSE file for details. 📜</p>


<hr>

<h2>🚀 Stay Connected</h2>

<p>If you found this project interesting or useful, feel free to ⭐️ this repository or contribute to it! Let's build amazing AI agents for the future! 🙌

</p>


<hr>


<h2>Output</h2>

![Screenshot 2025-02-17 233332](https://github.com/user-attachments/assets/bf7c12a1-2d34-4c87-bd49-65a93958c7ca)
![Screenshot 2025-02-17 233342](https://github.com/user-attachments/assets/86849a81-267f-45fe-9da1-c6c632040a02)
