import streamlit as st
from streamlit_condition_tree import condition_tree

config = {
    'fields': {
        'user': {
            'label': "User",
            'tooltip': "Group of fields",
            'type': "!struct",
            'subfields': {
                'firstName': {
                    'label2': "Username",
                    'type': "text",
                    'mainWidgetProps': {
                        'valueLabel': "Name",
                        'valuePlaceholder': "Enter name",
                    },
                },
                'login': {
                    'type': "text",
                    'tableName': "t1",
                    'mainWidgetProps': {
                        'valueLabel': "Login",
                        'valuePlaceholder': "Enter login",
                    },
                }
            }
        },
        'results': {
            'label': "Results",
            'type': "!group",
            'subfields': {
                'product': {
                    'type': "select",
                    'valueSources': ["value"],
                },
                'score': {
                    'type': "number",
                    'fieldSettings': {
                        'min': 0,
                        'max': 100,
                    },
                    'valueSources': ["value"],
                }
            }
        },
        'qty': {
            'label': "Qty",
            'type': "number",
            'fieldSettings': {
                'min': 0
            },
            'valueSources': ["value"],
            'preferWidgets': ["number"]
        },
        'price': {
            'label': "Price",
            'type': "number",
            'valueSources': ["value"],
            'fieldSettings': {
                'min': 10,
                'max': 100
            },
            'preferWidgets': ["slider", "rangeslider"]
        },
        'name': {
            'label': 'Name',
            'type': 'text',
        },
        'color': {
            'label': "Color",
            'type': "select",
            'valueSources': ["value"],
            'fieldSettings': {
                'listValues': [
                    {'value': "yellow", 'title': "Yellow"},
                    {'value': "green", 'title': "Green"},
                    {'value': "orange", 'title': "Orange"}
                ]
            }
        },
        'is_promotion': {
            'label': "Promo?",
            'type': "boolean",
            'operators': ["equal"],
            'valueSources': ["value"]
        }
    }
}

tree = {
    "type": "group",
    "children": [
        {
            "type": "rule",
            "properties": {
                "fieldSrc": "field",
                "field": "qty",
                "operator": "equal",
                "value": [
                    6568477
                ],
                "valueSrc": [
                    "value"
                ],
                "valueType": [
                    "number"
                ]
            }
        }
    ]
}

config2 = {
    'fields': {
        'name': {
            'label': 'Name',
            'type': 'text',
        },
        'qty': {
            'label': "Age",
            'type': "number",
            'fieldSettings': {
                'min': 0
            },
            'valueSources': ["value"],
            'preferWidgets': ["number"]
        },
        'like_tomatoes': {
            'label': "Like tomatoes",
            'type': "boolean",
            'operators': ["equal"],
            'valueSources': ["value"]
        }
    }
}

return_type = st.selectbox(
    'Return type',
    ['queryString', 'mongodb', 'sql',
     'spel', 'elasticSearch', 'jsonLogic']
)

placeholder = st.text_input(
    'placeholder',
    '123456abc'
)

return_val = condition_tree(
    config2,
    return_type='sql',
)

st.write(return_val)
