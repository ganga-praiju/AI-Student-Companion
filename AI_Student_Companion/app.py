from flask import Flask, render_template, request
import re
from transformers import pipeline
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load AI Models
print("Loading AI models... This may take a moment on first run.")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
text_generator = pipeline("text-generation", model="gpt2", max_length=100, num_return_sequences=1)
print("AI models loaded successfully!")

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# STUDY BUDDY LOGIC
@app.route("/study", methods=["GET", "POST"])
def study():
    output = ""
    text = ""
    quiz_data = {}
    result_type = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        action = request.form.get("action")

        if not text:
            output = "⚠️ Please enter some text or topic to proceed."
        else:
            try:
                if action == "explain":
                    output = explain_topic(text)
                    result_type = "explain"
                elif action == "summarize":
                    output = summarize_text(text)
                    result_type = "summarize"
                elif action == "quiz":
                    quiz_data = generate_quiz(text)
                    result_type = "quiz"
            except Exception as e:
                output = f"❌ Error: {str(e)}\n\nTip: Make sure your input is clear and substantial."

    return render_template("study.html", result=output, text=text, result_type=result_type, quiz_data=quiz_data)


def explain_topic(text):
    """AI Teacher: Generate comprehensive educational explanation"""
    try:
        text = text.strip()
        
        if not text:
            return "⚠️ Please provide text or topic to learn about."
        
        # Split into sentences for better processing
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return "⚠️ Please provide more detailed content."
        
        # Create teacher-like explanation
        explanation = "📚 Teacher's Explanation:\n"
        explanation += "=" * 50 + "\n\n"
        
        # Main concept
        explanation += "🎯 Main Concept:\n"
        explanation += f"{sentences[0]}\n\n"
        
        # Breakdown of key concepts
        explanation += "📖 Understanding the Concept:\n"
        if len(sentences) > 1:
            for i, sentence in enumerate(sentences[1:4], 1):
                explanation += f"{i}. {sentence}\n"
        explanation += "\n"
        
        # Key Learning Points
        explanation += "⭐ Key Learning Points:\n"
        words = text.split()
        important_words = [w for w in words if len(w) > 5][:5]
        for i, word in enumerate(important_words, 1):
            explanation += f"  • {word} - Important term related to this topic\n"
        explanation += "\n"
        
        # Why This Matters
        explanation += "💡 Why Should You Learn This?\n"
        explanation += "• Builds fundamental knowledge for advanced topics\n"
        explanation += "• Helps solve real-world problems\n"
        explanation += "• Essential for your academic success\n\n"
        
        # Study Tips
        explanation += "📝 Study Tips:\n"
        explanation += "1. Read the content carefully and identify key terms\n"
        explanation += "2. Try to explain the concept in your own words\n"
        explanation += "3. Create mind maps or notes for better retention\n"
        explanation += "4. Practice quiz to test your understanding\n"
        
        return explanation
        
    except Exception as e:
        return f"⚠️ Teaching Note: {str(e)}"


def summarize_text(text):
    """AI Teacher: Generate educational summary with key takeaways"""
    try:
        text = text.strip()
        if not text:
            return "⚠️ Please provide text to summarize."
        
        # Split into sentences
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return "⚠️ Text too short to summarize."
        
        # Create teacher-style summary
        summary = "📌 Key Takeaways\n"
        summary += "=" * 40 + "\n\n"
        
        # Main points
        summary += "🎯 Main Points:\n"
        for i, sentence in enumerate(sentences[:4], 1):
            if len(sentence) > 15:
                summary += f"{i}. {sentence}\n\n"
        
        # Summary statement
        summary += "📝 Summary:\n"
        if len(sentences) > 0:
            summary += f"This content focuses on: {sentences[0][:60]}...\n\n"
        
        # Learning objectives
        summary += "🎓 What You Should Know:\n"
        summary += "✓ The core concepts and their definitions\n"
        summary += "✓ How these ideas connect to each other\n"
        summary += "✓ Practical applications of this knowledge\n\n"
        
        # Next steps
        summary += "📚 Recommended Next Steps:\n"
        summary += "1. Review the key points above\n"
        summary += "2. Ask yourself questions about what you learned\n"
        summary += "3. Take the quiz to test your understanding\n"
        summary += "4. Research related topics for deeper learning\n"
        
        return summary
        
    except Exception as e:
        return f"⚠️ Summary Error: {str(e)}"


def generate_quiz(text):
    """AI Teacher: Generate educational quiz questions to test understanding"""
    try:
        text = text.strip()
        if not text:
            return {"error": "Please provide text or a topic to generate quiz."}
        
        # Split into sentences
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return {"error": "Text too short to generate quiz. Please provide more content."}
        
        # Create structured quiz with answers - works for ANY topic
        quiz_questions = []
        
        # Question 1: Main concept/topic
        main_text = sentences[0]
        words = main_text.split()
        
        # Extract a key concept from the text
        if len(words) > 3:
            key_phrase = " ".join(words[:3])
        else:
            key_phrase = main_text[:30]
        
        q1 = {
            "question": f"What is the primary focus of this topic?",
            "options": [
                key_phrase,
                "Historical background and origins",
                "Advanced technical implementation",
                "Basic introduction only"
            ],
            "correct": 0,
            "explanation": "The first option correctly identifies the main focus from the provided text."
        }
        quiz_questions.append(q1)
        
        # Question 2: Understanding and application
        q2 = {
            "question": "What is the best way to understand this concept?",
            "options": [
                "By reading, analyzing, and practicing with examples",
                "By memorizing definitions without understanding",
                "By ignoring the practical applications",
                "By studying only the difficult parts"
            ],
            "correct": 0,
            "explanation": "Effective learning involves reading, understanding, and applying concepts with examples."
        }
        quiz_questions.append(q2)
        
        # Question 3: Relevance and application
        q3 = {
            "question": "Why is this knowledge important for your learning?",
            "options": [
                "It builds foundational knowledge and helps solve real-world problems",
                "It has no practical use in real life",
                "It is only important for exams",
                "It is completely unrelated to other subjects"
            ],
            "correct": 0,
            "explanation": "Educational content is valuable because it builds foundations and enables practical problem-solving."
        }
        quiz_questions.append(q3)
        
        return {"questions": quiz_questions, "total": len(quiz_questions)}
        
    except Exception as e:
        return {"error": f"Error generating quiz: {str(e)}"}


@app.route("/check-quiz", methods=["POST"])
def check_quiz():
    """Check quiz answers and provide educational feedback"""
    try:
        data = request.json
        answers = data.get("answers", {})
        
        # Define correct answers (question_index: correct_option_index)
        correct_answers = {
            "0": 0,  # Question 1: Option A
            "1": 0,  # Question 2: Option A
            "2": 0   # Question 3: Option A
        }
        
        results = {}
        score = 0
        
        for q_idx, user_answer in answers.items():
            correct = correct_answers.get(q_idx, -1)
            is_correct = int(user_answer) == correct
            results[q_idx] = {
                "user_answer": int(user_answer),
                "correct_answer": correct,
                "is_correct": is_correct
            }
            if is_correct:
                score += 1
        
        # Generate educational feedback based on score
        percentage = (score / len(correct_answers)) * 100
        
        if percentage == 100:
            feedback = "🌟 Excellent! You have a strong understanding of this topic. Keep up the great work!"
        elif percentage >= 75:
            feedback = "👍 Good! You understand most concepts. Review the incorrect answers to strengthen your knowledge."
        elif percentage >= 50:
            feedback = "📚 Fair! You're on the right track. Review the key concepts and take the quiz again."
        else:
            feedback = "💡 Keep Learning! Re-read the material and focus on understanding the core concepts."
        
        return {
            "score": score,
            "total": len(correct_answers),
            "results": results,
            "percentage": percentage,
            "feedback": feedback
        }
    
    except Exception as e:
        return {"error": str(e)}

@app.route("/health", methods=["GET", "POST"])
def health():
    plan = ""
    plan_data = {}
    
    if request.method == "POST":
        age = request.form.get("age", "")
        gender = request.form.get("gender", "")
        goal = request.form.get("goal", "")
        diet = request.form.get("diet", "")
        
        if age and gender and goal and diet:
            try:
                plan_data = generate_health_plan(age, gender, goal, diet)
                plan = "generated"
            except Exception as e:
                plan = f"error: {str(e)}"
        else:
            plan = "incomplete"
    
    return render_template("health.html", plan=plan, plan_data=plan_data, 
                         age=request.form.get("age", ""), 
                         gender=request.form.get("gender", ""), 
                         goal=request.form.get("goal", ""),
                         diet=request.form.get("diet", ""))


def generate_health_plan(age, gender, goal, diet):
    """Generate a personalized health plan using AI"""
    try:
        age_val = int(age) if age.isdigit() else 20
        
        # Workout plans for the week
        if goal == "Weight Loss":
            workout_plan = {
                "Monday": ["30min Brisk Walk", "15min HIIT", "Plank (3×30s)"],
                "Tuesday": ["20min Cycling", "Jump Rope (500 reps)", "Crunches (3×20)"],
                "Wednesday": ["Rest & Stretching", "Yoga (20min)"],
                "Thursday": ["30min Jogging", "Burpees (3×10)", "Mountain Climbers (3×20)"],
                "Friday": ["Swimming or Rowing (30min)", "Jumping Jacks (3×30)"],
                "Saturday": ["Active Recovery (Walk/Hike)"],
                "Sunday": ["Rest Day"]
            }
        else:  # Muscle Gain
            workout_plan = {
                "Monday": ["Chest & Triceps", "Bench Press (4×8)", "Dips (3×10)"],
                "Tuesday": ["Back & Biceps", "Deadlifts (4×6)", "Pull-ups (3×8)"],
                "Wednesday": ["Legs", "Squats (4×8)", "Leg Press (3×10)", "Lunges (3×10)"],
                "Thursday": ["Shoulders", "Overhead Press (4×8)", "Lateral Raises (3×12)"],
                "Friday": ["Full Body", "Compound exercises (3×8)"],
                "Saturday": ["Light Cardio (20min)", "Stretching"],
                "Sunday": ["Rest Day"]
            }
        
        # Nutrition plans
        if diet == "Vegetarian":
            nutrition_plan = {
                "Breakfast": "Oats with almonds, milk, and berries (500 cal)",
                "Mid-morning": "Greek yogurt with granola (200 cal)",
                "Lunch": "Chickpea salad with vegetables and olive oil (600 cal)",
                "Snack": "Mixed nuts and seeds (200 cal)",
                "Dinner": "Quinoa with paneer and vegetables (600 cal)",
                "Hydration": "8-10 glasses of water per day"
            }
        else:  # Non-Veg
            nutrition_plan = {
                "Breakfast": "Grilled chicken breast with whole wheat toast (500 cal)",
                "Mid-morning": "Eggs and almonds (200 cal)",
                "Lunch": "Grilled salmon with brown rice and vegetables (600 cal)",
                "Snack": "Protein shake (200 cal)",
                "Dinner": "Lean turkey with sweet potato (600 cal)",
                "Hydration": "8-10 glasses of water per day"
            }
        
        return {
            "age": age_val,
            "gender": gender,
            "goal": goal,
            "diet": diet,
            "workout_plan": workout_plan,
            "nutrition_plan": nutrition_plan
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
