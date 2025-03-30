{
  "openapi": "3.0.0",
  "info": {
    "title": "GPT-Trader-Pro Actions",
    "version": "1.0.0"
  },
  "paths": {
    "/generate-signal": {
      "post": {
        "summary": "Génère un signal de trading basé sur un contexte",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "context": {
                    "type": "string"
                  }
                },
                "required": ["context"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Réponse contenant le signal",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "signal": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
