from __future__ import annotations

from typing import Any

ECHOFEEED_JSON_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["feedA", "feedB", "comparison"],
    "properties": {
        "feedA": {"$ref": "#/$defs/feed"},
        "feedB": {"$ref": "#/$defs/feed"},
        "comparison": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "framingDifference",
                "emotionalDifference",
                "bubbleRisk",
                "manipulationRisk",
                "polarizationRisk",
                "retentionPressure",
                "criticalConclusion",
                "finalQuestion",
            ],
            "properties": {
                "framingDifference": {
                    "type": "string",
                    "description": "Explique como o mesmo tema foi enquadrado de formas diferentes nos dois feeds.",
                    "minLength": 40,
                    "maxLength": 700,
                },
                "emotionalDifference": {
                    "type": "string",
                    "description": "Explique a diferença emocional entre os feeds.",
                    "minLength": 40,
                    "maxLength": 700,
                },
                "bubbleRisk": {"type": "integer", "minimum": 0, "maximum": 100},
                "manipulationRisk": {"type": "integer", "minimum": 0, "maximum": 100},
                "polarizationRisk": {"type": "integer", "minimum": 0, "maximum": 100},
                "retentionPressure": {"type": "integer", "minimum": 0, "maximum": 100},
                "criticalConclusion": {
                    "type": "string",
                    "description": "Conclusão crítica sobre hiperpersonalização, cultura comum e redes sociais.",
                    "minLength": 80,
                    "maxLength": 900,
                },
                "finalQuestion": {
                    "type": "string",
                    "description": "Uma pergunta provocativa para encerrar a apresentação.",
                    "minLength": 20,
                    "maxLength": 250,
                },
            },
        },
    },
    "$defs": {
        "feed": {
            "type": "object",
            "additionalProperties": False,
            "required": ["profileName", "dominantNarrative", "posts"],
            "properties": {
                "profileName": {
                    "type": "string",
                    "description": "Nome curto do perfil simulado.",
                    "minLength": 3,
                    "maxLength": 90,
                },
                "dominantNarrative": {
                    "type": "string",
                    "description": "Narrativa dominante construída pelo algoritmo para esse perfil.",
                    "minLength": 30,
                    "maxLength": 400,
                },
                "posts": {
                    "type": "array",
                    "description": "Três posts simulados para esse perfil.",
                    "minItems": 3,
                    "maxItems": 3,
                    "items": {"$ref": "#/$defs/post"},
                },
            },
        },
        "post": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "title",
                "hook",
                "caption",
                "visualStyle",
                "emotionalTone",
                "retentionTrigger",
                "algorithmicIntent",
                "possibleEffect",
                "bubbleRisk",
                "manipulationRisk",
            ],
            "properties": {
                "title": {"type": "string", "minLength": 10, "maxLength": 120},
                "hook": {"type": "string", "minLength": 10, "maxLength": 220},
                "caption": {"type": "string", "minLength": 20, "maxLength": 450},
                "visualStyle": {"type": "string", "minLength": 10, "maxLength": 220},
                "emotionalTone": {"type": "string", "minLength": 3, "maxLength": 80},
                "retentionTrigger": {"type": "string", "minLength": 10, "maxLength": 220},
                "algorithmicIntent": {"type": "string", "minLength": 10, "maxLength": 220},
                "possibleEffect": {"type": "string", "minLength": 20, "maxLength": 350},
                "bubbleRisk": {"type": "integer", "minimum": 0, "maximum": 100},
                "manipulationRisk": {"type": "integer", "minimum": 0, "maximum": 100},
            },
        },
    },
}
