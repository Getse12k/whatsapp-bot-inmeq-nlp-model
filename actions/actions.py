from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionStartService(Action):

    def name(self) -> Text:
        return "action_iniciar_atendimento"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        menu = """Olá, seja bem-vindo ao Instituto de Metrologia e Qualidade Industrial. Vamos começar seu atendimento: O que você deseja?\n
        - Tirar duvidas\n
        - Atendimento a oficinas permissionárias\n
        - Solicitação de serviço\n
        - Informações sobre o processo de fiscalização\n
        - Boletos\n
        - Segunda via renegociações de débitos\n
        - CADIN\n
        - Informações processuais\n
        - Dar sugestões\n
        - Reclamações\n"""

        dispatcher.utter_message(text=menu)

        return []

