# ML-STUDY-ONE

![img1](./docs/image1.png)

* set data
 
`curl -Uri http://localhost:6001 -Method POST -ContentType "application/json" -Body '{"timestamp":"2022-10-25 12:00:00","humidity": "60", "temperature": "100"}'`

* get data

`curl http://localhost:6002`