import streamlit as st
import random
from datetime import datetime

# Page config

st.set_page_config(page_title=“Athlete Motivation”, page_icon=“💪”, layout=“wide”)

# Custom CSS

st.markdown(”””
<style>
.big-font {
font-size: 28px !important;
font-weight: bold;
color: #FF4B4B;
}
.quote-box {
padding: 30px;
border-radius: 10px;
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
color: white;
margin: 20px 0;
}
.stat-box {
padding: 20px;
border-radius: 10px;
background-color: #f0f2f6;
text-align: center;
}
</style>
“””, unsafe_allow_html=True)

# Motivational quotes

quotes = [
{“text”: “The only way to prove you are a good sport is to lose.”, “author”: “Ernie Banks”},
{“text”: “Champions keep playing until they get it right.”, “author”: “Billie Jean King”},
{“text”: “You miss 100% of the shots you don’t take.”, “author”: “Wayne Gretzky”},
{“text”: “Hard work beats talent when talent doesn’t work hard.”, “author”: “Tim Notke”},
{“text”: “It’s not whether you get knocked down, it’s whether you get up.”, “author”: “Vince Lombardi”},
{“text”: “The difference between the impossible and the possible lies in determination.”, “author”: “Tommy Lasorda”},
{“text”: “Gold medals aren’t really made of gold. They’re made of sweat, determination, and hard-to-find alloy called guts.”, “author”: “Dan Gable”},
{“text”: “Pain is temporary. Quitting lasts forever.”, “author”: “Lance Armstrong”},
{“text”: “If you can’t outplay them, outwork them.”, “author”: “Ben Hogan”},
{“text”: “Don’t stop when you’re tired. Stop when you’re done.”, “author”: “Unknown”},
{“text”: “Your biggest competitor is yourself.”, “author”: “Unknown”},
{“text”: “Discipline is doing what needs to be done, even when you don’t want to do it.”, “author”: “Unknown”},
]

# Workout motivations

workouts = [
“🏃 Today’s challenge: Add 5 minutes to your cardio session”,
“💪 Focus on form today - quality over quantity”,
“🔥 Try a new exercise you’ve been avoiding”,
“⚡ High-intensity interval training day!”,
“🧘 Active recovery: Stretching and mobility work”,
“🏋️ Push yourself to lift 5% heavier today”,
“🌟 Practice your sport-specific skills”,
“💯 Complete your workout 10 minutes faster”,
]

# App header

st.title(“💪 Daily Athlete Motivation”)
st.markdown(f”**{datetime.now().strftime(’%A, %B %d, %Y’)}**”)

# Sidebar

with st.sidebar:
st.header(“🎯 Your Profile”)
athlete_name = st.text_input(“Your Name”, “Champion”)
sport = st.selectbox(“Your Sport”,
[“Running”, “Basketball”, “Football”, “Soccer”, “Swimming”,
“Cycling”, “Weightlifting”, “Tennis”, “CrossFit”, “Other”])

```
st.markdown("---")
st.header("📊 Quick Stats")
days_trained = st.number_input("Days trained this week", 0, 7, 0)
st.progress(days_trained / 7)

if days_trained >= 5:
    st.success("🔥 On fire!")
elif days_trained >= 3:
    st.info("💪 Keep pushing!")
else:
    st.warning("⚡ Time to get moving!")
```

# Main content

col1, col2 = st.columns([2, 1])

with col1:
st.header(“🌟 Your Daily Motivation”)

```
# Daily quote
daily_quote = random.choice(quotes)
st.markdown(f"""
    <div class="quote-box">
        <h2 style='color: white; font-style: italic;'>"{daily_quote['text']}"</h2>
        <p style='text-align: right; color: #e0e0e0;'>— {daily_quote['author']}</p>
    </div>
""", unsafe_allow_html=True)

# Personal message
st.subheader(f"💬 Message for {athlete_name}")
messages = [
    f"Every rep counts, {athlete_name}. Make today's training session legendary!",
    f"Your competition is training right now, {athlete_name}. What are you waiting for?",
    f"Champions aren't born, they're made. Today is another brick in your foundation, {athlete_name}.",
    f"The pain you feel today will be the strength you feel tomorrow. Get after it, {athlete_name}!",
    f"Your {sport} skills are built one practice at a time. Consistency is key, {athlete_name}.",
]
st.info(random.choice(messages))
```

with col2:
st.header(“🎯 Today’s Focus”)

```
# Daily workout suggestion
st.markdown("### 🔥 Training Tip")
daily_workout = random.choice(workouts)
st.success(daily_workout)

# Mindset tips
st.markdown("### 🧠 Mindset")
mindset_tips = [
    "Visualize success",
    "Control your breath",
    "Stay in the moment",
    "Trust your training",
    "Embrace the challenge",
    "Focus on progress",
]
for tip in random.sample(mindset_tips, 3):
    st.markdown(f"✓ {tip}")
```

# Goals section

st.markdown(”—”)
st.header(“🎯 Set Your Daily Goals”)

col3, col4, col5 = st.columns(3)

with col3:
st.markdown(’<div class="stat-box">’, unsafe_allow_html=True)
st.markdown(”### Training Goal”)
training_goal = st.checkbox(“Complete today’s workout”)
if training_goal:
st.balloons()
st.markdown(’</div>’, unsafe_allow_html=True)

with col4:
st.markdown(’<div class="stat-box">’, unsafe_allow_html=True)
st.markdown(”### Nutrition Goal”)
nutrition_goal = st.checkbox(“Hit protein target”)
st.markdown(’</div>’, unsafe_allow_html=True)

with col5:
st.markdown(’<div class="stat-box">’, unsafe_allow_html=True)
st.markdown(”### Recovery Goal”)
recovery_goal = st.checkbox(“Get 8 hours of sleep”)
st.markdown(’</div>’, unsafe_allow_html=True)

# Affirmations

st.markdown(”—”)
st.header(“🔥 Power Affirmations”)
affirmations = [
“I am strong, capable, and unstoppable”,
“My body is built for this challenge”,
“I welcome the grind because I know it makes me better”,
“I am mentally tough and physically prepared”,
“Every day I’m getting closer to my goals”,
]

for affirmation in affirmations:
st.markdown(f”✨ **{affirmation}**”)

# Footer

st.markdown(”—”)
st.markdown(”””
<div style='text-align: center; color: #666;'>
<p>Remember: The difference between ordinary and extraordinary is that little extra effort.</p>
<p><strong>Now go dominate your day! 💪</strong></p>
</div>
“””, unsafe_allow_html=True)
