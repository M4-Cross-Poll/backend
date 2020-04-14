# Backend Django App for Rain or Shine


## Endpoints

- GET `/api/v1/exercises`
```
[
    {
        "id": 1,
        "name": "180-twisting-jump-squats",
        "description": "Targets calves and hamstrings and quadriceps and also involves abs and glutes & hip flexors.",
        "img_url": "",
        "equipment": "NO EQUIPMENT",
        "instructions": "Begin standing tall with a tight core. Your chest will be up and your gaze will be straight ahead. Bend at the knees and drive your hips back as you lower yourself into a squat position. Launch yourself up while simultaneously twisting to the other side. Your body will perform a 180 degree turn in midair. Land with bent knees and immediately go right into another jump squat, turning to the starting position. Repeat this alternating pattern."
    },
    {
        "id": 2,
        "name": "ab-crunch-machine",
        "description": "Targets abs.",
        "img_url": "",
        "equipment": "Full gym",
        "instructions": "Sit on the ab machine and select a slight resistance. Position your feet under the pads and grab hold of the top handles. Make sure your arms are bent at 90 degrees and rest your triceps on the pads. Begin lifting your legs up as you engage your abs and crunch your upper torso. Exhale as you do so. Pause and slowly return to starting position as you inhale."
    },
    {
        "id": 3,
        "name": "agility-ladder-drills",
        "description": "Targets abs and calves and glutes & hip flexors and hamstrings and lower back and quadriceps and also involves biceps and shoulders and triceps.",
        "img_url": "",
        "equipment": "Agility Ladder",
        "instructions": "Lay out the agility ladder on a non-slip surface.  Perform a routine of choice."
    },
    ...
]
```

- GET `/api/v1/exercise/<int:exercise_id>`
```
{
  "id": 1,
  "name": "180-twisting-jump-squats",
  "description": "Targets calves and hamstrings and quadriceps and also involves abs and glutes & hip flexors.",
  "img_url": "",
  "equipment": "NO EQUIPMENT",
  "instructions": "Begin standing tall with a tight core. Your chest will be up and your gaze will be straight ahead. Bend at the knees and drive your hips back as you lower yourself into a squat position. Launch yourself up while simultaneously twisting to the other side. Your body will perform a 180 degree turn in midair. Land with bent knees and immediately go right into another jump squat, turning to the starting position. Repeat this alternating pattern.",
  "muscle_groups": [
    "primary": [
      {
      "id": 1,
      "name": "Abs"
      },
      {
      "id": 3,
      "name": "Calves"
      }
    ],
    "secondary": [
      {
      "id": 6,
      "name": "Glutes & Hip Flexors"
      },
      {
      "id": 7,
      "name": "Hamstrings"
      },
      {
      "id": 12,
      "name": "Quadriceps"
      }
    ]
  ]
}
```

- GET `/api/v1/activities`
```
[
    {
        "id": 1,
        "name": "Mountain Biking"
    },
    {
        "id": 2,
        "name": "Hiking"
    },
    {
        "id": 3,
        "name": "Road Biking"
    },
    ...
```

- GET `/api/v1/scheduled_activities/<int:scheduled_activity_id>`

```
{
    "id": 1,
    "status": "good",
    "date": "2020-04-07T20:42:24Z",
    "location": "Denver, CO",
    "forecast": "Sunny",
    "forecast_img": "sunshine",
    "temperature": "55.10",
    "temp_hi": "73.25",
    "temp_low": "45.76",
    "precip_probability": "0.05",
    "activity": {
        "id": 1,
        "name": "Mountain Biking",
        "primary_muscles": [
            {
                "id": 11,
                "name": "Obliques",
                "primary_exercises": [
                    {
                        "id": 25,
                        "name": "bench-swiss-exercise-ball-russian-twists",
                        "description": "Targets abs and obliques.",
                        "img_url": "",
                        "equipment": "Swiss / Exercise ball",
                        "instructions": "Straddle a bench and hold a Swiss ball comfortably on your lap. Using your legs to hold the bench, lean your body back until your abdominal muscles are working to keep you upright (aim for a 45 degree angle) . Extend your arms to hold the Swiss ball directly out in front of your chest.   Rotate your body to the left holding the Swiss ball at the extended position. Rotate your body back to the center and then to the right to complete 1 full repetition.  "
                    },
                    {
                        "id": 38,
                        "name": "bosu-ball-side-planks",
                        "description": "Targets abs and obliques and also involves shoulders.",
                        "img_url": "",
                        "equipment": "Bosu ball",
                        "instructions": "With a Bosu ball round side up, place your forearm onto the center of the ball.  Stretch out your legs to a fully extended position and place your feet on the side, one on top of the other.  Use you core and upper legs to lift your body into the side plank position. Remain in this position for the designated time with your hand either on your hip, or by your side."
                    },
                    {
                        "id": 61,
                        "name": "crab-walks",
                        "description": "Targets glutes & hip flexors and shoulders and also involves abs.",
                        "img_url": "",
                        "equipment": "NO EQUIPMENT",
                        "instructions": "Sit on the ground with your knees bent, feet flat on the ground and your hands behind you. Your hands should be facing forward towards you. Begin the movement by lifting your hips into the air and bracing your abdominals. Your hips must stay up throughout the movement. Walk forward by moving your right foot and right hand forward. Switch to the left side. Continue this back and forth pattern while keeping your hips elevated. When finished, lower yourself to the ground."
                    },
                    {
                        "id": 69,
                        "name": "double-crunches",
                        "description": "Targets abs.",
                        "img_url": "",
                        "equipment": "NO EQUIPMENT",
                        "instructions": "Lie on your back. Bring your knees up to a 90-degree angle. Shins should be parallel to the floor. Place your hands behind your head and bring your shoulders off the ground. Exhale and contract your abdominals. Bring your head towards your knees while moving your knees toward your chest. Pause and return to the starting position."
                    },
                    {
                        "id": 73,
                        "name": "dumbbell-biceps-curl-to-shoulder-press",
                        "description": "Targets biceps and shoulders and also involves abs.",
                        "img_url": "",
                        "equipment": "Dumbbells",
                        "instructions": "Holding a pair of dumbbells, stand tall with your feet shoulder-width apart. Make sure your core is tight and your chest is up. Begin by curling the weight up towards your shoulders. Keep your upper arms tight at your sides. Once the dumbbells reach your shoulders, twist the dumbbells to have your palms face out. Now, drive the dumbbells overhead. Slowly, lower the dumbbells to your shoulders. Now, flip them back so your palms are facing you. With arms tight at your sides, lower the dumbbells to the starting position."
                    }
                ]
            }
        ],
        "secondary_muscles": [
            {
                "id": 13,
                "name": "Shoulders",
                "secondary_exercises": [
                    {
                        "id": 3,
                        "name": "agility-ladder-drills",
                        "description": "Targets abs and calves and glutes & hip flexors and hamstrings and lower back and quadriceps and also involves biceps and shoulders and triceps.",
                        "img_url": "",
                        "equipment": "Agility Ladder",
                        "instructions": "Lay out the agility ladder on a non-slip surface.  Perform a routine of choice."
                    },
                    {
                        "id": 12,
                        "name": "barbell-overhead-squats",
                        "description": "Targets calves and hamstrings and quadriceps and also involves abs and shoulders.",
                        "img_url": "",
                        "equipment": "Barbell / EZ-Bar",
                        "instructions": "Place an appropriate amount of weight on a barbell in a squat rack. Position your hands in an overhand grip outside of shoulder-width on the barbell. Before beginning, make sure that your core is tight and your chest is up. Push the barbell straight above your head, locking out your elbows. Once you feel stabilized, slowly bend the knees and drive back your hips. Once your upper thighs come parallel with the ground, slowly push back up, returning to the starting position."
                    },
                    {
                        "id": 13,
                        "name": "barbell-pushups-push-ups",
                        "description": "Targets chest and triceps and also involves abs and shoulders.",
                        "img_url": "",
                        "equipment": "Barbell / EZ-Bar",
                        "instructions": "Place a loaded barbell on the floor and place your hands at a slightly-wider-than-shoulder-width grip.  Bracing your core, get into push-up position with a straight posture from head to heel. Lower your body down until your chest hovers about ½ an inch from the bar. Use a combination of chest and triceps power to push your body back up away from the bar."
                    },
                    {
                        "id": 29,
                        "name": "bent-over-water-bottle-flyes",
                        "description": "Targets upper back & lower traps and also involves shoulders.",
                        "img_url": "",
                        "equipment": "Water Bottles",
                        "instructions": "Begin by holding a pair of water bottles and standing with a braced core. Bend at the knees slightly and lean forward from the hips. Maintain a flat back throughout. Keeping your elbows slightly bent throughout the movement, lift the water bottles up and out to the side. Be sure to focus the contraction in the back of the shoulders. Pause at the top of the movement then slowly bring the water bottles to the starting position."
                    },
                    {
                        "id": 36,
                        "name": "bosu-ball-chest-dumbbell-flyes-flies",
                        "description": "Targets abs and chest and also involves shoulders and triceps.",
                        "img_url": "",
                        "equipment": "Bosu ball, Dumbbells",
                        "instructions": "Begin by sitting on the floor with your lower back against the side of the Bosu ball, and with the dumbbells resting on your upper thighs.  Lower yourself back onto the Bosu ball while bringing the dumbbells onto your chest. Naturally you should create a straight bridge from your knees to your shoulders. Extend the dumbbells upward so that they are directly above your chest, without locking your arms, while keeping you hands internally rotated. Lower the the dumbbells away from each other, opening your chest while creating tension. Be sure not to lower the dumbbells past your shoulder line.   Bring the dumbbells back inwards to meet in the central starting position. Like hugging a barrel."
                    }
                ]
            },
            {
                "id": 9,
                "name": "Middle Back / Lats",
                "secondary_exercises": [
                    {
                        "id": 111,
                        "name": "gymnastic-ring-pull-ups-pullups",
                        "description": "Targets middle back / lats and upper back & lower traps and also involves biceps and forearms and shoulders.",
                        "img_url": "",
                        "equipment": "Gymnastic Rings",
                        "instructions": "Stand directly beneath the Gymnastic Rings ensuring that they have enough height for you to lower your body without touching the ground.  Grip the rings so that your palms are facing inward. Pull your chest upwards and towards the rings by bending your arms. Aim to avoid any jerking movements as this may cause the rings to swing.  Once your chest is at its highest point, hold this position for one second before steadily lowering your body back down to the starting position."
                    },
                    {
                        "id": 115,
                        "name": "hamstring-stretch",
                        "description": "Targets hamstrings and also involves glutes & hip flexors.",
                        "img_url": "",
                        "equipment": "NO EQUIPMENT",
                        "instructions": "Sit on a mat and extend your right leg out to the side. Bend your left leg and place the foot against your inner right thigh. Lean forward from the hips and reach for your ankle as comfortably as you can. You should feel a slight pull in the hamstring. Hold the stretch and then repeat on the left leg."
                    },
                    {
                        "id": 118,
                        "name": "hanging-leg-raises",
                        "description": "Targets abs and also involves forearms and glutes & hip flexors.",
                        "img_url": "",
                        "equipment": "Full gym, NO EQUIPMENT",
                        "instructions": "Grip a chin up or pull up bar with a firm overhand grip. Hang from the bar with your legs straight. Raise your legs by flexing your hips forward and bending your knees up towards your chest. Continue to raise your knees towards your chest by flexing your waist forward. Don’t swing your body to use momentum. Use your abdominals to pull your legs up. Return to the starting position, lowering your legs slowly until they are straight. Repeat."
                    },
                    {
                        "id": 119,
                        "name": "hanging-leg-raises-to-bar",
                        "description": "Targets abs and obliques and also involves middle back / lats.",
                        "img_url": "",
                        "equipment": "Full gym",
                        "instructions": "Assume a wide grip on a pull-up bar and hang so that your feet are not in contact with the ground.  Once steady, slowly lift your knees up towards your chest, doing your best to keep your legs fully extended.  Allow you upper back to drop backward to create balance and avoid swinging as your legs continue to rise. Bring your toes up to touch the bar before slowly lowering them back down to the starting, hanging position."
                    },
                    {
                        "id": 132,
                        "name": "jump-squats",
                        "description": "Targets glutes & hip flexors and quadriceps and also involves abs and calves and hamstrings.",
                        "img_url": "",
                        "equipment": "NO EQUIPMENT",
                        "instructions": "Stand with your feet hip width apart. Your toes should be pointing straight ahead or only slightly outward. Cross your arms in front of your body, place your hands behind your head or at the sides of your head. Keep your weight on your heels and bend your knees while lowering your hips towards the ground as if you are sitting down on a chair. Keep your back straight at all times. Continue until you feel a slight stretch in your quadriceps. Do not let your knees extend out beyond the level of your toes. Pause for a count of one. In an explosive movement, drive down through your heels pushing yourself up of the floor with your quads. At the same time extend our arms out above you. Land with your knees slightly bent to absorb the impact. Repeat"
                    }
                ]
            }
        ]
    },
    "user": {
        "id": 1,
        "username": "user",
        "first_name": "user",
        "last_name": "name",
        "scheduled_activities": [
            {
                "id": 1,
                "status": "good",
                "activity": "Mountain Biking",
                "date": "2020-04-07T20:42:24Z",
                "location": "Denver, CO",
                "forecast": "Sunny",
                "forecast_img": "sunshine"
            },
            {
                "id": 2,
                "status": "good",
                "activity": "Frisbee",
                "date": "2020-04-09T22:37:44Z",
                "location": "Breckenridge, CO",
                "forecast": "Overcast",
                "forecast_img": "cloudy"
            },
            {
                "id": 3,
                "status": "bad",
                "activity": "Mountain Biking",
                "date": "2020-04-16T00:00:00Z",
                "location": "Denver, CO",
                "forecast": "Possible light snow (2–4 in.) in the morning.",
                "forecast_img": "snow"
            },
            {
                "id": 4,
                "status": "bad",
                "activity": "Cricket",
                "date": "2020-04-21T00:00:00Z",
                "location": "Breckenridge, CO",
                "forecast": "Foggy until afternoon, starting again overnight.",
                "forecast_img": "rain"
            }
        ]
    },
    "created_at": "2020-04-07T20:43:07.198918Z",
    "updated_at": "2020-04-07T20:43:07.198936Z"
}
```

- GET `/api/v1/users/:user_id/scheduled_activities`
```
{
    "id": 1,
    "username": "user",
    "first_name": "user",
    "last_name": "name",
    "scheduled_activities": [
        {
            "id": 1,
            "status": "good",
            "activity": "Mountain Biking",
            "date": "2020-04-07T20:42:24Z",
            "location": "Denver, CO",
            "forecast": "Sunny",
            "forecast_img": "sunshine"
        },
        {
            "id": 2,
            "status": "good",
            "activity": "Frisbee",
            "date": "2020-04-09T22:37:44Z",
            "location": "Breckenridge, CO",
            "forecast": "Overcast",
            "forecast_img": "cloudy"
        },
        {
            "id": 3,
            "status": "bad",
            "activity": "Mountain Biking",
            "date": "2020-04-16T00:00:00Z",
            "location": "Denver, CO",
            "forecast": "Possible light snow (2–4 in.) in the morning.",
            "forecast_img": "snow"
        },
        {
            "id": 4,
            "status": "bad",
            "activity": "Cricket",
            "date": "2020-04-21T00:00:00Z",
            "location": "Breckenridge, CO",
            "forecast": "Foggy until afternoon, starting again overnight.",
            "forecast_img": "rain"
        }
    ]
}
```
