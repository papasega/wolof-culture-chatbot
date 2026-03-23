import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted


class ActionGiveProverb(Action):
    """Action to give a random Wolof proverb with its meaning."""

    def name(self) -> Text:
        return "action_give_proverb"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        proverbs = [
            {
                "wolof": "Ku muñ muññ na.",
                "meaning": "Ki muñ, moo gëna am njariñ. (La patience est la clé du succès.)",
            },
            {
                "wolof": "Nit nit ay garab am.",
                "meaning": "Nit ki moy garab nit ki. (L'homme est le remède de l'homme.)",
            },
            {
                "wolof": "Ndey-jigéen du sàcc doom.",
                "meaning": "Yaay du wàcce doom ji. (La mère n'abandonne jamais son enfant.)",
            },
            {
                "wolof": "Góor du gis tànk, du ñàkk yoon.",
                "meaning": "Góor bu am xel mënul rëcc. (Un homme avisé ne se perd pas.)",
            },
            {
                "wolof": "Lu nekk ci biir ndox, xam na luy daanu.",
                "meaning": "Ku am xam-xam xam na fu mu jëm. (Celui qui sait, connaît sa direction.)",
            },
            {
                "wolof": "Bul toog foofu, dinga am gerte.",
                "meaning": "Liggéeyal sa bopp. (Travaille pour toi-même.)",
            },
            {
                "wolof": "Ku am jom am na loxo.",
                "meaning": "Ki am jom, mën na def lu mu bëgg. (Celui qui a de la dignité peut tout faire.)",
            },
            {
                "wolof": "Degg-degg moy garab gëna baax.",
                "meaning": "Dëgg-dëgg mooy garab gu ñuul. (La vérité est le meilleur remède.)",
            },
            {
                "wolof": "Ku bëgg ndox, wara na muñ taw.",
                "meaning": "Su ngay bëgg lenn, wara nga liggéey ngir am ko. (Pour obtenir, il faut travailler.)",
            },
            {
                "wolof": "Garab gu nekk ci tool, du mën yokk sa bopp.",
                "meaning": "Nit ki, soxla na yeneen nit. (Personne ne peut grandir seul.)",
            },
            {
                "wolof": "Baat bu baax, mën na faj feebar.",
                "meaning": "Baat bu neex mën na wer nit. (Une bonne parole peut guérir.)",
            },
            {
                "wolof": "Ku yaakaar Yàlla, du ñàkk dara.",
                "meaning": "Ki am ngëm ci Yàlla, mënul ñàkk. (Celui qui a foi en Dieu ne manquera de rien.)",
            },
            {
                "wolof": "Jëf ju baax, du rëcc.",
                "meaning": "Su nga def lu baax, du fàtte. (Une bonne action ne se perd jamais.)",
            },
            {
                "wolof": "Lu tey metti, elëk dina gëna baax.",
                "meaning": "Bul ñàkk jëmm, elëk dina gëna. (Ce qui est dur aujourd'hui sera meilleur demain.)",
            },
            {
                "wolof": "Ndimbal mooy loxo bu yore dundu.",
                "meaning": "Jàppale mooy dundu. (L'entraide, c'est la vie.)",
            },
        ]

        proverb = random.choice(proverbs)
        message = f"🌿 Lëbb : « {proverb['wolof']} »\n💡 {proverb['meaning']}"
        dispatcher.utter_message(text=message)

        return []


class ActionDefaultFallback(Action):
    """Fallback action when the bot does not understand."""

    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        fallback_messages = [
            "Baal ma, dëgguma sa wax bi. Ndax mën nga ko wax ci beneen yoon ?",
            "Xamu ma li ngay wax. Jéemaal ko wax ci yeneen baat.",
            "Baal ma, mënuma tontu lolu. Laaj ma ci beneen yoon.",
            "Hmm, dëgguma lu baax. Ndax mën nga simplifier sa laaj bi ?",
        ]

        dispatcher.utter_message(text=random.choice(fallback_messages))

        return [UserUtteranceReverted()]
