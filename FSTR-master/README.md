# REST API for FSTR pereval.online website

![TSSR Logo](https://tssr.ru/files/materials/1879/logo.png)

The Federation for Sports Tourism in Russia maintains a database of mountain passes that receives tourist contributions. The FSTR group of experts verifies the information and saves it to the database.
This is an API solution for a mobile application, which can be used by tourists to submit mountain pass data and
send it to FSTR once they have internet access.

When tourists reach a mountain pass, they can take pictures and use the mobile application to submit the information.
Once a tourist clicks "Send", the mobile application calls submitData method, which accepts data in JSON format.

Example JSON data:
```json
{
  "beauty_title": "pass ",
  "title": "Pkhia",
  "other_titles": "Triyev",
  "connect": "",
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Pupkin",
		 "name": "Vasily",
		 "otc": "Ivanovich",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  "level":{"winter": "", 
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   "images": [{"data":"<img1>", "title":"Saddle"}, {"data":"<img2>", "title":"Ascend"}]
}
```

The result of submission is status and status message. For example:
```json
{ "status": 200, "message": "OK"}
```
Once an object is submitted, it is assigned "new" status. FSTR experts change its status to "pending" meaning 
an expert is working on it, validate the new object, and then change the status either to "accepted" or "rejected". 

## API methods
#### GET /submitData/ method
Returns a list of all mountain passes.

#### POST /submitData/ method
Allows for a single mountain pass submission.

#### GET /submitData/{id}
Retrieves data for a particular mountain pass.

#### PATCH /submitData/{id}
Allows to change a mountain pass attribute values.
Returns a JSON response with 
- state: 1 for successful update and 0 for unsuccessful update
- message: explains why an update has failed

#### GET/submitData/?user__email=\<email>
Return a list of all objects that were sent to the system by the user with the specified email address

You can try using the API methods at https://imikhassik.pythonanywhere.com/swagger-ui