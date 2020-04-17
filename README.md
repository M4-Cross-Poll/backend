# Rain or Shine (Backend)

[Heroku](https://rain-or-shine-backend.herokuapp.com/)

[Frontend Repository](https://rain-or-shine-backend.herokuapp.com/)

### Description

Rain or Shine is a mobile app developed for Andriod and iOS. The application allows users to scheduled outdoor activities (such as hiking, mountain biking, kayaking, etc.) for a specified date and location. Rain or Shine will check the forecast at that location, and if the forecast is bad or would hinder them doing that activity due to rain, snow/sleet, or extreme wind, Rain or Shine will return a list of exercises the user can do that target the same muscle groups as that outdoor activity.

The backend for Rain or Shine is developed using Python and Django. Through various endpoints, our backend provides detailed information to our React Native frontend and also retrieves and synthesizes forecast data for scheduled activities on a daily basis. 

### Contents
- [Contributors](#contributors)
- [Getting Started](#getting-started)
- [Database Structure](#database-structure)
- [Endpoints](#endpoints)

## Contributors
Backend Developers
---
[Darren Campbell](https://github.com/darren2802)
[Dylan Connolly](https://github.com/dylanconnolly)

Frontend Developers
---
[Grayson Palmer](https://github.com/grayson-palmer)
[Johnny Cassidy](https://github.com/pJanks)

## Getting Started

1. Clone this repo: `git clone git@github.com:M4-Cross-Poll/backend.git`

2. Install dependencies: `pip3 install -r requirements.txt`



## Database Structure


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

- GET `/api/v1/user/<int:user_id>/scheduled_activities/<int:scheduled_activity_id>`

```
{
    "id": 4,
    "status": "bad",
    "date": "2020-04-21T00:00:00Z",
    "location": "Breckenridge, CO",
    "forecast": "Foggy until afternoon, starting again overnight.",
    "forecast_img": "rain",
    "temperature": "45.03",
    "temp_hi": "46.61",
    "temp_low": "28.48",
    "precip_probability": "0.46",
    "activity": {
        "id": 6,
        "name": "Cricket",
        "primary_muscles": [
            {
                "id": 6,
                "name": "Glutes & Hip Flexors",
                "primary_exercises": [
                    {
                        "id": 151,
                        "name": "lying-leg-curls",
                        "description": "Targets hamstrings and also involves glutes & hip flexors.",
                        "img_url": "",
                        "equipment": "Full gym",
                        "instructions": "Lie face down on a leg curl machine and lock your heels under the foot pad. Make sure your legs are fully extended and the foot pads are resting on the back of your ankles. If the machine is equipped with handles, grip them. If not, grip the front of the pad you are lying on. Remaining flat on the bench, with no arching of your spine, curl your legs up in a smooth arcing motion by bending your knees until your hamstrings are fully contracted. Hold for a count of one. Slowly lower your legs to the starting position in a smooth arcing motion. Repeat"
                    }
                ]
            }
        ],
        "secondary_muscles": [
            {
                "id": 4,
                "name": "Chest",
                "secondary_exercises": [
                    {
                        "id": 220,
                        "name": "shadow-boxing",
                        "description": "Targets abs and biceps and shoulders and triceps and also involves calves and glutes & hip flexors and lower back and quadriceps and shoulders and triceps.",
                        "img_url": "",
                        "equipment": "NO EQUIPMENT",
                        "instructions": "Stand tall with a tight core. Keep your gaze straight ahead. Bring your hands up to shoulder level. Make a tight fist with the thumb on the outside of your hand. Do not wrap your fingers around your thumb. Begin in a left lead stance. Your left foot should be in front. Your right foot should be behind. Throw a left lead jab by extending your left hand straight out in front of you and immediately retracting. Follow up the left jab with a right cross. Twist your foot and drive your right hip forward as you throw a straight punch with your back right hand. Alternate these two punches. Switch sides when finished with the prescribed repetitions."
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
    "created_at": "2020-04-14T00:44:31.125830Z",
    "updated_at": "2020-04-14T00:44:31.125857Z"
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

- DELETE `/api/v1/users/:user_id/scheduled_activities/:scheduled_activity_id`

If request is successful, will return `204` status and `Deleted successfully` message.

If record cannot be found based off the ID provided in the URL, will return `404` and `Record not found` message.

If server runs into an error when trying to delete a record, will raise `500` error and `Unable to delete record` message.
