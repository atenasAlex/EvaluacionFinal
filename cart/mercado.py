
import mercadopago
sdk = mercadopago.SDK("APP_USR-3f32cdbf-68d4-46a5-b68c-e595579fb8b1")

# Crea un ítem en la preferencia


preference_data = {
    "items": [
        {
            "title": "Mi producto",
            "quantity": 1,
            "unit_price": 75
        }
    ],

    "back_urls": {
        "success": "https://www.tu-sitio/success",
        "failure": "https://www.tu-sitio/failure",
        "pending": "https://www.tu-sitio/pendings"
    },
    "auto_return": "approved"
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]