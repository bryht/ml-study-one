# ML-STUDY-ONE

![img1](./docs/image1.png)

* set data : http://localhost:6001/docs

`curl -Uri http://localhost:6001 -Method POST -ContentType "application/json" -Body '{"timestamp":"2022-10-25 12:00:00","humidity": "60", "temperature": "100"}'`

* get data : http://localhost:6002/docs

`curl http://localhost:6002 | Select-Object -Expand RawContent` 