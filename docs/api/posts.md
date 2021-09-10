# Posts
Supports registering, viewing, and updating posts.

## Create or update a facebook post

**Request**:

`POST` `/posts/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
post_id    | string | Yes      | The id of the facebook Post
user_id    | string | Yes      | The id of the user that is the owner of the post on Facebook
likes      | int    | Yes      | Amount of likes of the post

*Note:*

- **[Authorization Protected](authentication.md)**

- If a post with that post_id already exists the content will be updated, even it is not a regular practice on the REST APIs this will make not necessary for the service to check if needs to create or update te post

**Response**:

```json
Content-Type application/json
201 Created

{
    "user_id": "u894210",
    "post_id": "p241521",
    "likes": 101
}
```


## List posts

**Request**:

`GET` `/posts/`

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

## Retrieve post

**Request**:

`GET` `/posts/:post_id`

Parameters

Name       | Type   | Required | Description
-----------|--------|----------|------------
post_id    | string | No       | The id of the facebook Post

*Note:*

- **[Authorization Protected](authentication.md)**
