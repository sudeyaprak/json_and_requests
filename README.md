![image](https://user-images.githubusercontent.com/119863892/235365495-7e5728f1-b9af-4681-8f23-17e2863e7615.png)

# Ecosnap API

Ecosnap aims to collect real-time citizen participation in the determination of enviromental and health problems during the creation of urban planning.

Ecosnap mobile application enables to report an array of incidents:

- Weak Wifi
- Enviromental Pollution
- Bad Sidewalk
- Electrical Problem
- Wrong Parking
- Waste 
- Other Problems

## Individual Project

### 1. Obtaining Our User ID from Postman

- URL: https://peer-review.hacettepe.edu.tr/v1/api/studentactivity/login
- Parameters:
```json
{
  "email": "*****@*****.com",
  "password": "********"
}
```
- Method: Post
 <img width="860" alt="image" src="https://user-images.githubusercontent.com/119863892/235366151-fefd7b4a-9abb-4844-9596-67ecec71e34d.png">


### 2. Obtaining Data We Submitted to Ecosnap

- URL: https://peer-review.hacettepe.edu.tr/v1/api/studentactivity?UserId=********-****-****-****-
  - ********-**** = user id that we found at the previous step
- Method: Get
<img width="866" alt="image" src="https://user-images.githubusercontent.com/119863892/235366364-29cacd1c-bc08-44ae-9e71-e0dc922fc365.png">


### 3. Retrieving The Same Data from Python

<img width="488" alt="image" src="https://user-images.githubusercontent.com/119863892/235371308-cacb27dc-7c78-46df-8725-43d3dc33f766.png">

<img width="642" alt="image" src="https://user-images.githubusercontent.com/119863892/235371380-c77dcbca-c62c-49fd-9fc5-38531de93d5f.png">

<img width="603" alt="image" src="https://user-images.githubusercontent.com/119863892/235373894-9178050e-91da-4e4d-9e3b-f325c8e04a44.png">



### 4. Ecosnap with 5 Example Post

- Enviromental Pollution

![WhatsApp Image 2023-04-30 at 20 11 08](https://user-images.githubusercontent.com/119863892/235366774-23ab8fd5-3141-44b1-bab7-6fb8317d0656.jpeg)

- Wrong Parking

![WhatsApp Image 2023-04-30 at 20 11 06 (1)](https://user-images.githubusercontent.com/119863892/235366836-6c8e8bf2-400f-4720-b05f-3e8046b1e7a1.jpeg)

- Bad Sidewalk

![WhatsApp Image 2023-04-30 at 20 11 05 (1)](https://user-images.githubusercontent.com/119863892/235366880-61c6ba96-1fa2-453d-bdd7-39421b5772c6.jpeg)

- Electrical Problem

![WhatsApp Image 2023-04-30 at 20 11 07](https://user-images.githubusercontent.com/119863892/235366917-82898593-cd59-4dfb-96e2-7ab2fe4acc09.jpeg)

- Other Problems

![WhatsApp Image 2023-04-30 at 20 11 05](https://user-images.githubusercontent.com/119863892/235366933-27bf541a-1910-49c4-9d7d-23f8b6d9c932.jpeg)


### 5. Display The Activity Types on an Interactive Map

<img width="616" alt="image" src="https://user-images.githubusercontent.com/119863892/235374813-07d9eb1b-752a-4117-902f-19a6efca751e.png">

<img width="214" alt="image" src="https://user-images.githubusercontent.com/119863892/235374727-bc55d4c6-ae3c-4e69-b37d-5e2dd65da9bf.png">

<img width="188" alt="image" src="https://user-images.githubusercontent.com/119863892/235374757-50e1daa7-3b55-4f11-b0ff-fec6559b8902.png">
