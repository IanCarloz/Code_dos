{
    "name": "Remainder List",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "rm_date": {
                "type": "datetime",
                "required": true,
                "read_only": false,
                "label": "Rm date"
            },
            "title": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Title",
                "max_length": 140
            },
            "rm_user": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Rm user"
            },
            "priority_tag": {
                "type": "choice",
                "required": true,
                "read_only": false,
                "label": "Priority tag",
                "choices": [
                    {
                        "value": "N",
                        "display_name": "Normal"
                    },
                    {
                        "value": "I",
                        "display_name": "Importante"
                    },
                    {
                        "value": "U",
                        "display_name": "Urgente"
                    }
                ]
            },
            "is_alert": {
                "type": "boolean",
                "required": false,
                "read_only": false,
                "label": "Is alert"
            }
        }
    }
}

{
    "rm_date": null,
    "title": "",
    "rm_user": null,
    "priority_tag": null,
    "is_alert": false
}
