# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ConversationPaused, ConversationResumed
from rasa_sdk.forms import FormAction
import logging
from rasa_sdk.events import ReminderScheduled


        return []


class ActionUserMessage(FormAction):

    def name(self) -> Text:
        return "form_get_client_message"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill."""

        return ["client_name", "client_email", "client_message"]

    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],):

        # Do something dramatically here, like call an API for example lol
        dispatcher.utter_message(text='TEST')

        return []
