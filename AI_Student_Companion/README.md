# 🎓 AI Student Companion

Your personal AI tutor & fitness buddy all in one! 💪🧠 
Get instant explanations, summaries, personalized workout plans, and nail those quizzes - all powered by AI. No more struggling alone! 🚀

---

## ✨ What You Can Do

### 📚 **Study Buddy** - Your AI Teacher
- **Explain** 📘 - Confused about a topic? Paste it here and get a clear breakdown!
- **Summarize** 📝 - Too many notes? Get the key points in seconds
- **Quiz Yourself** ❓ - Test your knowledge and get instant feedback
- Works with **ANYTHING** - Python code, Biology, History, Math... you name it! 🎯

### 💪 **Health Coach** - Your Fitness Friend
- Custom workouts based on YOUR goals (lose weight or build muscle?)
- Meal plans that match your diet (vegan? meat lover? no problem!)
- Daily routines for the whole week
- All packed in a beautiful, easy-to-use interface 💯

### 🎯 **Smart AI Teacher Feedback**
- Celebrates your wins ("🌟 Excellent! Keep it up!")
- Helps you learn from mistakes
- Gives study tips that actually work
- Tracks your progress and keeps you motivated

---

## 🛠️ What Powers This?

- **Flask** - The web framework holding it all together
- **Python** - The magic behind the scenes
- **AI Models** - BART, RoBERTa, and GPT-2 from Hugging Face (they're cool!)
- **PyTorch** - Deep learning that actually works
- **Vanilla JavaScript** - No fancy frameworks, just solid code

---

## 📋 Requirements

```
Flask==2.3.2
transformers==4.30.0
torch==2.0.0
nltk==3.8.1
```

See `requirements.txt` for complete dependencies.

---



### **Run the Application**
```bash
python app.py
```

The app will start at: **http://localhost:3000**

### **First Run - AI Model Loading**
On first run, AI models (~2.5 GB) will be downloaded and cached:
- `facebook/bart-large-cnn` - For text summarization
- `deepset/roberta-base-squad2` - For question answering
- `gpt2` - For text generation

This may take 5-10 minutes. After first run, models load instantly from cache.

## 💻 How to Use

### **Study Buddy** 📚
1. Click on **Study Buddy** from the sidebar
2. **Paste any text** you want to learn (lecture notes, random topic, whatever!)
3. Pick what you need:
   - **Explain** 📘 - Gets a full breakdown of the topic
   - **Summarize** 📝 - Gets the key points only
   - **Quiz** ❓ - Creates questions to test yourself
4. For quizzes:
   - Answer all 3 questions
   - Click "Check Answers"
   - See your score + detailed feedback
   - Learn from your mistakes 🎓

### **Health Coach** 💪
1. Go to **Health Coach** tab
2. Tell it about yourself:
   - Your age
   - Your gender
   - What you want (lose weight or build muscle?)
   - Your diet type (veggie or meat?)
3. Hit "Generate Plan"
4. See your custom workout & meal plan
5. Switch between **Workout Schedule** and **Nutrition Plan** tabs
6. Start crushing those goals! 💥

---

## 📁 What's Inside

### **Health Coach**
1. Navigate to **Health Coach** from the sidebar
2. **Fill in your information**:
   - Age
   - Gender (Male/Female/Other)
   - Primary Goal (Weight Loss / Muscle Gain)
   - Diet Preference (Vegetarian / Non-Veg)
3. Click **"Generate Plan"**
4. View your personalized plan:
   -    **Workout Schedule** - Daily exercises for the week
   -    **Nutrition Plan** - Meal breakdown with calories
5. Click **"Start Over"** to modify your plan anytime

### **Dashboard**
- Start page with quick access to all modules
- Learn about Study Buddy and Health Coach features

---

## 🎯 AI Teacher - Smart Learning System

The AI acts as a **personal teacher** with these features:

### Explanation Mode
- Breaks down complex topics into digestible concepts
- Provides real-world applications
- Includes study tips for better retention
- Explains why the topic is important

### Summary Mode
- Extracts key takeaways
- Lists learning objectives
- Recommends next steps
- Guides further learning

### Quiz Mode
- **Adaptive questions** for any topic
- **Instant feedback** on answers
- **Smart encouragement**:
  - 100% → "🌟 Excellent! Keep up the great work!"
  - 75%+ → "👍 Good! Review incorrect answers"
  - 50%+ → "📚 Fair! Review concepts and try again"
  - <50% → "💡 Keep Learning! Re-read material"

---

## 🔧 Customizing Your App

### Want to Change the Port?
Just edit `app.py` and find the line with `app.run()`:
```python
app.run(host="0.0.0.0", port=5000, debug=True)  # Change 3000 to whatever you want!
```

### Going Live?
Turn off debug mode for production:
```python
app.run(host="0.0.0.0", port=3000, debug=False)  # Way safer! 🔐
```

---

## 🌟 Features in Detail

### Study Material Processing
- Accepts any text input (lecture notes, textbooks, topics)
- AI analyzes content to generate relevant learning materials
- Supports long-form and short-form content
- Handles multiple topics simultaneously

### Quiz Features
- **Intelligent Question Generation**: Creates relevant MCQs automatically
- **Answer Validation**: Checks correctness against AI-trained models
- **Score Calculation**: Provides percentage and performance metrics
- **Detailed Feedback**: Explains correct answers for learning

### Health Plans
- **Personalized Workouts**: Based on fitness level and goals
- **Meal Plans**: Considers dietary restrictions and preferences
- **Progress Guidance**: Includes tips for consistency
- **Health Tips**: Sleep, hydration, stress management advice

---

## 🎓 For Students

### How to Learn Effectively
1. **Use Explain mode** to understand new topics
2. **Use Summarize mode** to review and retain
3. **Take Quizzes** to test your knowledge
4. **Review wrong answers** to strengthen understanding
5. **Take the quiz again** after reviewing

### Study Tips from AI Teacher
- Read carefully and identify key terms
- Explain concepts in your own words
- Create mind maps or notes for retention
- Practice quizzes regularly

---

## 🏥 For Health & Wellness

### Workout Tips
- Start with the provided routines
- Progressively increase intensity
- Rest days are important for recovery
- Track your progress weekly

### Nutrition Tips
- Follow meal recommendations
- Stay hydrated (8-10 glasses/day)
- Get 7-8 hours of sleep
- Be consistent for 4-6 weeks to see results

---

## 🚧 Future Enhancements

- [ ] User Authentication & Accounts
- [ ] Progress Tracking Dashboard
- [ ] File Upload Support (PDF, Images)
- [ ] Video Learning Integration
- [ ] Spaced Repetition System
- [ ] Leaderboards & Achievements
- [ ] Mobile App Version
- [ ] Advanced AI Models for better explanations
- [ ] Multi-language Support
- [ ] Voice Input/Output


## 🎉 Acknowledgments

- **Hugging Face** - For pre-trained AI models
- **Flask** - For the web framework
- **PyTorch & Transformers** - For deep learning capabilities
- **All Students** - Who use this app to learn

---

**Made with ❤️ for Students**

**Start Learning Today! 🚀**

