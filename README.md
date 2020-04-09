# Backend Django App for Rain or Shine


## Endpoints

- GET '/api/v1/exercise/<int:exercise_id>'
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

- GET `/api/v1/scheduled_activities/<int:scheduled_activity_id>`

```
{
    "id": 1,
    "date": "2020-04-06T03:23:24Z",
    "location": "Denver, CO",
    "forecast": "Overcast",
    "forecast_img": "cloudy",
    "activity": {
        "id": 1,
        "name": "Hiking",
        "muscle_groups": [
            "primary": [
              {
                  "id": 1,
                  "name": "Biceps",
                  "exercise_set": [
                      {
                          "id": 1,
                          "name": "Pull Ups",
                          "description": "Pull yourself up",
                          "img_url": "fake_img"
                      }
                  ]
              }
            ],
            "secondary": [
              {
                  "id": 2,
                  "name": "Forearms",
                  "exercise_set": [
                      {
                          "id": 3,
                          "name": "Push Ups",
                          "description": "Push yo' self",
                          "img_url": "some_img"
                      },
                      {
                          "id": 4,
                          "name": "Small Arm Circles",
                          "description": "Feel the burn",
                          "img_url": "some_img"
                      },
                  ]
              }
            ]
        ]
    },
    "user": {
        "id": 1,
        "first_name": "user",
        "last_name": "name"
    },
    "created_at": "2020-04-06T03:23:26.122544Z",
    "updated_at": "2020-04-06T03:23:26.122555Z"
}, {
    "id": 2,
    "date": "2020-04-01T03:23:24Z",
    "location": "Las Vegas, Nv",
    "forecast": "Sunny",
    "forecast_img": "sunshine",
    "activity": {
        "id": 3,
        "name": "Running",
        "muscle_groups": [
            {
                "id": 4,
                "name": "Calves",
                "exercise_set": [
                    {
                        "id": 1,
                        "name": "Pull Ups",
                        "description": "Pull yourself up ya dingus",
                        "img_url": "fake_img"
                    },
                    {
                        "id": 2,
                        "name": "Curls",
                        "description": "curl some heavy weights",
                        "img_url": "some_img"
                    },
                    {
                        "id": 3,
                        "name": "Push Ups",
                        "description": "Push yo' self",
                        "img_url": "some_img"
                    },
                    {
                        "id": 4,
                        "name": "Small Arm Circles",
                        "description": "Feel the burn",
                        "img_url": "some_img"
                    },
                    {
                        "id": 5,
                        "name": "Big Arm Circles",
                        "description": "Feel the bigger burn",
                        "img_url": "some_img"
                    },
                    {
                        "id": 6,
                        "name": "Jumping Jacks",
                        "description": "Don't stop, get it, get it",
                        "img_url": "some_img"
                    },
                ]
            }
        ]
    },
    "user": {
        "id": 1,
        "first_name": "user",
        "last_name": "name"
    },
    "created_at": "2020-04-02T03:23:26.122544Z",
    "updated_at": "2020-04-02T03:23:26.122555Z"
}, {
    "id": 3,
    "date": "2020-04-02T03:23:24Z",
    "location": "Boulder, CO",
    "forecast": "Rainyt",
    "forecast_img": "rainclouds",
    "activity": {
        "id": 4,
        "name": "Kayaking",
        "muscle_groups": [
            {
                "id": 1,
                "name": "Biceps",
                "exercise_set": [
                    {
                        "id": 3,
                        "name": "Push Ups",
                        "description": "Push yo' self",
                        "img_url": "some_img"
                    },
                    {
                        "id": 1,
                        "name": "Pull Ups",
                        "description": "Pull yourself up ya dingus",
                        "img_url": "fake_img"
                    }
                ]
            },
            {
                "id": 3,
                "name": "Ankles",
                "exercise_set": [
                    {
                        "id": 2,
                        "name": "Curls",
                        "description": "curl some heavy weights",
                        "img_url": "some_img"
                    }
                ]
            }
        ]
    },
    "user": {
        "id": 1,
        "first_name": "user",
        "last_name": "name"
    },
    "created_at": "2020-04-08T03:23:26.122544Z",
    "updated_at": "2020-04-08T03:23:26.122555Z"
},  {
    "id": 4,
    "date": "2020-04-07T03:23:24Z",
    "location": "Denver, CO",
    "forecast": "Windy",
    "forecast_img": "a picture of wind",
    "activity": {
        "id": 4,
        "name": "Kayaking",
        "muscle_groups": [
            {
                "id": 1,
                "name": "Biceps",
                "exercise_set": [
                    {
                        "id": 3,
                        "name": "Push Ups",
                        "description": "Push yo' self",
                        "img_url": "some_img"
                    },
                    {
                        "id": 1,
                        "name": "Pull Ups",
                        "description": "Pull yourself up ya dingus",
                        "img_url": "fake_img"
                    }
                ]
            },
            {
                "id": 3,
                "name": "Ankles",
                "exercise_set": [
                    {
                        "id": 2,
                        "name": "Curls",
                        "description": "curl some heavy weights",
                        "img_url": "some_img"
                    }
                ]
            }
        ]
    },
    "user": {
        "id": 1,
        "first_name": "user",
        "last_name": "name"
    },
    "created_at": "2020-04-06T03:23:26.122544Z",
    "updated_at": "2020-04-06T03:23:26.122555Z"
} {
    "id": 2,
    "date": "2020-04-07T03:23:24Z",
    "location": "Denver, CO",
    "forecast": "Sunny",
    "forecast_img": "sunshine",
    "activity": {
        "id": 2,
        "name": "Biking",
        "muscle_groups": [
            {
                "id": 4,
                "name": "Calves",
                "exercise_set": [
                    {
                        "id": 1,
                        "name": "Pull Ups",
                        "description": "Pull yourself up ya dingus",
                        "img_url": "fake_img"
                    },
                    {
                        "id": 2,
                        "name": "Curls",
                        "description": "curl some heavy weights",
                        "img_url": "some_img"
                    },
                    {
                        "id": 3,
                        "name": "Push Ups",
                        "description": "Push yo' self",
                        "img_url": "some_img"
                    },
                    {
                        "id": 4,
                        "name": "Small Arm Circles",
                        "description": "Feel the burn",
                        "img_url": "some_img"
                    },
                    {
                        "id": 5,
                        "name": "Big Arm Circles",
                        "description": "Feel the bigger burn",
                        "img_url": "some_img"
                    },
                    {
                        "id": 6,
                        "name": "Jumping Jacks",
                        "description": "Don't stop, get it, get it",
                        "img_url": "some_img"
                    },
                ]
            },
            {
                "id": 5,
                "name": "Knees",
                "exercise_set": [
                    {
                        "id": 1,
                        "name": "Pull Ups",
                        "description": "Pull yourself up ya dingus",
                        "img_url": "fake_img"
                    },
                    {
                        "id": 3,
                        "name": "Push Ups",
                        "description": "Push yo' self",
                        "img_url": "some_img"
                    },
                    {
                        "id": 4,
                        "name": "Small Arm Circles",
                        "description": "Feel the burn",
                        "img_url": "some_img"
                    },
                ]
            }
        ]
    },
    "user": {
        "id": 1,
        "first_name": "user",
        "last_name": "name"
    },
    "created_at": "2020-04-03T03:23:26.122544Z",
    "updated_at": "2020-04-03T03:23:26.122555Z"
},
```

- GET `/api/v1/:user_id/scheduled_activities`
```
{
   "id": 1,
   "username": "test_user",
   "first_name": test,
   "last_name": user,
   "scheduled_activities": [
       {
        "activity_name": "Mountain Biking",
        "date": "2020-04-10",
        "location": "Denver, CO",
        "forecast": "Sunny",
        "forecast_img": "sunny"
       } ,
      {
        "activity_name": "Kayaking",
        "date": "2020-04-22",
        "location": "Golden, CO",
        "forecast": "Overcast",
        "forecast_img": "cloudy"
       } ,
   ]
}
```