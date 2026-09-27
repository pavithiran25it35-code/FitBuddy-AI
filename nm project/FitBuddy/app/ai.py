
import json
import os


# ============================================================
# FITBUDDY DEMO WORKOUTS
# ============================================================

DEMO_WORKOUTS = {
    "weight loss": {
        "bodyweight": [
            ("Day 1", "Full Body Fat Burn", [
                "Bodyweight squats 3x12",
                "Incline push-ups 3x10",
                "Reverse lunges 3x10/side",
                "Mountain climbers 3x20",
                "Plank 3x30 sec"
            ]),
            ("Day 2", "Cardio + Core", [
                "Brisk walk 25 min",
                "High knees 3x30 sec",
                "Bird dogs 3x10/side",
                "Dead bug 3x10/side",
                "Plank 3x30 sec"
            ]),
            ("Day 3", "Upper Body + Core", [
                "Incline push-ups 3x10",
                "Wall push-ups 3x12",
                "Backpack rows 3x12",
                "Shoulder taps 3x16",
                "Dead bug 3x10/side"
            ]),
            ("Day 4", "Active Recovery", [
                "Easy walk 20 min",
                "Hip mobility 5 min",
                "Shoulder mobility 5 min",
                "Full-body stretching 10 min"
            ]),
            ("Day 5", "Lower Body Burn", [
                "Bodyweight squats 3x15",
                "Reverse lunges 3x10/side",
                "Glute bridges 3x15",
                "Calf raises 3x18",
                "Wall sit 3x30 sec"
            ]),
            ("Day 6", "Cardio + Full Body", [
                "Walk/jog intervals 25 min",
                "Bodyweight squats 3x12",
                "Incline push-ups 3x10",
                "Mountain climbers 3x20",
                "Plank 3x30 sec"
            ]),
            ("Day 7", "Recovery + Mobility", [
                "Easy walk 20 min",
                "Full-body stretch 10 min",
                "Gentle mobility 5 min",
                "Deep breathing 5 min"
            ])
        ]
    },

    "muscle gain": {
        "bodyweight": [
            ("Day 1", "Full Body Strength", [
                "Slow bodyweight squats 4x10",
                "Push-ups 4x8-12",
                "Glute bridges 4x12",
                "Pike push-ups 3x8",
                "Plank 3x40 sec"
            ]),
            ("Day 2", "Upper Body", [
                "Push-ups 4x8-12",
                "Backpack rows 4x10-12",
                "Pike push-ups 3x8",
                "Close-grip push-ups 3x8",
                "Dead bug 3x10/side"
            ]),
            ("Day 3", "Lower Body", [
                "Bodyweight squats 4x12",
                "Reverse lunges 3x10/side",
                "Single-leg glute bridges 3x10/side",
                "Calf raises 4x15",
                "Wall sit 3x40 sec"
            ]),
            ("Day 4", "Recovery", [
                "Easy walk 20 min",
                "Mobility 10 min",
                "Full-body stretching 10 min"
            ]),
            ("Day 5", "Full Body Strength", [
                "Bulgarian split squats 3x8/side",
                "Push-ups 4x10",
                "Backpack rows 4x12",
                "Glute bridges 4x15",
                "Plank 3x45 sec"
            ]),
            ("Day 6", "Upper + Core", [
                "Push-ups 4x10",
                "Backpack rows 4x12",
                "Pike push-ups 3x10",
                "Shoulder taps 3x16",
                "Plank 3x45 sec"
            ]),
            ("Day 7", "Active Recovery", [
                "Easy walk 20 min",
                "Gentle stretching 15 min",
                "Breathing 5 min"
            ])
        ]
    },

    "general wellness": {
        "bodyweight": [
            ("Day 1", "Full Body Fitness", [
                "Bodyweight squats 3x10",
                "Incline push-ups 3x10",
                "Glute bridges 3x12",
                "Bird dogs 3x10/side",
                "Plank 3x30 sec"
            ]),
            ("Day 2", "Cardio + Mobility", [
                "Brisk walk 25 min",
                "Hip mobility 5 min",
                "Shoulder mobility 5 min",
                "Gentle stretching 5 min"
            ]),
            ("Day 3", "Upper Body + Core", [
                "Incline push-ups 3x10",
                "Backpack rows 3x12",
                "Shoulder taps 3x16",
                "Dead bug 3x10/side"
            ]),
            ("Day 4", "Recovery", [
                "Easy walk 20 min",
                "Full-body stretching 10 min",
                "Breathing 5 min"
            ]),
            ("Day 5", "Lower Body", [
                "Bodyweight squats 3x12",
                "Reverse lunges 3x8/side",
                "Glute bridges 3x15",
                "Calf raises 3x15"
            ]),
            ("Day 6", "Cardio + Core", [
                "Walk/jog intervals 20 min",
                "Bird dogs 3x10/side",
                "Plank 3x30 sec",
                "Dead bug 3x10/side"
            ]),
            ("Day 7", "Active Recovery", [
                "Easy walk 20 min",
                "Full-body stretch 10 min",
                "Relaxation breathing 5 min"
            ])
        ]
    }
}


# ============================================================
# EQUIPMENT-SPECIFIC WORKOUT REPLACEMENTS
# ============================================================

EQUIPMENT_EXERCISES = {
    "Dumbbells": [
        "Goblet squats 3x10-12",
        "Dumbbell chest press 3x10",
        "One-arm dumbbell rows 3x10/side",
        "Dumbbell shoulder press 3x10",
        "Dumbbell Romanian deadlifts 3x10",
        "Dumbbell lunges 3x8/side"
    ],

    "Home gym": [
        "Goblet squats 3x10-12",
        "Resistance chest press 3x10",
        "Cable rows 3x12",
        "Shoulder press 3x10",
        "Romanian deadlifts 3x10",
        "Glute bridges 3x15"
    ],

    "Full gym": [
        "Barbell or machine squats 3x8-10",
        "Bench press 3x8-10",
        "Lat pulldown 3x10",
        "Seated cable row 3x10",
        "Romanian deadlift 3x8-10",
        "Leg press 3x10"
    ]
}


# ============================================================
# FOOD PLAN
# ============================================================

def food_plan(diet):
    diet = (diet or "balanced").lower()

    if diet == "vegetarian":
        return [
            "Breakfast: Oats with milk/curd, banana and nuts",
            "Lunch: Rice or roti with dal, vegetables and curd",
            "Snack: Fruit with yogurt, nuts or roasted chickpeas",
            "Dinner: Paneer/tofu with roti and mixed vegetables"
        ]

    if diet == "vegan":
        return [
            "Breakfast: Oats with soy milk, banana and chia seeds",
            "Lunch: Rice/quinoa with lentils, beans and vegetables",
            "Snack: Fruit with nuts or roasted chickpeas",
            "Dinner: Tofu/beans with roti and mixed vegetables"
        ]

    if diet == "high-protein":
        return [
            "Breakfast: Eggs/Greek yogurt with oats and fruit",
            "Lunch: Chicken/fish/tofu with rice and vegetables",
            "Snack: Greek yogurt, fruit and nuts",
            "Dinner: Lean protein with vegetables and whole-food carbohydrates"
        ]

    return [
        "Breakfast: Oats/eggs with fruit and nuts",
        "Lunch: Rice or roti with vegetables and a protein source",
        "Snack: Fruit with yogurt or nuts",
        "Dinner: Protein + vegetables + whole-food carbohydrate"
    ]


# ============================================================
# DEMO PLAN
# ============================================================

def demo_plan(profile, feedback=""):
    goal = str(profile.get("goal", "general wellness")).lower()
    experience = str(profile.get("experience", "beginner")).lower()
    equipment = str(profile.get("equipment", "bodyweight"))

    minutes = profile.get("workout_minutes") or 30
    activity = profile.get("activity_level", "moderate")
    diet = profile.get("dietary_preference", "balanced")

    # Select base workout
    goal_workouts = DEMO_WORKOUTS.get(
        goal,
        DEMO_WORKOUTS["general wellness"]
    )

    workouts = goal_workouts.get(
        "bodyweight",
        DEMO_WORKOUTS["general wellness"]["bodyweight"]
    )

    days = []

    for index, (name, focus, exercises) in enumerate(workouts):

        current_exercises = list(exercises)

        # If user has equipment, add suitable resistance exercises.
        if equipment in EQUIPMENT_EXERCISES and index in [0, 2, 4]:
            equipment_exercises = EQUIPMENT_EXERCISES[equipment]

            if experience == "beginner":
                current_exercises = equipment_exercises[:3]

            elif experience == "intermediate":
                current_exercises = equipment_exercises[:4]

            else:
                current_exercises = equipment_exercises[:5]

        # Keep recovery days simple.
        if "Recovery" in focus or "recovery" in focus:
            current_exercises = exercises

        # Make duration reasonable.
        duration = minutes

        if "Recovery" in focus:
            duration = min(minutes, 30)

        days.append({
            "day": name,
            "focus": focus,
            "workout": current_exercises,
            "duration_minutes": duration,
            "intensity": activity,
            "food": food_plan(diet),
            "recovery": (
                "Hydrate well, prioritize sleep, and take rest when needed. "
                "Stop exercise if you experience sharp pain, dizziness, "
                "or feel unwell."
            )
        })

    return {
        "title": (
            "7-Day FitBuddy Plan — "
            + str(profile.get("goal", "General Wellness")).title()
        ),
        "goal": profile.get("goal", "general wellness"),
        "summary": (
            "A personalized 7-day workout and nutrition plan based on "
            "your goal, experience, equipment, activity level and workout time."
        ),
        "days": days,
        "nutrition": [
            "Include a good protein source in your main meals.",
            "Include vegetables and fruit regularly.",
            "Drink water throughout the day.",
            "Choose sustainable portions instead of extreme restriction."
        ],
        "safety": (
            "If you have a medical condition, injury, are pregnant, "
            "or are unsure whether exercise is safe for you, consult "
            "a qualified healthcare or fitness professional."
        )
    }


# ============================================================
# GEMINI PLAN GENERATOR
# ============================================================

def generate_plan(profile, feedback=""):

    key = os.getenv("GEMINI_API_KEY", "").strip()

    # --------------------------------------------------------
    # No Gemini key -> demo mode
    # --------------------------------------------------------

    if not key or key == "YOUR_GEMINI_API_KEY_HERE":
        return demo_plan(profile, feedback), "demo"

    try:
        from google import genai

        client = genai.Client(api_key=key)

        model = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

        schema = {
            "title": "string",
            "goal": "string",
            "summary": "string",

            "days": [
                {
                    "day": "Day 1",
                    "focus": "string",

                    "workout": [
                        "Exercise name — sets x reps — rest"
                    ],

                    "duration_minutes": 30,
                    "intensity": "easy/moderate/hard",

                    "food": [
                        "Breakfast: ...",
                        "Lunch: ...",
                        "Snack: ...",
                        "Dinner: ..."
                    ],

                    "recovery": "string"
                }
            ],

            "nutrition": [
                "string",
                "string",
                "string"
            ],

            "safety": "string"
        }

        prompt = f"""
You are FitBuddy, a personalized AI fitness and nutrition planning assistant.

Create a SAFE and PRACTICAL 7-DAY FITNESS PLAN.

USER PROFILE:
{json.dumps(profile, indent=2)}

USER FEEDBACK:
{feedback or "None"}

IMPORTANT WORKOUT REQUIREMENTS:

1. Create exactly 7 days.
2. Workout must be personalized using:
   - goal
   - experience
   - equipment
   - activity level
   - workout minutes
3. Do not give the same workout every day.
4. Include different muscle groups and recovery days.
5. Match exercises to the available equipment.
6. Respect the user's requested workout duration.
7. For each workout exercise, provide:
   - exercise name
   - sets
   - reps OR duration
   - rest when appropriate
8. Beginner users should receive simpler exercises and manageable volume.
9. Intermediate users can receive moderate volume.
10. Advanced users can receive more challenging variations.
11. Include at least one recovery/active recovery day.
12. Do not recommend dangerous, extreme or unsafe exercises.

IMPORTANT FOOD REQUIREMENTS:

1. FOOD MUST BE INCLUDED FOR ALL 7 DAYS.
2. Never remove the food section.
3. Every day must contain exactly:
   - Breakfast
   - Lunch
   - Snack
   - Dinner
4. Food must match the user's dietary preference.
5. Food should be practical and realistic.
6. Do not prescribe medication or supplements as medical treatment.
7. Do not diagnose diseases.
8. Avoid extreme calorie restriction.

OUTPUT REQUIREMENTS:

Return ONLY valid JSON.

The JSON MUST match this structure:

{json.dumps(schema, indent=2)}

Do not add Markdown.
Do not add ```json.
Do not add explanations outside JSON.
"""

        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        text = response.text.strip()

        # Remove accidental markdown fences if Gemini returns them.
        if text.startswith("```"):
            parts = text.split("```")

            if len(parts) >= 2:
                text = parts[1]

                if text.lstrip().startswith("json"):
                    text = text.lstrip()[4:]

        plan = json.loads(text)

        # ----------------------------------------------------
        # Basic validation
        # ----------------------------------------------------

        if not isinstance(plan, dict):
            raise ValueError("Gemini returned an invalid plan.")

        if not isinstance(plan.get("days"), list):
            raise ValueError("Gemini plan does not contain days.")

        if len(plan["days"]) != 7:
            raise ValueError("Gemini did not generate exactly 7 days.")

        # Make sure food exists even if Gemini accidentally misses it.
        for day in plan["days"]:

            if not isinstance(day.get("workout"), list):
                day["workout"] = []

            if not isinstance(day.get("food"), list) or len(day["food"]) == 0:
                day["food"] = food_plan(
                    profile.get(
                        "dietary_preference",
                        "balanced"
                    )
                )

            if not day.get("recovery"):
                day["recovery"] = (
                    "Hydrate, sleep well and take rest when needed."
                )

        return plan, "gemini"

    except Exception as exc:

        # ----------------------------------------------------
        # Gemini failure -> safe fallback
        # ----------------------------------------------------

        plan = demo_plan(profile, feedback)

        plan["summary"] += (
            " Gemini was unavailable, so FitBuddy used its "
            "built-in personalized fallback plan."
        )

        return plan, "fallback:" + type(exc).__name__
 
