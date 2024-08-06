Weather Forcast Micro Service
This Micro Service uses HTTP POST requests to transfer data. 
It acts as a webserver that you send a POST request to and it will respond with a Post request holding a forcast in the body of the request.

**How to request/receive data**
1) Run the MS on your computer this will enable it to recive requests.
2) Send a POST request to 'http://127.0.0.1:5000/Short_Term_Weather' with the body containing a lat and lon. EX: (38.5810606, -121.493895).

   a) In **python** this can be acomplished with the requests module.
       EX:  include requests
            Weather_Forecast = requests.post('http://127.0.0.1:5000/Short_Term_Weather', json=(38.5810606, -121.493895)).json()['result']
   Now you have the forecast!

   b) In **js** it is a little more complex but looks like this.
           let Lat_Long = (38.5810606, -121.493895)
           async function weatherRequest(Lat_Long){
          
                 var options = {
                      method: 'POST',
              
                      url: `http://127.0.0.1:5000/Short_Term_Weather`,
                      body: Lat_Long,
              
                      json: true
                  };
              
                  var sendrequest = await request(options) 
                
                      // The parsedBody contains the data 
                      // sent back from the Flask server  
                      .then(function (parsedBody) { 
                          let result; 
                          result = parsedBody['result']; 
                          
                          return result 
                      }) 
                      .catch(function (err) { 
                          console.log(err); 
                      }); 

              let Weather_Forecast = await weatherRequest(Lat_Long)
     Now you have the forecast in the Weather_Forecast variable!
