def test_public_api(client, app):
    response = client.get("/v2/openapi.json")
    assert response.status_code == 200
    assert response.json == {
        "components": {
            "schemas": {
                "BookingFormula": {
                    "description": "An enumeration.",
                    "enum": ["PLACE", "ABO", ""],
                    "title": "BookingFormula",
                },
                "BookingOfferType": {
                    "description": "An enumeration.",
                    "enum": ["BIEN", "EVENEMENT"],
                    "title": "BookingOfferType",
                },
                "ValidationError": {
                    "description": "Model " "of a " "validation " "error " "response.",
                    "items": {"$ref": "#/components/schemas/ValidationErrorElement"},
                    "title": "ValidationError",
                    "type": "array",
                },
                "ValidationErrorElement": {
                    "description": "Model " "of " "a " "validation " "error " "response " "element.",
                    "properties": {
                        "ctx": {"title": "Error " "context", "type": "object"},
                        "loc": {"items": {"type": "string"}, "title": "Missing " "field " "name", "type": "array"},
                        "msg": {"title": "Error " "message", "type": "string"},
                        "type": {"title": "Error " "type", "type": "string"},
                    },
                    "required": ["loc", "msg", "type"],
                    "title": "ValidationErrorElement",
                    "type": "object",
                },
                "GetBookingResponse": {
                    "properties": {
                        "bookingId": {"title": "Bookingid", "type": "string"},
                        "dateOfBirth": {"title": "Dateofbirth", "type": "string"},
                        "datetime": {"title": "Datetime", "type": "string"},
                        "ean13": {"nullable": True, "title": "Ean13", "type": "string"},
                        "email": {"title": "Email", "type": "string"},
                        "formula": {"$ref": "#/components/schemas/BookingFormula"},
                        "isUsed": {"title": "Isused", "type": "boolean"},
                        "offerId": {"title": "Offerid", "type": "integer"},
                        "offerName": {"title": "Offername", "type": "string"},
                        "offerType": {"$ref": "#/components/schemas/BookingOfferType"},
                        "phoneNumber": {"title": "Phonenumber", "type": "string"},
                        "price": {"title": "Price", "type": "number"},
                        "publicOfferId": {"title": "Publicofferid", "type": "string"},
                        "quantity": {"title": "Quantity", "type": "integer"},
                        "theater": {"title": "Theater", "type": "object"},
                        "userName": {"title": "Username", "type": "string"},
                        "venueAddress": {"nullable": True, "title": "Venueaddress", "type": "string"},
                        "venueDepartmentCode": {"nullable": True, "title": "Venuedepartmentcode", "type": "string"},
                        "venueName": {"title": "Venuename", "type": "string"},
                    },
                    "required": [
                        "bookingId",
                        "dateOfBirth",
                        "datetime",
                        "email",
                        "formula",
                        "isUsed",
                        "offerId",
                        "publicOfferId",
                        "offerName",
                        "offerType",
                        "phoneNumber",
                        "price",
                        "quantity",
                        "theater",
                        "userName",
                        "venueName",
                    ],
                    "title": "GetBookingResponse",
                    "type": "object",
                },
                "UpdateVenueStockBodyModel": {
                    "description": "Available stock quantity for a book",
                    "properties": {
                        "available": {"minimum": 0, "title": "Available", "type": "integer"},
                        "price": {
                            "description": "(Optionnel) Prix en Euros avec 2 d??cimales possibles",
                            "title": "Price",
                            "nullable": True,
                            "type": "number",
                        },
                        "ref": {"description": "Format: EAN13", "title": "ISBN", "type": "string"},
                    },
                    "required": ["ref", "available"],
                    "title": "Stock",
                    "type": "object",
                },
                "UpdateVenueStocksBodyModel": {
                    "properties": {
                        "stocks": {
                            "items": {"$ref": "#/components/schemas/UpdateVenueStockBodyModel"},
                            "title": "Stocks",
                            "type": "array",
                        }
                    },
                    "required": ["stocks"],
                    "title": "Venue's stocks update body",
                    "type": "object",
                },
            },
            "securitySchemes": {
                "ApiKeyAuth": {"description": "Api key issued by passculture", "scheme": "bearer", "type": "http"},
                "SessionAuth": {
                    "in": "cookie",
                    "name": "session",
                    "type": "apiKey",
                },
            },
        },
        "info": {"title": "pass Culture pro public API v2", "version": "2"},
        "openapi": "3.0.3",
        "paths": {
            "/v2/bookings/cancel/token/{token}": {
                "patch": {
                    "description": "Bien que, dans le cas d???un ??v??nement, l\u2019utilisateur ne peut plus annuler sa r??servation 72h avant le d??but de ce dernier, cette API permet d\u2019annuler la r??servation d\u2019un utilisateur si elle n\u2019a pas encore ??t?? valid??.",
                    "operationId": "patchBookingsPatchCancelBookingByToken",
                    "parameters": [
                        {
                            "description": "",
                            "in": "path",
                            "name": "token",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "responses": {
                        "204": {"description": "La contremarque a ??t?? annul??e avec succ??s"},
                        "401": {"description": "Authentification n??cessaire"},
                        "403": {
                            "description": "Vous n'avez pas les droits n??cessaires pour annuler cette contremarque ou la r??servation a d??j?? ??t?? valid??e"
                        },
                        "404": {"description": "La contremarque n'existe pas"},
                        "410": {"description": "La contremarque a d??j?? ??t?? annul??e"},
                        "422": {
                            "description": "Unprocessable Entity",
                            "content": {
                                "application/json": {"schema": {"$ref": "#/components/schemas/ValidationError"}}
                            },
                        },
                    },
                    "summary": "Annulation d'une r??servation.",
                    "tags": ["API Contremarque"],
                }
            },
            "/v2/bookings/keep/token/{token}": {
                "patch": {
                    "description": "",
                    "operationId": "patchBookingsPatchBookingKeepByToken",
                    "parameters": [
                        {
                            "description": "",
                            "in": "path",
                            "name": "token",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "responses": {
                        "204": {"description": "L'annulation de la validation de la contremarque a bien ??t?? effectu??e"},
                        "401": {"description": "Authentification n??cessaire"},
                        "403": {"description": "Vous n'avez pas les droits n??cessaires pour voir cette contremarque"},
                        "404": {"description": "La contremarque n'existe pas"},
                        "410": {
                            "description": "La requ??te est refus??e car la contremarque n'a pas encore ??t?? valid??e, a ??t?? annul??e, ou son remboursement a ??t?? initi??"
                        },
                        "422": {
                            "description": "Unprocessable Entity",
                            "content": {
                                "application/json": {"schema": {"$ref": "#/components/schemas/ValidationError"}}
                            },
                        },
                    },
                    "summary": "Annulation de la validation d'une r??servation.",
                    "tags": ["API Contremarque"],
                }
            },
            "/v2/bookings/token/{token}": {
                "get": {
                    "description": "Le code \u201ccontremarque\u201d ou \"token\" est une cha\u00eene de caract??res permettant d\u2019identifier la r??servation et qui sert de preuve de r??servation. Ce code unique est g??n??r?? pour chaque r??servation d'un utilisateur sur l'application et lui est transmis ?? cette occasion.",
                    "operationId": "getBookingsGetBookingByTokenV2",
                    "parameters": [
                        {
                            "description": "",
                            "in": "path",
                            "name": "token",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {"schema": {"$ref": "#/components/schemas/GetBookingResponse"}}
                            },
                            "description": "La contremarque existe et n\u2019est pas valid??e",
                        },
                        "401": {"description": "Authentification n??cessaire"},
                        "403": {"description": "Vous n'avez pas les droits n??cessaires pour voir cette contremarque"},
                        "404": {"description": "La contremarque n'existe pas"},
                        "410": {
                            "description": "La contremarque n'est plus valide car elle a d??j?? ??t?? valid??e ou a ??t?? annul??e"
                        },
                        "422": {
                            "description": "Unprocessable Entity",
                            "content": {
                                "application/json": {"schema": {"$ref": "#/components/schemas/ValidationError"}}
                            },
                        },
                    },
                    "security": [{"ApiKeyAuth": []}, {"SessionAuth": []}],
                    "summary": "Consultation d'une r??servation.",
                    "tags": ["API Contremarque"],
                }
            },
            "/v2/bookings/use/token/{token}": {
                "patch": {
                    "description": "Pour confirmer que la r??servation a bien ??t?? utilis??e par le jeune.",
                    "operationId": "patchBookingsPatchBookingUseByToken",
                    "parameters": [
                        {
                            "description": "",
                            "in": "path",
                            "name": "token",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "responses": {
                        "204": {"description": "La contremarque a bien ??t?? valid??e"},
                        "401": {"description": "Authentification n??cessaire"},
                        "403": {"description": "Vous n'avez pas les droits n??cessaires pour voir cette contremarque"},
                        "404": {"description": "La contremarque n'existe pas"},
                        "410": {
                            "description": "La contremarque n'est plus valide car elle a d??j?? ??t?? valid??e ou a ??t?? annul??e"
                        },
                        "422": {
                            "description": "Unprocessable Entity",
                            "content": {
                                "application/json": {"schema": {"$ref": "#/components/schemas/ValidationError"}}
                            },
                        },
                    },
                    "security": [{"ApiKeyAuth": []}, {"SessionAuth": []}],
                    "summary": "Validation d'une r??servation.",
                    "tags": ["API Contremarque"],
                }
            },
            "/v2/venue/{venue_id}/stocks": {
                "post": {
                    "description": """Seuls les livres, pr??alablement pr??sents dans le catalogue du pass Culture seront pris en compte, tous les autres stocks seront filtr??s. Les stocks sont r??f??renc??s par leur isbn au format EAN13. Le champ "available" repr??sente la quantit?? de stocks disponible en librairie. Le champ "price" (optionnel) correspond au prix en euros. Le param??tre {venue_id} correspond ?? un lieu qui doit ??tre attach?? ?? la structure ?? laquelle la cl?? d'API utilis??e est reli??e.""",
                    "operationId": "postVenueUpdateStocks",
                    "parameters": [
                        {
                            "description": "",
                            "in": "path",
                            "name": "venue_id",
                            "required": True,
                            "schema": {"format": "int32", "type": "integer"},
                        }
                    ],
                    "requestBody": {
                        "content": {
                            "application/json": {"schema": {"$ref": "#/components/schemas/UpdateVenueStocksBodyModel"}}
                        }
                    },
                    "responses": {
                        "204": {"description": "No Content"},
                        "401": {"description": "Unauthorized"},
                        "403": {"description": "Forbidden"},
                        "404": {"description": "Not Found"},
                        "422": {
                            "description": "Unprocessable Entity",
                            "content": {
                                "application/json": {"schema": {"$ref": "#/components/schemas/ValidationError"}}
                            },
                        },
                    },
                    "summary": "Mise ?? jour des stocks d'un lieu enregistr?? aupr??s du pass Culture.",
                    "tags": ["API Stocks"],
                }
            },
        },
        "security": [],
        "tags": [{"name": "API Contremarque"}, {"name": "API Stocks"}],
    }
