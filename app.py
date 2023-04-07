from flask import Flask, request
app=Flask(__name__)
hackathons_list={
    "GHW_API Week":{
        "start_date":"2023-04-03 12:00:00",
        "end_date":"2023-04-10 12:00:00",
        "location":"Everywhere, online",
        "type":"Digital only"
    }, 
    "Bitcamp":{
        "start_date":"2023-04-07 12:00:00",
        "end_date":"2023-04-09 12:00:00",
        "location":"College Park, Maryland",
        "type":"In-Person only"
    }
}
@app.route("/")
def hello_ghw():
    return"<p>Hello You gorgeous<p>"

@app.route('getHackathons', methods=['GET'])
def getHackathons():
    return hackathons_list

if __name__=="__main_2":
    app.run(debug=True)