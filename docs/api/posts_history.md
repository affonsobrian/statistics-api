# Posts History
Supports viewing history of posts

## List posts history

**Request**:

`GET` `/posthistory/`

Url parameters

Name       | Type   | Required | Description
-----------|--------|----------|------------
post_id    | string | No       | The id of the facebook Post
user_id    | string | No       | The id of the user that is the owner of the post on Facebook

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "user_id": "412412",
            "post_id": "412124412",
            "likes": 101
        },
        {
            "user_id": "u894210",
            "post_id": "p241521",
            "likes": 101
        }
    ]
}   
```


## List average amount of likes per day in the last 30 days

**Request**:

`GET` `/posthistory/month_average/`

Url parameters

Name       | Type   | Required | Description
-----------|--------|----------|------------
user_id    | string | No       | The id of the user that is the owner of the post on Facebook

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

[
    {
        "user_id": "412412",
        "created_at": "2021-09-10",
        "average_likes": 101.0
    },
    {
        "user_id": "u894210",
        "created_at": "2021-09-10",
        "average_likes": 101.0
    }
]
```
