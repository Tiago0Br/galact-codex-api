from flask import Flask, jsonify, request
from app.services.swapi import SwapiService

app = Flask(__name__)

@app.get("/")
def health_check():
  return jsonify({"status": "ok", "message": "Galactic Codex API is running"}), 200

@app.get("/people")
def get_people():
  search_query = request.args.get("search")
  
  try:
    people = SwapiService.get_people(search_query)
    return jsonify([p.model_dump() for p in people]), 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.get("/planets")
def get_planets():
  search_query = request.args.get("search")
  try:
    planets = SwapiService.get_planets(search_query)
    return jsonify([p.model_dump() for p in planets]), 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.get("/starships")
def get_starships():
  search_query = request.args.get("search")
  try:
    starships = SwapiService.get_starships(search_query)
    return jsonify([s.model_dump() for s in starships]), 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.get("/films")
def get_films():
  search_query = request.args.get("search")
  try:
    films = SwapiService.get_films(search_query)
    return jsonify([f.model_dump() for f in films]), 200
  except Exception as e:
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
  app.run(debug=True, port=8080)