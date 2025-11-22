# Weather Report Agent Project 

```markdown
# 🌦️ AI Weather Agent

A smart AI-powered weather assistant built with Agno framework that fetches real-time weather data and automatically saves reports to files. Features natural language interaction, tool calling, and automatic file management.

## 🚀 Features

- **🌤️ Real-time Weather Data** - Fetch current weather for any city worldwide
- **💬 Interactive Chat** - Natural language interface using Groq LLM
- **📁 Automatic File Management** - Save weather reports as JSON/TXT files
- **🛠️ Tool Calling** - Intelligent agent that decides when to use weather and file tools


## 🛠️ Technologies Used

- **Agno** - AI agent framework
- **Groq LLM** - LLaMA 3.3 70B model for natural language processing
- **WeatherAPI** - Real-time weather data provider
- **Python** - Core programming language

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mumair567/weather_agent.git
   cd weather_agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your API keys:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     WEATHERAPI_KEY=your_weatherapi_key_here
     ```

## 🎯 Usage

Run the weather agent:
```bash
python weather_agent.py
```

### Example Interactions:
- "What's the weather in Lahore?"
- "Get Karachi weather and save it to a file"
- "Check Islamabad weather and save as JSON"
- "What's the temperature in Peshawar and save the report"

## 📁 Project Structure

```
weather_agent/
├── weather_agent.py     # Main agent with tool integration
├── agentt.py           # Additional agent configurations
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```



## 🔧 API Keys Required

1. **Groq API Key** - [Get from Groq Console](https://console.groq.com/)
2. **WeatherAPI Key** - [Get from WeatherAPI](https://www.weatherapi.com/)


## 👨‍💻 Author

**Umair**  
📧 Email: umair786uet@gmail.com  
🔗 GitHub: [Mumair567](https://github.com/Mumair567)


⭐ Star this repository if you find it helpful!
